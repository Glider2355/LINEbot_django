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


class Alert_Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name


class Pisto_Alert_Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name


class Alert_Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name


class Pisto_Alert_Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name


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
        verbose_name="アラート日"
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
        verbose_name="アラート文",
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


class User(AbstractUser):
    REQUIRED_FIELDS = []
