from rest_framework import routers
from django.urls import path, include
from .views import UserCreateView, PrivacyPolicyView, view_pdf, BlogViewSet, UserUpdateView

router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('user/register/', UserCreateView.as_view(), name='create-user'),
    path('user/update/', UserUpdateView.as_view(), name='edit-user'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='pdf-view'),
    path('privacy/', view_pdf, name='drive-pdf-view')
]