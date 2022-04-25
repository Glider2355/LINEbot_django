# 追加機能
部内会計に対して建て替え申請(経費申請)ができるようになりました。   
レシート画像はcloudinaryのクラウドに保存されます。

# 注意点
外部APIキーを含む.envファイルは公開していません。

# 動作確認環境
- テスト環境 \
※初回のアクセスは時間がかかります。
  - bot管理サイト: <https://test-line-bot-django.herokuapp.com/staff-admin/> 
  - ユーザーID: admin 
  - パスワード: editor 
 
    ![image](https://user-images.githubusercontent.com/62125008/120919073-b2dac880-c6f2-11eb-916c-9434404e3bf0.png)
  - LINEbotのQR(上記のQRからLINEで友達追加してください)

LINEbotの動作確認をする場合は以下のURLにアクセスすることでリマインダーの通知を流すことができます。

通知トリガーURL: <https://test-line-bot-django.herokuapp.com/callback/> 
