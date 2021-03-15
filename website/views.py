from django.views.generic.edit import DeleteView, CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post, Alert, Pisto_Alert
from django.urls import reverse_lazy
from .forms import SignUpForm

import datetime

from linebot import LineBotApi
from linebot.models import TextSendMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


class PistoView(TemplateView):
    template_name = "pisto.html"

# ListViewは一覧を簡単に作るためのView


class Blog(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    template_name = "blog/post_list.html"
    model = Post


class Alert_View(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    template_name = "alert/post_list.html"
    model = Alert


class Pisto(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    template_name = "gassyuku/post_list.html"
    model = Pisto_Alert


# DetailViewは詳細を簡単に作るためのView


class Detail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    template_name = "blog/post_detail.html"
    model = Post


class Alert_Detail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    template_name = "alert/post_detail.html"
    model = Alert


class Pisto_Detail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    template_name = "gassyuku/post_detail.html"
    model = Pisto_Alert


# CreateViewは新規作成画面を簡単に作るためのView


class Create(CreateView):
    template_name = "blog/post_form.html"
    model = Post

    # 編集対象にするフィールド
    fields = ["title", "body", "category", "tags"]


class Alert_Create(CreateView):
    template_name = "alert/post_form.html"
    model = Alert

    # 編集対象にするフィールド
    fields = ["title", "schedule", "alert_time", "body", "category", "tags"]


class Pisto_Create(CreateView):
    template_name = "gassyuku/post_form.html"
    model = Pisto_Alert

    # 編集対象にするフィールド
    fields = ["title", "schedule1", "schedule2",
              "alert_time", "body", "category"]


class Update(UpdateView):
    template_name = "blog/post_form.html"
    model = Post
    fields = ["title", "body", "category", "tags"]


class Alert_Update(UpdateView):
    template_name = "alert/post_form.html"
    model = Alert
    fields = ["title", "schedule", "alert_time", "body", "category", "tags"]


class Pisto_Update(UpdateView):
    template_name = "gassyuku/post_form.html"
    model = Pisto_Alert
    fields = ["title", "schedule1", "schedule2",
              "alert_time", "body", "category"]


class Delete(DeleteView):
    template_name = "blog/post_confirm_delete.html"
    model = Post

    # 削除したあとに移動する先（トップページ）
    success_url = "/blog/post_list"


class Alert_Delete(DeleteView):
    template_name = "alert/post_confirm_delete.html"
    model = Alert

    # 削除したあとに移動する先（トップページ）
    success_url = "/alert/post_list"


class Pisto_Delete(DeleteView):
    template_name = "gassyuku/post_confirm_delete.html"
    model = Pisto_Alert

    # 削除したあとに移動する先（トップページ）
    success_url = "/gassyuku/post_list"


class index(TemplateView):
    template_name = "registration/index.html"


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


# LINE_bot

@csrf_exempt
def callback(request):

    YOUR_CHANNEL_ACCESS_TOKEN = "ga3RTbFajryJHCJWQZGN8+it8YPgBMlqcDQnYhoOY9IGwW1NFoH4viAdEOTgE3VIn+ha9uYYnoNlBKuvTC6B7djAaU1dFgro9KhOsBi5D8BUcNfi0oX0uaSS+h7hkN51NtIoTsFWe85RwQjji6hQHQdB04t89/1O/w1cDnyilFU="
    groupid = 'Cb6b3f7abfc4ce53eb1aeccb7412db99b'
    line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)

    class today:
        dt_now = datetime.datetime.now()
        year = dt_now.year
        month = dt_now.month
        day = dt_now.day

    check = Alert.objects.filter(alert_time__year=today.year).filter(
        alert_time__month=today.month).filter(alert_time__day=today.day)
    check2 = Pisto_Alert.objects.filter(
        alert_time__month=today.month).filter(alert_time__day=today.day)

    oono = check2.filter(category__name="大野")
    kisogawa = check2.filter(category__name="木曽川")
    fukui = check2.filter(category__name="福井")

    k_must_list = '''
やる事リスト
•Googleカレンダー作成
•出入り表作成
•ドライブに合宿フォルダを作る
•教官WTマン依頼
•教官依頼状添え状作成
•訓練届、参加者一覧、陸送届、機体借用願を提出(学連)
•メーリスを流す
•まごころにFAX(3日前までに)'''

    o_must_list = '''
やる事リスト
•Googleカレンダー作成
•出入り表作成
•ドライブに合宿フォルダを作る
•教官WTマン依頼
•教官依頼状添え状作成
•訓練届(OGCと東海関西)、参加者一覧(東海関西)、陸送届(学連)、に提出
•OGC参加表明確認
•メーリスを流す'''

    f_must_list = '''
やる事リスト
•Googleカレンダー作成
•出入り表作成
•ドライブに合宿フォルダを作る
•教官WTマン依頼
•教官依頼状添え状作成
•訓練届(東海関西)、参加者一覧(東海関西)、陸送届(学連)、に提出
•機体借用願(256→同志社、557→大工)に提出
•メーリスを流す
•はるせんに電話(前日までに)'''

    for massage in check:
        massages = TextSendMessage(
            text="タイトル:" + massage.title + "\n" + "実施日:" + massage.schedule.strftime('%m/%d') + "\n" + massage.body)
        line_bot_api.push_message(groupid, massages)

    for massage in oono:
        massages = TextSendMessage(text="合宿名:" + massage.title + "\n" + "実施日:" + massage.schedule1.strftime(
            '%m/%d') + "(集合日)～" + massage.schedule2.strftime('%m/%d') + "\n" + massage.body + "\n" + o_must_list)
        line_bot_api.push_message(groupid, massages)

    for massage in kisogawa:
        massages = TextSendMessage(text="合宿名:" + massage.title + "\n" + "実施日:" + massage.schedule1.strftime(
            '%m/%d') + "(集合日)～" + massage.schedule2.strftime('%m/%d') + "\n" + massage.body + "\n" + k_must_list)
        line_bot_api.push_message(groupid, massages)

    for massage in fukui:
        massages = TextSendMessage(text="合宿名:" + massage.title + "\n" + "実施日:" + massage.schedule1.strftime(
            '%m/%d') + "(集合日)～" + massage.schedule2.strftime('%m/%d') + "\n" + massage.body + "\n" + f_must_list)
        line_bot_api.push_message(groupid, massages)

    """
    if(today.month == 1 and today.day == 15):
        Alert.objects.filter(schedule__year=today.year - 1).filter(
            schedule__month=12).delete()

    elif(today.day == 15):
        Alert.objects.filter(schedule__year=today.year).filter(
            schedule__month=today.month - 1).delete()
    """

    return HttpResponse("Hello heroku")
