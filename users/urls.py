from .views import SignUpView, CustomLoginView
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
