from django.contrib import admin
from django.urls import path, include

admin.site.site_title = '内部管理サイト'
admin.site.site_header = '内部管理サイト'
admin.site.index_title = 'メニュー'
# admin.site.unregister(Group)


urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('', include("reminder.urls")),
]
