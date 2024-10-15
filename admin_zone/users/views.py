# Импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView
# Функция reverse_lazy позволяет получить URL по параметрам функции path()
from django.urls import reverse_lazy
# импортируем созданный нами класс формы CreationForm из users/forms.py
from users.forms import CreationForm
from django.shortcuts import render


class SignUp(CreateView):
    """Форма регистрации нового пользователя."""
    # Форма будет работать с созданным нами классом формы CreationForm
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную
    success_url = reverse_lazy('users:index')
    # users - пространство имён namespace
    # index - name из path
    template_name = 'users/signup.html'
    # имя шаблона, куда будет передана переменная form с объектом HTML-формы


def index(request):
    """Главная страница сайта."""
    context = {
        'title': 'Главная страница сайта',
    }
    return render(request, template_name='users/index.html', context=context)
