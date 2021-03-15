from django.urls import path

from . import views

from django.contrib.auth.decorators import login_required
from .admin import mypage_site
from django.contrib import admin

urlpatterns = [
    path('', login_required(views.index.as_view()), name="index"),
    path("signup/", login_required(views.SignUpView.as_view()), name="signup"),
    path('mypage/', mypage_site.urls),
    path('staff-admin/', admin.site.urls),
    path('callback/', views.callback, name='callback'),
]

"""
    path('gassyuku/post_list/', login_required(views.Pisto.as_view()), name="pisto"),
    path('alert/post_list/',
         login_required(views.Alert_View.as_view()), name="alert"),
    path('blog/post_list/',
         login_required(views.Blog.as_view()), name="blog"),


    path('detail/<pk>/',
         login_required(views.Detail.as_view()), name="detail"),
    path('alert_detail/<pk>/',
         login_required(views.Alert_Detail.as_view()), name="alert_detail"),
    path('gassyuku_detail/<pk>/',
         login_required(views.Pisto_Detail.as_view()), name="gassyuku_detail"),



    path('create/', login_required(views.Create.as_view()), name="create"),
    path('alert_create/', login_required(views.Alert_Create.as_view()),
         name="alert_create"),
    path('gassyuku_create/', login_required(views.Pisto_Create.as_view()),
         name="gassyuku_create"),


    path('update/<pk>', login_required(views.Update.as_view()), name="update"),
    path('alert_update/<pk>',
         login_required(views.Alert_Update.as_view()), name="alert_update"),
    path('gassyuku_update/<pk>',
         login_required(views.Pisto_Update.as_view()), name="gassyuku_update"),


    path('delete/<pk>', login_required(views.Delete.as_view()), name="delete"),
    path('alert_delete/<pk>',
         login_required(views.Alert_Delete.as_view()), name="alert_delete"),
    path('gassyuku_delete/<pk>',
         login_required(views.Pisto_Delete.as_view()), name="gassyuku_delete"),
     """
