from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.contrib.auth import login, authenticate
from .forms import (
    CustomUserCreationForm,
    UserUpdateForm,
)  # Modificado
from django.contrib.auth import get_user_model
from django.views.generic import (
    DetailView,
    UpdateView,
)  # Modificado
from django.urls import reverse  # Añadido

User = get_user_model()

# Omitido
class UserUpdate(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'accounts/user_edit.html'

    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.kwargs['pk']})
# Aquí termina

class UserCreateAndLoginView(CreateView):
    form_class = CustomUserCreationForm  # Modificado
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("tasks:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        raw_pw = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=raw_pw)
        login(self.request, user)
        return response

# Aquí comienza
class UserDetail(DetailView):
    model = User
    template_name = 'accounts/user_detail.html'
# Aquí termina

# Omitido
from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView)  # Añadido

# Omitido
class PasswordChange(PasswordChangeView):
    template_name = 'accounts/password_change.html'

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/user_detail.html'

class UserDelete(DeleteView):
    model = User
    template_name = 'accounts/user_delete.html'
    success_url = reverse_lazy('login')
