from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView, CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView, CustomSignUpView

urlpatterns = [
    path('burgers/', views.burger_list, name='burger_list'),
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('create/', views.create_burger, name='create_burger'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('signup/', CustomSignUpView.as_view(), name='signup'),
]
