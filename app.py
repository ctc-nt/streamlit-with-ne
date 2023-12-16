from backend import get_system_version,get_users,get_tty
import streamlit as st
import pandas as pd

selected_menu = st.sidebar.radio("Menu",["top","users","tty"])

if selected_menu == "top":
    res = get_system_version()
    st.write("OS Version",res["systeminfo"]["Boot"]["System"]["Version"])
    st.write("Model",res["systeminfo"]["HW"]["Model"])

if selected_menu == "users":
    "Current User Confugiration"
    res = get_users()
    df = pd.json_normalize(res["users"])
    df

    "Create User"
    "参考 : 取得してきた生のjson"
    res


if selected_menu == "tty":
    "Current tty Confugiration"
    res = get_tty()
    df = pd.json_normalize(res["ttylist"])
    df

    baud_list=["9600","115200"]
    bitchar_list=["8"]
    parity_list=["none"]
    stop_list=["1"]
    flow_list=["none"]
    detect_dsr_list=["on","off"]    

    "Modify tty Configuration"
    tty = st.selectbox("tty",res["ttylist"],format_func=lambda x : x["tty"],index=0)
    baud = st.selectbox("baud",baud_list)
    bitchar = st.selectbox("bitchar",bitchar_list)
    parity = st.selectbox("parity",parity_list)
    stop = st.selectbox("stop",stop_list)
    flow = st.selectbox("flow",flow_list)
    detect_dsr = st.selectbox("detect_dsr",detect_dsr_list)

    "参考 : 取得してきた生のjson"
    res

