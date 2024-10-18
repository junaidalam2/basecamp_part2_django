from django.contrib.auth.views import LoginView
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login, get_user_model, update_session_auth_hash
from django.views.generic import FormView, ListView, DetailView, UpdateView
from .forms import SignUpForm, AdminUpdateForm, UpdateForm

User = get_user_model()


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class SignUpView(FormView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Save the user and log them in
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())


class AdminUserListView(ListView):
    model = User
    template_name = 'registration/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()


class AdminUserDetailView(DetailView):
    template_name = 'registration/user_detail.html'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()

        return context


class AdminUpdateView(UpdateView):
    model = User
    template_name = 'registration/user_admin_update.html'
    form_class = AdminUpdateForm
    success_url = reverse_lazy('users:user-list')

    def form_valid(self, form):
        user = form.save
        return super().form_valid(form)  


class UserUpdateView(UpdateView):
    model = User
    template_name = 'registration/user_update.html'
    form_class = UpdateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)

        if form.has_changed(): 
            if form.cleaned_data.get('password1'):
                user.set_password(form.cleaned_data['password1'])
                update_session_auth_hash(self.request, user)
        
        user.save()
        return redirect(self.get_success_url())