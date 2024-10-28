from django.shortcuts import render
from rest_framework import viewsets
from users.models import User
from api.serializers import UserGetUpdateDeleteSerializer, UserCreateSerializer
from api.permissions import IsUserObject, IsUser, IsAdmin
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import JsonResponse
from rest_framework import status


class APIGenericUserDetail(RetrieveUpdateDestroyAPIView):
    """Этот набор представлений работает с моделью User.
    Его работа — возвращать, обновлять или удалять объекты модели по одному.
    Редактировать свою запись сможет только её создатель.
    api/v1/all-users/<str:username>/.
    """

    serializer_class = UserGetUpdateDeleteSerializer
    permission_classes = [IsUserObject, ]
    lookup_field = 'username'

    def get_queryset(self):
        """Будет возвращать один объект модели User - текущего
        зарегистрированного пользователя.
        """
        user = self.request.user
        return User.objects.filter(pk=user.id)

class APIGenericUserCreate(CreateAPIView):
    """Будет создавать нового пользователя.
    Этот адрес доступен только администратору сайта - user.is_staff is True.
    api/v1/all-users/.
    """

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAdmin, ]  # IsAdminUser,


class UserViewSet(viewsets.ModelViewSet):
    """Набор представлений, работающий с моделью User.
    Работает с адресами:
    users/ - доступен только админу;
    users/<int:pk>/ - доступен только админу;
    users/me/ - доступен только зарегистрированным пользователям;
    """
    queryset = User.objects.all()
    serializer_class = UserGetUpdateDeleteSerializer
    permission_classes = [IsAdmin, ]

    #detail=False - чтобы в адресе не было /<int:pk>/, а чтобы
    # получить конкретный объект, отфильтруем quieryset
    # 'get', 'patch' - чтобы пользователь мог только прочитать
    # и отредактировать запись, но не удалить или изменить целиком
    # IsUserObject отредактировать запись по этому адресу сможет только
    # её владелец
    @action(
       detail=False, methods=['get', 'patch'],
       permission_classes=[IsUserObject, ]
    )
    def me(self, request):
        """По адресу users/me/ зарегистрированный пользователь
        сможет прочитать и отредактировать свою запись в моделе User.
        """

        user_id = request.user.id
        #user_queryset = User.objects.filter(id=user_id)
        user_queryset = User.objects.get(id=user_id)

        if request.method == 'GET':
            serializer = self.get_serializer(user_queryset)
            return Response(serializer.data)

        if request.method == 'PATCH':
            # Update `user_queryset` with partial data
            # в запросе получили информацию
            data = request.data
            # частично изменяем объект user_queryset полученной в запросе инф
            serializer = self.get_serializer(user_queryset, data=data, partial=True)
            # проверка с помощью метода is_valid
            # Если данные не будут соответствовать схеме, описанной внутри
            # UserCreateSerializer, то вызов метода
            # is_valid(raise_exception=True)
            # приведёт к исключению ValidationError
            if serializer.is_valid():
            # преобразуем и сохраняем данные с помощью встроенного
            # метода perform_update
                self.perform_update(serializer)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
