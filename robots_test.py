# 로봇 배제 표준

import requests
urls = ["https://www.naver.com/", "https://python.org/"]
filename = "robots.txt"
for url in urls:
  file_path = url + filename
  print(file_path)
  resp = requests.get(file_path)
  print(resp.text)
  print("\n")