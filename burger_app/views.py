from django.shortcuts import render, redirect
from .models import Burger, Ingredient
from .forms import BurgerForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordResetForm, CustomSetPasswordForm

def burger_list(request):
    burgers = Burger.objects.all()
    ingredients = Ingredient.objects.all()
    return render(request, 'burger_app/burger_list.html', {'burgers': burgers, 'ingredients': ingredients})


def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'burger_app/ingredient_list.html', {'ingredients': ingredients})


def create_burger(request):
    if request.method == 'POST':
        form = BurgerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('burger_list')
    else:
        form = BurgerForm()

    return render(request, 'burger_app/create_burger.html', {'form': form})



class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm

class CustomLogoutView(LogoutView):
    pass

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    form_class = CustomPasswordResetForm

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    form_class = CustomSetPasswordForm

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'

class CustomSignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')