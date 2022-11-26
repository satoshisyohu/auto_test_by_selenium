# auto_test_by_selenium

this is a test repository for auto tests

1. csvファイル or json ファイルからjobを実行する
2. クロームを開いてクリックを実行する
   - htmlのinputのところを探してname="hoge"を探して
   - find_element(By.NAME, 'hoge')のかたちで検索を実施する
3. 実行後に終了したことを結果として受け取る
4. Loggingでログを取得する
5. gcsにファイルが存在していることを確認する
