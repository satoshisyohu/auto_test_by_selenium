# auto_test_by_selenium

this is a test repository for auto tests

1. csvファイル or json ファイルからjobを実行する
2. クロームを開いてクリックを実行する
   - htmlのinputのところを探してname="hoge"を探して
   - find_element(By.NAME, 'hoge')のかたちで検索を実施する
   - 実行後にパラメータのスクリーンショットを取得する
3. 実行後に終了したことを結果として受け取る
4. Loggingでログを取得する
   - apiを使用する
5. gcsにファイルが存在していることを確認する


### 調べる必要があること
- ログの取得方法はpythonクライアントがないのでapiを使用する([API](https://cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list?hl=ja))
  - podでログを取得出来ひんのが辛いなあ
- gcs クライアントを使用方法([参照](https://dev.classmethod.jp/articles/gcs-python-client-libraries-how2/))

### 問題点　
- selenium で実行すると待ち時間が発生してしまう
- 