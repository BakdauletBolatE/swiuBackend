from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Quote)
admin.site.register(Questions)

class PostImgTabularInline(admin.TabularInline):
    model = PostImages

class PostsAdmin(admin.ModelAdmin):
    inlines = [PostImgTabularInline]
    list_filter = ('category',)
    list_display = ('title','category','created_at')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(PostComments)
admin.site.register(Post,PostsAdmin)
admin.site.register(PostImages)
admin.site.register(PageHit)
admin.site.register(Like)
admin.site.register(PostCategories)
admin.site.register(Request)