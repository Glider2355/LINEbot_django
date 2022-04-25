from django.urls import path

from . import views, send_LINE_api

from django.contrib.auth.decorators import login_required
from .admin import mypage_site
from django.contrib import admin

urlpatterns = [
    path('', login_required(views.index.as_view()), name="index"),
    path("signup/", login_required(views.SignUpView.as_view()), name="signup"),
    path('mypage/', mypage_site.urls),
    path('staff-admin/', admin.site.urls),
    path('callback/', send_LINE_api.callback, name='callback'),
]
