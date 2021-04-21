from django.shortcuts import render

# Create your views here.
from accounts.forms import UserAccountForm


def user_creation(request):
    form = UserAccountForm
    context = {
        "form": form

    }
    return render(request, "user/user_creation.html", context)
