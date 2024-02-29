from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserViewSet, AuthorViewSet, UserProductAccessViewSet, LessonViewSet, ProductViewSet, GroupViewSet, LessonListAPIView

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'userproductaccess', UserProductAccessViewSet)
router.register(r'product', ProductViewSet)
router.register(r'lesson', LessonViewSet)
router.register(r'group', GroupViewSet)
urlpatterns = [
    *router.urls,
    path('products/<int:product_id>/lessons/', LessonListAPIView.as_view(), name='lesson-list'),
]