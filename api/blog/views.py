import os, jwt
from rest_framework import views, viewsets, generics, status, filters, pagination
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend
from django.http import FileResponse
from django.contrib.sites.shortcuts import get_current_site
from django.views import View
from django.conf import settings
from django.urls import reverse
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from .serializers import UserSerializer, BlogSerializer, RestrictBlogSerializer, EmailVerificationSerializer
from .models import User, BlogPost, RestrictBlogPost
from .utils import Util
from .permissions import IsVerifiedUser

# Criação de usuário
@extend_schema(
        description="Custom description for create user"
)
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        user_data = serializer.data
      
        user_created = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user_created).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('verify-email')
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi ' + user_created.username +' \nTo verify your accont use the link bellow \n'+ absurl
        data = {'email_body': email_body, 'to_email': user_created.email,'email_subject': 'Verify your email'}
        Util.send_email(data)

        headers = self.get_success_headers(user_data)
        return Response(user_data, status.HTTP_201_CREATED, headers=headers)
    
# Edição do usuário
class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        if 'password' in request.data:
            user.set_password(request.data['password'])
            user.save()

        return Response(serializer.data)


@extend_schema(
    parameters=[OpenApiParameter(name='token', type=str, location=OpenApiParameter.QUERY, description='Description')]
)

class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer

    def get(self, request):
        token = request.query_params.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Sucessfully activated'}, status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired, contact the admin'}, status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token, contact the admin'}, status.HTTP_400_BAD_REQUEST)

# CRUD do BlogPost

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 20

class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, SearchFilter]
    filterset_fields = ['draft']
    search_fields = ['title', 'content']
    ordering_fields = ('title', 'create_at')
    ordering = ['create_at']
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
    
class RestrictBlogViewSet(viewsets.ModelViewSet):
    queryset = RestrictBlogPost.objects.all()
    serializer_class = RestrictBlogSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, SearchFilter]
    filterset_fields = ['draft']
    search_fields = ['title', 'content']
    ordering_fields = ('title', 'create_at')
    ordering = ['create_at']
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticated, IsVerifiedUser]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

@extend_schema(
        description="Retrieve the privacy policy document.",
        responses={200: OpenApiResponse("PDF file")},
)
# Termos de uso e política de privacidade via pasta no projeto
class PrivacyPolicyView(View):
    def get(self, request):
        pdf_path = os.path.join(settings.BASE_DIR, 'api/documents/privacy-policy.pdf')
        response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=privacy-policy.pdf'
        return response