from rest_framework import routers
from django.urls import path, include
from .views import UserRegisterView, UserUpdateView, BlogViewSet, RestrictBlogViewSet, VerifyEmail, ResendVerificationEmail, PrivacyPolicyView

router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet)
router.register(r'restricted-blog', RestrictBlogViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('user/register/', UserRegisterView.as_view(), name='create-user'),
    path('user/update/', UserUpdateView.as_view(), name='edit-user'),
    path('user/verify-email/', VerifyEmail.as_view(), name='verify-email'),
    path('user/resend-verification-email/', ResendVerificationEmail.as_view(), name='resend-verification-email'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='pdf-view')
]