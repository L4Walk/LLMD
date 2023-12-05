import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json
import os
import re
import time

def get_model_links(url):
    print("进入下载程序")
    # 设置 Edge WebDriver
    edge_options = Options()
    edge_options.add_argument('--no-proxy-server')  # 禁用代理
    driver = webdriver.Edge(options=edge_options)
    # 等待页面加载（根据需要调整等待时间）
    driver.implicitly_wait(10)

    # 假设最大页数
    max_pages = 189
    models = []

    for page_number in range(1, max_pages + 1):
        try:
            # 调整url
            page_url = f"{url}?page={page_number}"
            print(f"开始爬取{page_url}")
            driver.get(page_url)


            # 等待页面动态加载内容
            time.sleep(10)  # 根据需要调整等待时间

            # 获取渲染后的页面源代码
            html_content = driver.page_source
          
    
            # 使用 BeautifulSoup 解析 HTML
            soup = BeautifulSoup(html_content, 'html.parser')
    
            # 提取链接（根据实际页面结构调整选择器）
            links = soup.find_all('a', href=True)
            print(links)
            model_links = [link['href'] for link in links if 'models' in link['href']]
    
            print("打印模型链接")
            print(model_links)
    
            
            for link in model_links:
                match = re.search(r'models/(.+)', link)
                if match:
                    models.append([match.group(1),url + '/' + match.group(1)])
       
            print(f"page = {page_number}下载完毕")
            print(models)

        except TimeoutException:
            print(f"Page {page_number} not found or not clickable.")
            break
        except Exception as e:
            print(f"Error on page {page_number} : {e}")
            break

    #models = {link.get_text(strip=True): link['href'] for link in model_links if 'models/' in link['href']}

    # 关闭 WebDriver
    driver.quit()

    print("下载完毕")
    return models

def append_to_json(file_path, data):
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r+', encoding='utf-8') as file:
            file_data = json.load(file)
            file_data.update(data)
            file.seek(0)
            json.dump(file_data, file, ensure_ascii=False, indent=4)
    else:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


def downloads():
  url = 'https://modelscope.cn/models'
  models = get_model_links(url)
  
  # 保存到 JSON 文件
  # 设置日志文件夹路径
  json_directory = os.path.join(os.getcwd(), "datas")
  
  # 如果日志文件夹不存在，则创建它
  if not os.path.exists(json_directory):
      os.makedirs(json_directory)
  
  json_filename = os.path.join(json_directory, "model_scope_links.json")
  
  append_to_json(json_filename, models)
  
  print(f"模型链接已保存到 {json_filename} 文件中。")
