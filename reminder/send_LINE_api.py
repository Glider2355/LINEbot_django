import datetime

from linebot import LineBotApi
from linebot.models import TextSendMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import Alert
from g_reminder.models import Pisto_Alert

import os
import environ

env = environ.Env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env.read_env((os.path.join(BASE_DIR, '.env')))


@csrf_exempt
def callback(request):

    # アクセストークンの設定
    YOUR_CHANNEL_ACCESS_TOKEN = env('YOUR_CHANNEL_ACCESS_TOKEN')
    line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)

    # 今日の日付
    class today:
        dt_now = datetime.datetime.now()
        year = dt_now.year
        month = dt_now.month
        day = dt_now.day

    # リマインダーの通知チェック
    check = Alert.objects.filter(alert_time__year=today.year).filter(
        alert_time__month=today.month).filter(alert_time__day=today.day)

    # 合宿リマインダーの通知チェック
    check2 = Pisto_Alert.objects.filter(
        alert_time__month=today.month).filter(alert_time__day=today.day)

    oono = check2.filter(category__name="大野")
    kisogawa = check2.filter(category__name="木曽川")
    fukui = check2.filter(category__name="福井")

    # 木曽川やることリスト
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

    # 大野やることリスト
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

    # 福井空港やることリスト
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

    # メッセージ送信処理
    for massage in check:
        massages = TextSendMessage(
            text="タイトル:" + massage.title + "\n" + "実施日:" + massage.schedule.strftime('%m/%d') + "\n" + massage.body)
        line_bot_api.broadcast(massages)

    for massage in oono:
        massages = TextSendMessage(text="合宿名:" + massage.title + "\n" + "実施日:" + massage.schedule1.strftime(
            '%m/%d') + "(集合日)～" + massage.schedule2.strftime('%m/%d') + "\n" + massage.body + "\n" + o_must_list)
        line_bot_api.broadcast(massages)

    for massage in kisogawa:
        massages = TextSendMessage(text="合宿名:" + massage.title + "\n" + "実施日:" + massage.schedule1.strftime(
            '%m/%d') + "(集合日)～" + massage.schedule2.strftime('%m/%d') + "\n" + massage.body + "\n" + k_must_list)
        line_bot_api.broadcast(massages)

    for massage in fukui:
        massages = TextSendMessage(text="合宿名:" + massage.title + "\n" + "実施日:" + massage.schedule1.strftime(
            '%m/%d') + "(集合日)～" + massage.schedule2.strftime('%m/%d') + "\n" + massage.body + "\n" + f_must_list)
        line_bot_api.broadcast(massages)

    return HttpResponse("Hello heroku")
