import streamlit as st

## 显示各种文本格式的函数 ##

# 显示标题
st.title('Welcome to the world of :red[Streamlit]')

# 显示章节标题
st.header('Header: Pandas DataFrame')

# 显示子标题
st.subheader('Subheader: 子标题 ')

# 显示普通文本
st.text('Text: 普通文本 ')

# 显示描述：caption常用于为插图、表格或图表提供标题和描述
st.caption('caption: 描述 ')


# 显示 markdown 文本1
st.markdown("Load :blue[Iris Data Set]")

# 显示 markdown 文本2
st.markdown("- Markdown : 无序列表")

# 显示latex公式
st.latex('x^2 + y^2 = z^2')

# 显示代码
st.code("a = 10")
