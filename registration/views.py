from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
# from django.shortcuts import render, redirect, HttpResponseRedirect
# from .forms import UserForm, UserRegistrationForm


# def login_view(request):
#     title = "Login"
#     form = UserForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         next = request.POST.get("next", 'cafeteria/')
#         return HttpResponseRedirect(next)
#     return render(request, "registration/login_page.html", {"form": form, "title": title})
#
#
# def register_view(request):
#     title = "Register"
#     form = UserRegistrationForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         password = form.cleaned_data.get('password')
#         user.set_password(password)
#         user.save()
#         new_user = authenticate(username=user.username, password=password)
#         login(request, new_user)
#         return redirect("menu:detail")
#
#     context = {
#         "form": form,
#         "title": title,
#     }
#     return render(request, "registration/login_page.html", context)
#
#
# def logout_view(request):
#     logout(request)
#     return redirect("menu:detail")

from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, SignUpForm
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/cafeteria')
        else:
            form=SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
