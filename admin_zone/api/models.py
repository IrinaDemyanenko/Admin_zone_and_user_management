from django.db import models
from django.contrib.auth.models import AbstractUser


CHOICES = {
    'user': 'USER',
    'moderator': 'MODERATOR',
    'admin': 'ADMIN',
}

class CustomUser(AbstractUser):
    """Кастомная модель пользователя, добавляющая:

     - пользовательские роли к существующей модели;
     - поле username должно быть уникальным в сервисе;
     - поле email становится обязательным, должно быть уникальным;
     - сочетание полей email и username должно быть уникальным.
    """
    role = models.CharField(
        verbose_name='Роль', max_length=15, choices=CHOICES, default='user'
        )

    username = models.CharField(
        verbose_name='Выбранное имя', max_length=150, unique=True, blank=False
    )

    email = models.EmailField(verbose_name='Почта', blank=False, unique=True)

    class Meta:
        # зададим ограничение на модель, чтобы пара полей
        # username email были уникальными
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'], name='uniqe_username_email'
                ),
        ]

    # создадим приватные атибуты класса, чтобы получать информацию о
    # роли пользователя; напишем в стилистике Django как is_staff is_superuser
    # т.е. прописали только getter, можем только считывать информацию,
    # setter прописывать не будем, тк роли будет назначать админ или
    # суперпользователь

    # является ли пользователь админом?
    # да если в поле роль указано 'admin' или
    # если в стандартных полях Django как is_staff и is_superuser значение True
    @property
    def is_admin(self):
        """Является ли пользователь админом?
        Да, если в поле role указано 'admin' или
        если в стандартных полях Django как is_staff и is_superuser
        значение True.
        Админ имеет право на управление всем контентом проекта.
        """
        return self.is_staff or self.is_superuser or self.role == 'admin'

    # является ли пользователь модератором (права управлять определённым контентом)?
    # да если в поле роль указано 'moderator' или 'admin' (тк админ управляеи всем проектом,)
    # если в стандартных полях Django как is_staff и is_superuser значение True
    @property
    def is_moderator(self):
        """Является ли пользователь модератором (права управлять определённым
        контентом)?
        Да, если в поле role указано 'moderator' или 'admin' (тк админ
        управляеи всем проектом), если в стандартных полях Django как
        is_staff и is_superuser значение True.
        Модератор имеет те же права, что и зарегистрированный пользователь,
        а так же права на управление определённой частью контента проекта.
        """
        return (
            self.is_staff
            or self.is_superuser
            or self.role == 'admin'
            or self.role == 'moderator')

    # является ли пользователь пользователем?
    # да если в поле роль указано 'user' или
    # если в стандартных полях Django is_authenticated значение True.
    @property
    def is_user(self):
        """Является ли пользователь пользователем?
        Да, если в поле role указано 'user' или
        если в стандартных полях Django is_authenticated значение True.
        """
        return self.is_authenticated or self.role == 'user'

    def __str__(self):
        return f'Пользователь {self.username}.'
