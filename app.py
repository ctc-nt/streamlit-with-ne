from backend import get_system_version,get_users,get_tty
import streamlit as st

st.write(get_system_version())
st.write(get_users())
st.write(get_tty())