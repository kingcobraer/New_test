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

# 方法一
st.code("mylist = [i for i in range(10)]")

# 方法二
"""```python 
mylist = [i for i in range(10)]"""

# 方法三
'''```
这是一个代码框
'''

'Hi好阿达水电费'

'# 得到水电 __*费水电*__ 费水电费'

r12c1, r12c2, r12c3, r12c4 = st.columns([2, 4, 6, 8])
with r12c1:  # a simple example
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
with r12c2:  # render a line when value is None
    st.metric(label="Number1", value=None, delta="-15")
with r12c3:  # red up and green down
    st.metric(label="Number2", value=666, delta=166, delta_color="inverse")
with r12c4:  # color off
    st.metric(label="HelloWorld", value="刘志昱", delta="说", delta_color="off")

if pic == "A":
    picA1 = "https://i.hexuexiao.cn/up/ca/63/4a/a32912fc26b8445797c8095ab74a63ca.jpg"
else:
    picA1 = 'http://tour.youth.cn/xw/202203/W020220302343706665093.jpg'

col1, col2 = st.columns(2)
with col2:
    st.image(picA1, width=600, caption="This is a Cat")
    '# 哈哈哈哈哈哈哈'
    '# 第四行'
with col1:
    st.image("https://static.streamlit.io/examples/dog.jpg")
    st.image(Image.open(r"C:\Users\Eric Zhang\Pictures\Screenpresso\2022-08-01_22h34_39.gif"))

# st.line_chart(df)
# st.bar_chart(df)

st.button("这是一个按钮")

st.balloons()

st.video(open(r"C:\Users\Eric Zhang\Pictures\Screenpresso\1月14日抢购记录.mp4", "rb").read())

with st.echo():
    st.write('This code will be printed')


