from users.models import User
from rest_framework import serializers


class UserGetUpdateDeleteSerializer(serializers.ModelSerializer):
    """Сериализатор для редактирования пользователем своей
    существующей записи модели User.
    """

    class Meta:
        # сериализатор будет работать с моделью User
        model = User
        # сериализатор будет работать с полями из модели User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        read_only_fields = ['id', ]


class UserCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания новых записей (пользователей)
    администратором в модели User.
    """

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username',
            'email', 'password', 'role'
            ]

    # def validate(self, data):
    #     """Проверяем, что при регистрации в поле username
    #     не будет использованно зарезервированное имя me.
    #     """
    #     if data.get['username'] != 'me':
    #         return data
    #     return serializers.ValidationError(
    #         'Имя me зарезервировано. Выберите другое имя пользователя (username).'
    #         )
