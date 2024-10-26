from users.views import (
    SignUpView, 
    CustomLoginView, 
    AdminUserListView,
    AdminUserDetailView,
    AdminUpdateView,
    UserUpdateView,
    UserDeleteView,
)
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('', AdminUserListView.as_view(), name='user-list'),
    path('<int:pk>/', AdminUserDetailView.as_view(), name='user-detail'),
    path('admin/<int:pk>/', AdminUpdateView.as_view(), name='user-admin-update'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),

]
