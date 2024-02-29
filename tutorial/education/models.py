from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
        
    def __str__(self):
        return self.name

   
class Author(models.Model):
    name = models.CharField(max_length=100)
       
    def __str__(self):
        return self.name


class Product(models.Model):
    creator = models.ForeignKey(Author, on_delete=models.CASCADE)  # Создатель продукта
    name = models.CharField(max_length=100)  # Название продукта
    start_date = models.DateTimeField()  # Дата и время старта
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Стоимость продукта
    min_users = models.IntegerField()  # Минимальное количество пользователей в группе
    max_users = models.IntegerField()  # Максимальное количество пользователей в группе
    
    def __str__(self):
        return self.name
 
    
class UserProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    has_access = models.BooleanField(default=False)
    

class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Продукт, к которому относится урок
    name = models.CharField(max_length=100)  # Название урока
    video_link = models.URLField()  # Ссылка на видео
    
    def __str__(self):
        return self.name
    
class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Продукт, к которому относится группа
    name = models.CharField(max_length=100)  # Название группы
    users = models.ManyToManyField(User, related_name='groups')  # Ученики, состоящие в группе
    
    def __str__(self):
        return self.name
    