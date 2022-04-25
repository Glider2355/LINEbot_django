from django.db import models
from django.urls import reverse_lazy


class Receipt_Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '建て替え人登録'
        verbose_name_plural = '建て替え人登録'


class Receipt_Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '建て替えレシートタグ'
        verbose_name_plural = '建て替えレシートタグ'


class Receipt_data(models.Model):
    receipt = models.ImageField(upload_to="images", verbose_name="レシート", null=False, blank=False)

    date = models.DateTimeField(
        auto_now_add=False,
        editable=True,
        blank=False,
        null=False,
        verbose_name="建て替え日"
    )

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="タイトル"
    )

    body = models.TextField(
        blank=True,
        null=True,
        verbose_name="備考",
        help_text="HTMLタグは使えません。"
    )

    category = models.ForeignKey(
        Receipt_Category,
        on_delete=models.CASCADE,
        verbose_name="建て替え人"
    )

    price = models.IntegerField(
        verbose_name='金額',
        blank=False,
        null=False,
        default=0
    )

    tags = models.ManyToManyField(
        Receipt_Tag,
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
        return reverse_lazy("receipt", args=[self.id])

    class Meta:
        verbose_name = '建て替えレシート登録'
        verbose_name_plural = '建て替えレシート登録'

