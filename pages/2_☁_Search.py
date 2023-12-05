# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd


def get_huggingface_download_url(df):

    herf = "url"
    return herf


def get_modelscope_download_url(df):

    herf = "url"
    return herf



"""
# LLM搜索
欢迎来到搜索界面！
在这个页面，你可以使用下面的搜索框来查询你感兴趣的内容。  
只需输入关键词，就能够搜索LLM。
"""


# 创建搜索框
search_query = st.text_input("输入你想搜索的大模型", "")

# 创建一个空的 DataFrame
data = {
    "模型名称": [],
    "Hugging Face 主页": [],
    "Hugging Face 下载": [],
    "Model Scope 主页": [],
    "Model Scope 下载": []
}
df = pd.DataFrame(data)
# 假设这里是你的搜索逻辑，根据搜索查询填充 DataFrame
# 这里只是一个示例，你需要根据实际情况来填充数据
if search_query:
    # 示例数据
    df = pd.DataFrame({
        "模型名称": ["Model 1", "Model 2"],
        "Hugging Face 主页": ["https://huggingface.co/model1", "https:/huggingface.co/model2"],
        "Hugging Face 下载": [""],
        "Model Scope 主页": ["https://modelscope.example.com/model1", "https:/modelscope.  example.com/model2"],
        "Model Scope 下载": [""],
    })

    for i in df.index:
        df.at[i, "Hugging Face 下载"] = get_huggingface_download_url(df.iloc[[i]])
        df.at[i, "Model Scope 下载"] = get_modelscope_download_url(df.iloc[[i]])



# 显示表格
st.table(df)


"""
### 热门模型推荐
"""
hot_data = {
    "模型名称": [],
    "Hugging Face 主页": [],
    "Hugging Face 下载": [],
    "Model Scope 主页": [],
    "Model Scope 下载": []
}
hot_df = pd.DataFrame(hot_data)
hot_df = pd.DataFrame({
        "模型名称": ["Model 1", "Model 2"],
        "Hugging Face 主页": ["https://huggingface.co/model1", "https:/huggingface.co/model2"],
        "Hugging Face 下载": ["url1", "url2"],
        "Model Scope 主页": ["https://modelscope.example.com/model1", "https:/modelscope.  example.com/model2"],
        "Model Scope 下载": ["url1", "url2"],
    })

st.table(hot_df)


