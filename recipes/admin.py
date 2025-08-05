from django.contrib import admin
from .models import Recipe, Category, Comment, Like


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at', 'category')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'recipe', 'created_at')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user__username', 'recipe__title')


class SafeRecipeAdmin(admin.ModelAdmin):
    # ...
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
