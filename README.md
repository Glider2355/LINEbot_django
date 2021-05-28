# 航空部LINEリマインダーBot

## 機能
- リマインダー設定
  - Botに設定したいリマインダーを設定する(カテゴリー、タグは後の検索用に付けてください)

- 合宿リマインダー設定
  - 合宿のリマインダーに特化した設定。 合宿の日程は毎年あまり変動がないため使いまわせるようにリマインダー日の月と日で通知日を判断します。

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
