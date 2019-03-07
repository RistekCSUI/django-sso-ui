from django.urls import path
from django.http import HttpResponse
from django_sso_ui.decorators import with_sso_login
import json


@with_sso_login(force_login=True)
def login(request, sso_profile):
    return HttpResponse(json.dumps(sso_profile))


urlpatterns = [path("login/", login)]
