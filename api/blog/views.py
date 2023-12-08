import os
from rest_framework import viewsets, generics, status, filters, pagination
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.http import FileResponse
from django.contrib.auth import get_user_model
from django.views import View
from django.shortcuts import redirect
from django.conf import settings
from .serializers import UserSerializer, BlogSerializer
from .models import BlogPost
User = get_user_model()

# Criação de usuário
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status.HTTP_201_CREATED, headers=headers)

# Edição do usuário
class UserUpdateView(generics.RetrieveUpdateAPIView):
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

# CRUD do BlogPost

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100

class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'content']
    ordering_fields = ('title', 'create_at')
    ordering = ['create_at']
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticated]


# Termos de uso e política de privacidade via pasta no projeto
class PrivacyPolicyView(View):
    def get(self, request):
        pdf_path = os.path.join(settings.BASE_DIR, 'api/documents/privacy-policy.pdf')
        response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=documento.pdf'
        return response

# Termos de uso e política de privacidade via Drive

def view_pdf(request):
    pdf_url = pdf_url = f"https://drive.google.com/uc?id=15AMkH17xmZmxJObfYREmLgwMTJ4HQSZk"
    return redirect(pdf_url)
