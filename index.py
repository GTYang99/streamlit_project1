import streamlit as st
import time

print("程式起點")
st.title('這是我的第一個streamlit標題')
st.header('這是我的次標題')
st.subheader('這是我的三級標題')
st.write('這是段落1')
st.write('這是段落2')
st.write('這是段落3')
st.markdown('''
---
# H1
---
## H2
---
### H3
---
#### H4
---
##### H5
---
###### H6
''')
st.text("Hello world")

st.sidebar.markdown('''
### 這是sidebar
---
這是**段落1**
---
這是***段落2***
''')

with st.sidebar:
    st.markdown('''
    ### 這是sidebar2
    ---
    這是**段落2-1**
    ---
    這是***段落2-2***
    ''')
    btn1 = st.button('按鈕1')
    if btn1:
        print("btn1被按了")

def downloaddata():
    print("下載資料")

# 要給一個跳出迴圈的指令
# while True:
#     time.sleep(5)
#     print('過了五秒')
#     downloaddata()
    # st.experimental_rerun

# while True:


print('程式結束點')