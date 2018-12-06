import platform
import time
import sys
import os
from webBrow import ProxyWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread


def wait_for(element, by1, by2):
    return element.until(EC.presence_of_element_located((by1, by2)))


def send_text(wait_br, class_name, text):
    element = wait_for(wait_br, By.CLASS_NAME, class_name)
    element.send_keys(text)
    element.send_keys(Keys.ENTER)
    return element


def run():
    pw = ProxyWebDriver(**kw)
    br, wait_br = pw.get_driver()
    br.get(
        "http://admin.t7.site.webot.ai/static/h51/index.html?code=982ea76e92a211e787e1000c2913faa4&time=1543835171504")
    wait_for(wait_br, By.ID, 'write').click()
    for i, msg1 in enumerate(msg1s):
        send_text(wait_br, 'write', msg1 + str(i))
        print(msg1 + str(i))
        time.sleep(2)
    br.find_element_by_xpath("//div[@class='btn-box show-tools']/button[2]").click()
    time.sleep(2)
    print('已点击转人工')
    for i, msg2 in enumerate(msg2s):
        send_text(wait_br, 'write', msg2 + str(i))
        print(msg2 + str(i))
        time.sleep(2)


def _server():
    ser_win_lin = tuple(platform.architecture())
    name = ser_win_lin[1]
    if 'Win' in name:
        return 1
    else:
        return 2


if __name__ == '__main__':
    length = sys.argv
    if _server() == 2:
        kw = {
            'path': os.getcwd() + '/webdriver/linux/chromedriver',
            'headless': True
        }
    else:
        kw = {
            'path': os.getcwd() + '/webdriver/windows/chromedriver.exe',
            'headless': True
        }
    msg1s, msg2s = [['robot'] * 10, ['人工客服对话'] * 10]

    for c in range(0, int(length[-1]) if len(length) == 2 else 1):
        t = Thread(target=run)
        t.start()
