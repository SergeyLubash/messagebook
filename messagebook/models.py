from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    phone = models.BigIntegerField(verbose_name='Номер телефона')
    dateofbirth = models.DateField(verbose_name='Дата рождения')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']


class Comments(models.Model):
    user_comment = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Автор')
    text_comment = models.TextField(max_length=300, verbose_name='Текст комментария')
    post_comment = models.ForeignKey('Posts', on_delete=models.CASCADE, verbose_name='Пост')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.post_comment}'


class Posts(models.Model):
    title = models.CharField(max_length=20, verbose_name='Заголовок')
    description = models.TextField(max_length=300, verbose_name='Текст сообщения')
    photo = models.ImageField(upload_to='photos/', blank=True,  verbose_name='Изображение')
    user_post = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Автор')
    post_сomment = models.ManyToManyField('Comments', blank=True, verbose_name='Комментарии')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['title']

    def __str__(self):
        return self.title

    def display_сomment(self):
        return ', '.join([сomment.text_comment for сomment in self.post_сomment.all()])

    display_сomment.short_description = 'Комментарии'
