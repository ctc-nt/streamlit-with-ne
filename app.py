from backend import get_system_version,get_users,get_tty
import streamlit as st
import pandas as pd

# df = pd.json_normalize(res, record_path=["info"])
# df

menu = [
    "top",
    "users",
    "tty"
]

selected_menu = st.sidebar.radio("Menu",menu)

if selected_menu == "top":
    res = get_system_version()
    st.write("OS Version",res["systeminfo"]["Boot"]["System"]["Version"])
    st.write("Model",res["systeminfo"]["HW"]["Model"])

if selected_menu == "users":
    "Current User Confugiration"
    res = get_users()
    df = pd.json_normalize(res["users"])
    df
    "参考 : 取得してきた生のjson"
    res

    "Create User"

if selected_menu == "tty":
    "Current tty Confugiration"
    res = get_tty()
    df = pd.json_normalize(res["ttylist"])
    df
    "参考 : 取得してきた生のjson"
    res

    "Modify tty"