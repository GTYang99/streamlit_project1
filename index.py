import streamlit as st
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import pandas as pd

# Use a service account.
# app = None
# db = None
if 'firestore' not in st.session_stat:
    st.session_state['firestore'] = True
    key_dict = json.loads(st.secrets["textkey"])
    cred = credentials.Certificate(key_dict)
    app = firebase_admin.initialize_app(cred)
    # if app is None:
    #     app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    st.session_state['db'] = db
db = st.session_state['db']

# 建立與數據庫連線
records_ref = db.collection('records')
# 只取20筆數據
query = records_ref.limit_to_last(20)
docs = query.get()
print(docs)
# for doc in docs:
    # print(doc)
    # print(doc.to_dict()['日期'])        #doc轉成字典
    # dict_data = doc.to_dict()

# doc內容轉換成字典內容，並儲存成pandas的資料結構
datalist = [doc.to_dict() for doc in docs]
dict_data = pd.DataFrame(datalist)

st.title('光線和距離即時監控')
st.table(dict_data)

def downloaddata():
    print("下載資料")
    