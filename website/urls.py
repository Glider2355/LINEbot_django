from django.urls import path

from . import views

from django.contrib.auth.decorators import login_required
from .admin import mypage_site
from django.contrib import admin

urlpatterns = [
    path('', login_required(views.Login.as_view()), name="login"),
    path('pisto/', login_required(views.PistoView.as_view())),
    path('blog/post_list/',
         login_required(views.Blog.as_view()), name="blog"),
    path('detail/<pk>/',
         login_required(views.Detail.as_view()), name="detail"),
    path('create/', login_required(views.Create.as_view()), name="create"),
    path('update/<pk>', login_required(views.Update.as_view()), name="update"),
    path('delete/<pk>', login_required(views.Delete.as_view()), name="delete"),
    path("signup/", login_required(views.SignUpView.as_view()), name="signup"),
    path('activate/<uidb64>/<token>/',
         views.ActivateView.as_view(), name='activate'),
    path('mypage/', mypage_site.urls),
    path('staff-admin/', admin.site.urls),
    # path('callback/', views.callback, name='callback'),
]
