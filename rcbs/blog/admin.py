from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import Post, Category, Tag


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_image')
    list_display_links = ('id', 'title', 'get_image')
    search_fields = ('title',)
    list_filter = ('category',)
    readonly_fields = ('views', 'created_at', 'get_image')
    fields = ('title', 'slug', 'category', 'tags', 'description', 'content', 'is_published', 'image', 'get_image', 'views', 'created_at')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '-'

    get_image.short_description = 'Фото'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
