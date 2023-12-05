import streamlit as st
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import subprocess
import shutil
import time
import sys
import os

from utils.config import config

#logger = setup_logger()

#logger.info("进入 本地模型管理 页面")

st.title("本地模型管理")
st.write("查看和管理本地已下载的模型")



# 默认路径：项目根目录/models
save_path = config.model_dir

# 检查路径是否存在
if not os.path.exists(save_path):
    # 如果不存在，则创建该路径
    os.makedirs(save_path)
    print(f"创建了文件夹：{save_path}")
else:
    print(f"文件夹已存在：{save_path}")

# 使用session_state来跟踪输入框的状态
if 'editable' not in st.session_state:
    st.session_state.editable = False

# 根据状态显示输入框
if st.session_state.editable:
    # 可编辑状态
    save_path = st.text_input("地址", value=save_path)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        print(f"创建了文件夹：{save_path}")
    else:
        print(f"文件夹已存在：{save_path}")
    
    config.update_model_dir(save_path)
else:
    # 只读状态
    st.text_input("地址", value=save_path, disabled=True)

# 切换按钮
if st.button('修改LLM保存路径'):
    st.session_state.editable = not st.session_state.editable
    if not st.session_state.editable:
        # 这里可以添加代码来处理保存路径的更新
        st.write(f"保存路径已更新为: {save_path}")



# 创建一个空的 DataFrame
data = {
    "模型名称": [],
    "Hugging Face 主页": [],
    "Model Scope 主页": []
}
df = pd.DataFrame(data)


"""
## 本地LLM
"""
# 获取save_path下的所有子目录
def get_subdirectories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]


# 打开本地模型
def open_model_Folder(path):
    if sys.platform == "win32":
        os.startfile(path)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", path])
    else:  # Assume it's a Unix-like system (Linux, etc.)
        subprocess.Popen(["xdg-open", path])


# 删除本地模型
def delete_model(path):
     # 检查文件夹是否存在
    if os.path.exists(path):
        # 删除文件夹及其所有内容
        shutil.rmtree(path)
        st.success(f"文件夹 {path} 已被删除")
        
    else:
        st.error(f"文件夹 {path} 不存在")
       



# 获取Models列表项
items = get_subdirectories(save_path)

# 为每个列表项创建一个按钮
for index, item in enumerate(items):  
    # 使用 Streamlit 的列功能来并排显示按钮和文本
    col1, col2, col3 = st.columns([3, 1, 2])
    with col1:
        st.write(item)  # 显示列表项名称
    with col2:
        if st.button(f"本地打开", key=f"open_{index}"):
            open_model_Folder(os.path.join(save_path, item))
    with col3:
        # 创建按钮，并使用 lambda 函数来传递当前项的名称
        if st.button(f"删除模型", key=f"delete_{index}"):
            path = os.path.join(save_path, item)
            delete_model(path)
 
            # 延迟0.5s刷新界面  
            time.sleep(0.5)  
            st.experimental_rerun()
