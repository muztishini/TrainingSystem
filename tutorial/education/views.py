from rest_framework import viewsets
from .models import User, Author, UserProductAccess, Lesson, Product, Group
from .serializers import UserSerializer, AuthorSerializer, UserProductAccessSerializer, LessonSerializer, ProductSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()    
    
    
class UserProductAccessViewSet(viewsets.ModelViewSet):
    serializer_class = UserProductAccessSerializer
    queryset = UserProductAccess.objects.all()
    
    
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    
class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    
    
class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()