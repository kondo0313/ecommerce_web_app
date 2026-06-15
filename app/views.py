from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserSignupForm
from django.shortcuts import render, redirect
from .models import AccountUser
from django.contrib.auth.hashers import check_password
from .forms import UserLoginForm
from .forms import UserSignupForm


def index(request):
    user_id = request.session.get("user_id")

    user = None
    if user_id:
        user = AccountUser.objects.filter(user_id=user_id).first()

    return render(request, "app/main.html", {"user": user})

def admin_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "app/accounts/admin_register.html", {"form": form})

def user_register(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            return render(
                request,
                "app/accounts/user_confirm.html",
                {"data": form.cleaned_data}
            )
    else:
        form = UserSignupForm()

    return render(request, "app/accounts/user_register.html", {"form": form})

def user_register_commit(request):
    if request.method == "POST":
        AccountUser.objects.create(
            user_id=request.POST.get("user_id"),
            password=request.POST.get("password"),
            name=request.POST.get("name"),
            address=request.POST.get("address"),
        )

        #print("いま入ってるデータベースだよん", AccountUser.objects.all())

        return render(
            request,
            "app/accounts/user_register_commit.html",
            {"name": request.POST.get("name")}
        )

def user_login(request):
    form = UserLoginForm(request.POST)
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")

        user = AccountUser.objects.filter(user_id=user_id).first()

        #print("全部だよん", AccountUser.objects.all())

        if user:
            if user_id == user.user_id and password == user.password:
                request.session["user_id"] = user.user_id
                #print(":D")
                return redirect("index")

        return render(
            request,
            "app/accounts/user_login.html",
            {"form": form}
        )

    return render(request, "app/accounts/user_login.html", {"form": form})

def user_info(request):
    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("user_login")
    
    user = AccountUser.objects.filter(user_id=user_id).first()
    #print(user)

    return render(request, "app/accounts/user_info.html", {"user": user})

def user_update(request):
    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("user_login")

    user = AccountUser.objects.filter(user_id=user_id).first()

    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            return render(
                request,
                "app/accounts/user_update_confirm.html",
                {"data": form.cleaned_data}
            )
    else:
        form = UserSignupForm(initial={
            "user_id": user.user_id,
            "password": user.password,
            "password": user.password,  # confirm用
            "name": user.name,
            "address": user.address,
        })

    return render(request, "app/accounts/user_update.html", {
        "form": form
    })

def user_update_commit(request):
    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("user_login")

    user = AccountUser.objects.filter(user_id=user_id).first()

    if request.method == "POST" and user:
        user.password = request.POST.get("password")
        user.name = request.POST.get("name")
        user.address = request.POST.get("address")
        user.save()

    return render(
        request,
        "app/accounts/user_update_commit.html",
        {"data": user}
    )

def withdraw_confirm(request):
    user_id = request.session.get("user_id")

    user = AccountUser.objects.filter(user_id=user_id).first()

    return render(
        request,
        "app/accounts/withdraw_confirm.html",
        {"name": user.name}
    )

def withdraw_commit(request):
    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("user_login")

    user = AccountUser.objects.filter(user_id=user_id).first()

    if request.method == "POST" and user:
        user.delete()                  # ← 退会（削除）

    return render(request, "app/accounts/withdraw_commit.html", {"name": user.name})

def serch_result(request):
    return render(request, "shop/serch_result.html")


