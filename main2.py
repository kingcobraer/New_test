import streamlit as st
from sklearn import datasets
import pandas as pd
from PIL import Image

pic = st.sidebar.selectbox("这是一个下拉框", ["A", "B"])


import time
bar = st.progress(0.0)
for percentage in range(20):
    time.sleep(0.02)
    bar.progress(percentage * 0.05 + 0.05)

with st.spinner('Wait for it...'):
    time.sleep(1)
st.success('Done!')

'#### 这是Dataframe'
df = datasets.load_iris()
df = pd.DataFrame(data=df.data, columns=df.feature_names)
df
st.dataframe(df)
st.markdown('# 这是一级标题')
'# 这是一级标题'

st.markdown('## 这是2级标题')
st.markdown('### 这是3级标题')
st.caption('这是对上面内容的一条注解')
'# dsd f'

