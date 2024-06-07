# pip install selenium
# pip install webdriver-manager

from selenium import webdriver

wd = webdriver.Chrome()

from selenium.webdriver.chrome.options import Options
# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# 웹피이지 해당 주소 이름
driver.get("https://www.naver.com")