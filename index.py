import streamlit as st

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
    st.button('按鈕1')

print('程式結束點')