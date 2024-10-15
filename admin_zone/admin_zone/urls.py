
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # подключение регистр и авторизации из приложения users
    # Django проверяет url-адреса сверху вниз,
    # нам нужно, чтобы Django сначала проверял адреса в приложении users
    path('auth/', include('users.urls', namespace='users')),
    # path('api/v1/', include('api.urls', namespace='api')),
    path('admin/', admin.site.urls),
    # подключение регистр и авторизации из приложения django.contrib.auth.
    # Все адреса с префиксом /auth
    # будут прернаправлены в модуль django.contrib.auth
    # Если какой-то URL не обнаружится в приложении users —
    # Django пойдёт искать его в django.contrib.auth
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('users.urls', namespace='users')),
]
