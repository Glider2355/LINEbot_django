from django.views.generic.edit import DeleteView, CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.http import redirect


class PistoView(TemplateView):
    template_name = "pisto.html"

# ListViewは一覧を簡単に作るためのView


class Blog(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    template_name = "blog/post_list.html"
    model = Post

# DetailViewは詳細を簡単に作るためのView


class Detail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    template_name = "blog/post_detail.html"
    model = Post

# CreateViewは新規作成画面を簡単に作るためのView


class Create(CreateView):
    template_name = "blog/post_form.html"
    model = Post

    # 編集対象にするフィールド
    fields = ["title", "body", "category", "tags"]


class Update(UpdateView):
    template_name = "blog/post_form.html"
    model = Post
    fields = ["title", "body", "category", "tags"]


class Delete(DeleteView):
    template_name = "blog/post_confirm_delete.html"
    model = Post

    # 削除したあとに移動する先（トップページ）
    success_url = "/blog/post_list"


class Login(TemplateView):
    template_name = "registration/index.html"


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        User = form.save()
        Login(self.request, User)
        self.object = User
        return redirect(self.get_success_url())


"""
# LINE_bot
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["ga3RTbFajryJHCJWQZGN8+it8YPgBMlqcDQnYhoOY9IGwW1NFoH4viAdEOTgE3VIn+ha9uYYnoNlBKuvTC6B7djAaU1dFgro9KhOsBi5D8BUcNfi0oX0uaSS+h7hkN51NtIoTsFWe85RwQjji6hQHQdB04t89/1O/w1cDnyilFU="]
YOUR_CHANNEL_SECRET = os.environ["090728578e63d4649fc2eac21a2e1e7e"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        HttpResponseForbidden()
    return HttpResponse('OK', status=200)


# オウム返し
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=event.message.text))
"""
