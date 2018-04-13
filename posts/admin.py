from django.contrib import admin

from .models import Post, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Post._meta.get_fields()]
    # list_display_links = [field.name for field in Post._meta.get_fields()]

    def name(self):
        pass

admin.site.register(Post)
admin.site.register(Category)
