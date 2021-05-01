

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

