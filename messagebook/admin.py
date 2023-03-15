from django.contrib import admin
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.html import format_html

from messagebook.models import Users, Posts, Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user_link', 'text_comment', 'updated_at', 'post_link')
    search_fields = ('post_comment',)

    def user_link(self, obj):
        user = obj.user_comment
        url = reverse("admin:messagebook_users_changelist") + str(user.pk)
        return format_html(f'<a href="{url}">{user}</a>')

    user_link.short_description = 'Автор'

    def post_link(self, obj):
        post = obj.post_comment
        url = reverse("admin:messagebook_posts_changelist") + str(post.pk)
        return format_html(f'<a href="{url}">{post}</a>')

    post_link.short_description = 'Пост'


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'display_сomment', 'user_link')
    list_filter = ('created_at',)
    search_fields = ('title',)

    def user_link(self, obj):
        user = obj.user_post
        url = reverse("admin:messagebook_users_changelist") + str(user.pk)
        return format_html(f'<a href="{url}">{user}</a>')

    user_link.short_description = 'Автор'


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone', 'dateofbirth')
    list_display_links = ('username',)


admin.site.register(Users, UsersAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(Comments, CommentsAdmin)
