from django.contrib import admin
from .models import Quote,Questions,PageHit,PostImages,Post,PostComments,Like

# Register your models here.

admin.site.register(Quote)
admin.site.register(Questions)

class PostImgTabularInline(admin.TabularInline):
    model = PostImages

class PostsAdmin(admin.ModelAdmin):
    inlines = [PostImgTabularInline]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(PostComments)
admin.site.register(Post,PostsAdmin)
admin.site.register(PostImages)
admin.site.register(PageHit)
admin.site.register(Like)