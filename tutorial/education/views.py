from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
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
        
        
class LessonListAPIView(APIView):
    def get(self, request, product_id):
        user = request.user  # Получаем текущего пользователя

        # Проверяем доступ пользователя к указанному продукту
        if not UserProductAccess.objects.filter(user=user, product_id=product_id).exists():
            return Response({"error": "У вас нет доступа к этому продукту"}, status=status.HTTP_403_FORBIDDEN)

        # Получаем список уроков для указанного продукта
        lessons = Lesson.objects.filter(product_id=product_id)

        # Сериализуем список уроков и возвращаем его
        serialized_lessons = LessonSerializer(lessons, many=True)
        return Response(serialized_lessons.data, status=status.HTTP_200_OK)
    