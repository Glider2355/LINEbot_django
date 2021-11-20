# 航空部LINEリマインダーBot

## 今までの課題

![image](https://user-images.githubusercontent.com/62125008/142735229-e6dd4fc9-0dd4-4110-951c-d8b507ac4a6a.png)

航空部ではやるべきタスクが多く、タスク漏れが往々にしてあります。  
例えば、航空無線通信士や自家用操縦士試験の申し込み(年にそれぞれ数回)、部車(二台)の車検や保険の更新、保有機体(二機)の耐空検査、それを運ぶトレーラー(二台)の車検... (そのほかにもたくさんあります。)  
このようなタスクは部員全員が気づき、可視化する必要があります。  
このリマインダーはその役割を担います。  
私の所属する航空部では、リマインダーは航空部のグループLINEに通知され、部内で共有しています。

## 動作確認
- テスト環境 \
※初回のアクセスは時間がかかります。
  - bot管理サイト: <https://test-line-bot-django.herokuapp.com/staff-admin/> 
  - ユーザーID: admin 
  - パスワード: editor 
 
    ![image](https://user-images.githubusercontent.com/62125008/120919073-b2dac880-c6f2-11eb-916c-9434404e3bf0.png)
  - LINEbotのQR(上記のQRからLINEで友達追加してください)

リマインダーは午前10時に自動で通知されます。(通知するものはリマインダー日で設定した日付と今日の日付で判断します。)

手動で通知したい場合は以下のURLにアクセスすることでもリマインダーの通知を流すことができます。

通知トリガーURL: <https://test-line-bot-django.herokuapp.com/callback/> 
- 使用例
  - https://ku-glider-platform.herokuapp.com/mypage/
  - ユーザーID: viewer  (実際に私の所属する航空部のグループLINEにて運用中の為、編集権限はありません。)
  - パスワード: non_editor 
## 機能
- リマインダー設定
  - Botに設定したいリマインダーを設定する(カテゴリー、タグは後の検索用に付けてください)

- 合宿リマインダー設定
  - 合宿のリマインダーに特化した設定。 合宿の日程は毎年あまり変動がないため使いまわせるようにリマインダー日の月と日で通知日を判断します。教官のブッキング等があるため、基本的に2ヶ月前から準備します。

- 資料庫
  - Botとは無関係です。 資料の保管場所に使ってください。
## 構成図
![base](https://user-images.githubusercontent.com/62125008/116781584-bf9a4a00-aabe-11eb-8bc4-ddecbb559277.png)
- 使用する際の入力箇所
  - settings.py 30行目
  - viwes.py 147,148行目
  - .env 1行目

- 使用したクラウド
  - Heroku (アドオンでHeroku_scheduler)

- データベース
  - PostgresSQL

Heroku_schedulerに以下を設定(アラートを流したい時間で実行)

```
curl [自分のURL]/callback
```

# リマインダーBot管理画面
![image](https://user-images.githubusercontent.com/62125008/119561882-af853a00-bde0-11eb-94ee-6d1a35896512.png)

## 合宿場所を設定すると「やることリスト」が生成されます
![image](https://user-images.githubusercontent.com/62125008/119562063-e4918c80-bde0-11eb-94b2-9f2e4221f4e8.png)
![image](https://user-images.githubusercontent.com/62125008/119562726-a0eb5280-bde1-11eb-9906-ba381104c223.png)


![image](https://user-images.githubusercontent.com/62125008/119562094-eb200400-bde0-11eb-81f6-527510c90c79.png)
