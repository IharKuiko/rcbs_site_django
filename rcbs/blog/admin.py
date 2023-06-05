from django.contrib import admin

from .models import Posts, Category, Tag


admin.register(Posts)
admin.register(Category)
admin.register(Tag)
