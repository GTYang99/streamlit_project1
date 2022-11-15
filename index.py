import streamlit as st
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Use a service account.
app = None
db = None
if db is None :
    key_dict = json.loads(st.secrets["textkey"])
    cred = credentials.Certificate(key_dict)
    if app is None:
        app = firebase_admin.initialize_app(cred)
    db = firestore.client()

doc_ref = db.collection('records')
docs = doc_ref.get()
print(docs)
for doc in docs:
    print(doc)

st.title('光線和距離即時監控')

def downloaddata():
    print("下載資料")
    