import streamlit as st
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Application Default credentials are automatically created.
cred = credentials.Certificate('private/raspberry1-58efc-firebase-adminsdk-tzk5o-6836a56c1e.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

st.title('光線和距離即時監控')

def downloaddata():
    print("下載資料")
    