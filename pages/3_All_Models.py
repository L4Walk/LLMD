import streamlit as st
import pandas as pd
import json
import os


# 读取 JSON 文件的函数
def load_data(file_path):
    if not os.path.exists(file_path):
        st.error(f"{file_path}不存在")
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# 创建下载按钮的函数（这里是下载逻辑的占位符）
def download_model(link):
    # 你的下载逻辑
    st.write(f"下载链接：{link}")


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
            download_model(link)
