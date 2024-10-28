from django.urls import include, path
from api.views import APIGenericUserDetail, APIGenericUserCreate, UserViewSet
from rest_framework import routers


app_name = 'api'  # пространство имён namespace

router_v1 = routers.DefaultRouter()

router_v1.register(r'users', UserViewSet, basename='api_users')

urlpatterns = [
    #path('', include(router_v1.urls)),
    # в перфиксе роутера тоже есть users, значит это имя повторно использовать не можем
    path('all-users/', APIGenericUserCreate.as_view(), name='api_user_create'),
    path('all-users/<str:username>/', APIGenericUserDetail.as_view(), name='api_user_detail'),
    path('', include(router_v1.urls)),
    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),
    #path('', ),
]

# Список всех эндпоинтов, которые создаёт djoser, есть в документации.

# Available endpoints¶
# •	/users/
# •	/users/me/
# •	/users/confirm/
# •	/users/resend_activation/
# •	/users/set_password/
# •	/users/reset_password/
# •	/users/reset_password_confirm/
# •	/users/set_username/
# •	/users/reset_username/
# •	/users/reset_username_confirm/
# •	/token/login/ (Token Based Authentication)
# •	/token/logout/ (Token Based Authentication)
# •	/jwt/create/ (JSON Web Token Authentication)
# •	/jwt/refresh/ (JSON Web Token Authentication)
# •	/jwt/verify/ (JSON Web Token Authentication)
