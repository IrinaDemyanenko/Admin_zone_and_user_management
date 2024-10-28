from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Функция get_user_model() обращается именно к той модели,
# которая зарегистрирована в качестве основной модели пользователей
# в конфиге проекта.
