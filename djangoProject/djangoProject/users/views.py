from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCreationForm, ArticlesForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ArticlesForm
from .models import Articles
from django.views.generic import UpdateView, DetailView


class ArticlesView(DetailView):
    model = Articles
    template_name = 'details_articles.html'
    context_object_name = 'article'


class ArticlesUpdateView(UpdateView):
    model = Articles
    template_name = 'test.html'

    fields = ['title', 'date']


def achieve(request):
    achievements = Articles.objects.all()
    return render(request, 'test.html', {'achievements': achievements})


posts = [
    {
        'author': 'Администратор',
        'title': 'Это я, всем ку',
        'content': 'Тут я расскажу как круто играть в казино',
        'date_posted': '29 февраля, 2024'
    },

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Заполнено не верно'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'create.html', data)
