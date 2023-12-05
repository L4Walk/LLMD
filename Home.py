import streamlit as st
from utils import getModelUrls
from dotenv import load_dotenv

load_dotenv()

"""
# LLMD

`LLMD`是一个基于streamlit的大语言模型下载器，支持从model scope上下载管理语言模型
"""


def update_urls():
    getModelUrls.downloads()


if st.button("更新下载地址"):
    update_urls()