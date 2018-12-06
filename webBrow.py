from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class ProxyWebDriver(object):
    """
    br_name: the name of webdriver
    path: the path of webdriver
    disable_cache:  if the param is true, no img would be loaded
    headless: if the param is true, the webdriver can run on server
    proxy_api: the url of proxy
    """

    def __init__(self, **kwargs):
        self.user_agent = kwargs.get('user_agent', None)
        self.kwargs = kwargs
        self.name = self.kwargs.get('br_name', 'phantomjs')
        self.path = self.kwargs.get('path', "webdriver/windows/chromedriver.exe")
        self.proxy = None
        self.br = None

    def get_driver(self):
        self.br = self._get_webdriver()
        # self.br.maximize_window()
        self.br.set_window_size(1900, 1035)
        # print('get window size ----- > ', self.br.get_window_size())
        self.br.set_page_load_timeout(30)
        self.br.set_script_timeout(20)
        return self.br, WebDriverWait(self.br, 3, 1.0)

    def _get_webdriver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('disable-infobars')  # 屏蔽弹窗
        chrome_options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"')  # 设置请求头
        # chrome_options.add_argument("--proxy-server=http://{}".format(self.proxy))  # 禁止代理
        if self.kwargs.get('disable_cache'):
            chrome_options.add_argument('--disable-cache=false')
            prefs = {"profile.managed_default_content_settings.images": 2}
            chrome_options.add_experimental_option("prefs", prefs)
        if self.kwargs.get('headless'):
            chrome_options.add_argument("--headless")
            # chrome_options.add_argument("--disable-gpu")
        print(self.path)
        return webdriver.Chrome(self.path, chrome_options=chrome_options)

    def quit_webdriver(self):
        self.br.quit()
