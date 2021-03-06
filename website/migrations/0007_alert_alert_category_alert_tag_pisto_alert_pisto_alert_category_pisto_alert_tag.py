# Generated by Django 3.0.5 on 2021-02-27 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20210222_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alert_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pisto_Alert_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pisto_Alert_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pisto_Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule1', models.DateTimeField(verbose_name='集合日')),
                ('schedule2', models.DateTimeField(verbose_name='最終日')),
                ('alert_time', models.DateTimeField(verbose_name='アラート日')),
                ('title', models.CharField(max_length=255, verbose_name='合宿名')),
                ('body', models.TextField(blank=True, help_text='HTMLタグは使えません。', verbose_name='アラート文')),
                ('published', models.BooleanField(default=True, verbose_name='公開する')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Pisto_Alert_Category', verbose_name='合宿場所')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.DateTimeField(verbose_name='予定日')),
                ('alert_time', models.DateTimeField(verbose_name='アラート日')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('body', models.TextField(blank=True, help_text='HTMLタグは使えません。', verbose_name='アラート文')),
                ('published', models.BooleanField(default=True, verbose_name='公開する')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Alert_Category', verbose_name='カテゴリ')),
                ('tags', models.ManyToManyField(blank=True, to='website.Alert_Tag', verbose_name='タグ')),
            ],
        ),
    ]
