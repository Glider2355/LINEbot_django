from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin import AdminSite

admin.site.register(User, UserAdmin)


class PostInline(admin.TabularInline):
    model = models.Post
    fields = ('title', 'body')
    extra = 1


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [PostInline]


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class PostAdminForm(forms.ModelForm):
    class Meta:
        labels = {
            'title': 'ブログタイトル',
        }


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    readonly_fields = ('created', 'updated')
    fieldsets = [
        (None, {'fields': ('title', )}),
        ('コンテンツ', {'fields': ('body', )}),
        ('分類', {'fields': ('category', 'tags')}),
        ('メタ', {'fields': ('published', 'created', 'updated')})
    ]

    form = PostAdminForm
    filter_horizontal = ('tags',)

    list_display = ('id', 'title', 'category',
                    'tags_summary', 'published', 'created', 'updated')
    list_select_related = ('category', )
    list_editable = ('title', 'category')
    search_fields = ('title', 'category__name',
                     'tags__name', 'created', 'updated')
    ordering = ('-updated', '-created')
    list_filter = ('category', 'tags', 'created', 'updated')

    def tags_summary(self, obj):
        qs = obj.tags.all()
        label = ', '.join(map(str, qs))
        return label

    tags_summary.short_description = "tags"

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    actions = ["publish", "unpublish"]

    def publish(self, request, queryset):
        queryset.update(published=True)

    publish.short_description = "公開する"

    def unpublish(self, request, queryset):
        queryset.update(published=False)

    unpublish.short_description = "下書きに戻す"


class BlogAdminSite(AdminSite):
    site_header = 'マイページ'
    site_title = 'マイページ'
    index_title = 'ホーム'
    login_form = AuthenticationForm

    def has_permission(self, request):
        return request.user.is_active


mypage_site = BlogAdminSite(name="mypage")

mypage_site.register(models.Post)
mypage_site.register(models.Tag)
mypage_site.register(models.Category)
