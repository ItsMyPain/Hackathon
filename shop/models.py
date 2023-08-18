from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.CharField(max_length=100, unique=True, verbose_name='Почта')
    password = models.CharField(max_length=128, unique=True, verbose_name='Пароль')

    state_id = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время регистрации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
