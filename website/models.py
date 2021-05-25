from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '資料庫カテゴリー'
        verbose_name_plural = '資料庫カテゴリー'


class Alert_Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'リマインダーカテゴリー'
        verbose_name_plural = 'リマインダーカテゴリー'


class Pisto_Alert_Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '合宿リマインダーカテゴリー'
        verbose_name_plural = '合宿リマインダーカテゴリー'


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '資料庫タグ'
        verbose_name_plural = '資料庫タグ'


class Alert_Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'リマインダータグ'
        verbose_name_plural = 'リマインダータグ'


class Pisto_Alert_Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '合宿リマインダータグ'
        verbose_name_plural = '合宿リマインダータグ'


class Post(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False,
        verbose_name="作成日"
    )

    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False,
        verbose_name="最終更新日"
    )

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="タイトル"
    )

    body = models.TextField(
        blank=True,
        null=False,
        verbose_name="本文",
        help_text="HTMLタグは使えません。"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="カテゴリ"
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name="タグ"
    )

    published = models.BooleanField(
        default=True,
        verbose_name="公開する"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])

    class Meta:
        verbose_name = '資料庫'
        verbose_name_plural = '資料庫'


class Alert(models.Model):
    schedule = models.DateTimeField(
        auto_now_add=False,
        editable=True,
        blank=False,
        null=False,
        verbose_name="予定日"
    )

    alert_time = models.DateTimeField(
        auto_now=False,
        editable=True,
        blank=False,
        null=False,
        verbose_name="リマインダー日"
    )

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="タイトル"
    )

    body = models.TextField(
        blank=True,
        null=False,
        verbose_name="リマインダー文",
        help_text="HTMLタグは使えません。"
    )

    category = models.ForeignKey(
        Alert_Category,
        on_delete=models.CASCADE,
        verbose_name="カテゴリ"
    )

    tags = models.ManyToManyField(
        Alert_Tag,
        blank=True,
        verbose_name="タグ"
    )

    published = models.BooleanField(
        default=True,
        verbose_name="公開する"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("alert", args=[self.id])

    class Meta:
        verbose_name = 'リマインダー設定'
        verbose_name_plural = 'リマインダー設定'


class Pisto_Alert(models.Model):
    schedule1 = models.DateTimeField(
        auto_now_add=False,
        editable=True,
        blank=False,
        null=False,
        verbose_name="集合日"
    )

    schedule2 = models.DateTimeField(
        auto_now_add=False,
        editable=True,
        blank=False,
        null=False,
        verbose_name="最終日"
    )

    alert_time = models.DateTimeField(
        auto_now=False,
        editable=True,
        blank=False,
        null=False,
        verbose_name="アラート日"
    )

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="合宿名"
    )

    body = models.TextField(
        blank=True,
        null=False,
        verbose_name="アラート文",
        help_text="HTMLタグは使えません。"
    )

    category = models.ForeignKey(
        Pisto_Alert_Category,
        on_delete=models.CASCADE,
        verbose_name="合宿場所"
    )

    tags = models.ManyToManyField(
        Alert_Tag,
        blank=True,
        verbose_name="タグ"
    )

    published = models.BooleanField(
        default=True,
        verbose_name="公開する"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("gassyuku", args=[self.id])

    class Meta:
        verbose_name = '合宿リマインダー設定'
        verbose_name_plural = '合宿リマインダー設定'


class User(AbstractUser):
    REQUIRED_FIELDS = []
