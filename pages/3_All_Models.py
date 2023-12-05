import streamlit as st
import threading
import json
import os
from utils.model_downloader import down_models



# 读取 JSON 文件的函数
def load_data(file_path):
    if not os.path.exists(file_path):
        st.error(f"{file_path}不存在")
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# 创建下载按钮的函数
def download_model(model_name):
    with st.spinner(f'正在下载 {model_name}...'):
        down_models(model_name)
    st.success(f"{model_name} 下载成功")

def download_task(model_name):
    with st.spinner(f'正在下载 {model_name}...'):
        down_models(model_name)
        st.success(f"{model_name} 下载成功")



def start_download_thread(model_name):
    download_thread = threading.Thread(target=download_task, args=(model_name,))
    download_thread.start()


"""
# 全部模型列表
欢迎来到全部模型，这里可以查看截至`2023年12月5日`的所有Model_Scope模型  
"""

#读取本地数据
file_path = './datas/model_scope_links.json'
data = load_data(file_path)

total_count = len(data.items())
st.write(f"共计收录{total_count}个模型，点击按钮即可下载")

# 在 Streamlit 中显示等宽的下载按钮，每行一个
for model_name, link in data.items():
    # 为每个按钮创建一个单独的列布局
    col = st.columns([1])[0]  # 创建一个列，占据整行宽度
    with col:
        if st.button(f" {model_name}"):
            download_model(model_name)
