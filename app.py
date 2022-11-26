from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

CHROME_DRIVER = "./chromedriver.exe"


@app.route('/')
def hello_world():  # put application's code here
    # optionsを設定することで、selenium実行終了後にchromeが落ちないようになる。(設定しなければ落ちる)
    browser = chrome_setting()
    # アクセスするブラウザを設定する
    browser.get("https://github.com/satoshisyohu/auto_test_by_selenium/tree/main")
    elem = browser.find_element(By.NAME, 'q')
    elem.send_keys("satoshisyohu/banking" + Keys.RETURN)
    # browser.quit()
    return 'Hello World!'


def chrome_setting():
    options = Options()
    options.add_experimental_option('detach', True)
    return webdriver.Chrome(CHROME_DRIVER, options=options)


if __name__ == '__main__':
    app.run()
