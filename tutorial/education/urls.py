from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AuthorViewSet, UserProductAccessViewSet, LessonViewSet, ProductViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'userproductaccess', UserProductAccessViewSet)
router.register(r'product', ProductViewSet)
router.register(r'lesson', LessonViewSet)
router.register(r'group', GroupViewSet)
urlpatterns = router.urls
