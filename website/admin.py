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


class Pisto_PostInline(PostInline):
    model = models.Pisto_Alert


class Alert_PostInline(PostInline):
    model = models.Alert


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [PostInline]


@admin.register(models.Pisto_Alert_Category)
class Pisto_CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Alert_Category)
class Alert_CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Alert_Tag)
class Alert_TagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Pisto_Alert_Tag)
class Pisto_TagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class PostAdminForm(forms.ModelForm):
    class Meta:
        labels = {
            'title': 'タイトル',
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


@admin.register(models.Alert)
class Alert_PostAdmin(PostAdmin):
    readonly_fields = ('id', )
    fieldsets = [
        (None, {'fields': ('title', )}),
        ('コンテンツ', {'fields': ('body', )}),
        ('分類', {'fields': ('category', 'tags')}),
        ('メタ', {'fields': ('published', 'schedule', 'alert_time')})
    ]
    list_display = ('id', 'title', 'category',
                    'tags_summary', 'published', 'schedule', 'alert_time')
    list_select_related = ('category', )
    list_editable = ('title', 'category', 'schedule', 'alert_time')
    search_fields = ('title', 'category__name',
                     'tags__name')
    list_filter = ('category', 'tags')
    ordering = ('schedule', )


@admin.register(models.Pisto_Alert)
class Pisto_PostAdmin(Alert_PostAdmin):
    fieldsets = [
        (None, {'fields': ('title', )}),
        ('コンテンツ', {'fields': ('body', )}),
        ('分類', {'fields': ('category', 'tags')}),
        ('メタ', {'fields': ('published', 'schedule1', 'schedule2', 'alert_time')})
    ]
    list_display = ('id', 'title', 'category',
                    'tags_summary', 'published', 'schedule1', 'schedule2', 'alert_time')
    list_select_related = ('category', )
    list_editable = ('title', 'category', 'schedule1',
                     'schedule2', 'alert_time')
    search_fields = ('title', 'category__name',
                     'tags__name')
    list_filter = ('category', 'tags')
    ordering = ('schedule1', )


class BlogAdminSite(AdminSite):
    site_header = 'マイページ'
    site_title = 'マイページ'
    index_title = 'ホーム'
    login_form = AuthenticationForm

    def has_permission(self, request):
        return request.user.is_active


mypage_site = BlogAdminSite(name="mypage")
@admin.register(models.Post, site=mypage_site)
class PMyAdmin(PostAdmin):
    pass


@admin.register(models.Tag, site=mypage_site)
class TMyAdmin(TagAdmin):
    pass


@admin.register(models.Category, site=mypage_site)
class CMyAdmin(CategoryAdmin):
    pass


@admin.register(models.Alert, site=mypage_site)
class APMyAdmin(Alert_PostAdmin):
    pass


@admin.register(models.Alert_Category, site=mypage_site)
class ACMyAdmin(Alert_CategoryAdmin):
    pass


@admin.register(models.Alert_Tag, site=mypage_site)
class ATMyAdmin(Alert_TagAdmin):
    pass


@admin.register(models.Pisto_Alert, site=mypage_site)
class PPMyAdmin(Pisto_PostAdmin):
    pass


@admin.register(models.Pisto_Alert_Category, site=mypage_site)
class PCMyAdmin(Pisto_CategoryAdmin):
    pass


@admin.register(models.Pisto_Alert_Tag, site=mypage_site)
class PTMyAdmin(Pisto_TagAdmin):
    pass
