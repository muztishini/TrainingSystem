from django.contrib import admin
from .models import User, UserProductAccess, Lesson, Product, Group, Author


admin.site.register(User)
admin.site.register(Author)
admin.site.register(UserProductAccess)
admin.site.register(Lesson)
admin.site.register(Product)
admin.site.register(Group)
