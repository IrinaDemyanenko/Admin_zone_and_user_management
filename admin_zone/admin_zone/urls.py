
from django.contrib import admin
from django.urls import path, include
# подключаем плагин для генерации документации
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

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
    # подключаем адреса приложения api
    path('api/v1/', include('api.urls', namespace='api')),
    # Генерация OpenAPI схемы
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI
    path('api/v1/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc
    path('api/v1/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
