from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Language, ListTrainee


def detail(request, language_id):
    language = get_object_or_404(Language, pk=language_id)
    return render(request, 'training_polls/detail.html', {'language': language})


def index(request):
    language_list = Language.objects.order_by()
    context = {'language_list': language_list}
    return render(request, 'training_polls/index.html', context)


def get_delete(request, language_name):
    delete_element = ListTrainee.objects.filter(language=language_name)
    delete_element.delete()
    context = {'language_name': language_name}
    return render(request, 'training_polls/get_delete.html',  context)


def profile(request):
    user = request.user
    whole_list_language = ListTrainee.objects.all()
    list_language = whole_list_language.filter(name=user)
    context = {'list_language': list_language}
    return render(request, 'training_polls/profile.html', context)

def login_page(request):
    return render(request, 'training_polls/login_page.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return render(request, 'training_polls/index.html')
    else:
        form = UserRegisterForm()
    return render(request, 'training_polls/register.html', {'form': form})


def get_enter(request, language_id):
    language = get_object_or_404(Language, pk=language_id)
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('language'):
            trainee = ListTrainee()
            trainee.name = request.POST.get('name')
            trainee.language = request.POST.get('language')
            trainee.save()
            return render(request, 'training_polls/get_enter.html', {'language': language})
    else:
        return render(request, 'training_polls/get_enter.html', {'language': language})
