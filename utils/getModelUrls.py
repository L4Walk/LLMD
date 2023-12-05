import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
import json
import os

def get_model_links(url):
    print("进入下载程序")
    # 设置 Edge WebDriver
    edge_options = Options()
    edge_options.add_argument('--no-proxy-server')  # 禁用代理
    driver = webdriver.Edge(options=edge_options)

    driver.get(url)
    
    # 等待页面加载（根据需要调整等待时间）
    driver.implicitly_wait(10)
    
    # 获取渲染后的页面源代码
    html_content = driver.page_source
    driver.quit()
    
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 提取链接（根据实际页面结构调整选择器）
    links = soup.find_all('a', href=True)
    model_links = [link['href'] for link in links if 'models' in link['href']]
    models = {link.get_text(strip=True): link['href'] for link in model_links if '/models/' in link['href']}

    print("下载完毕")
    print(models)

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
