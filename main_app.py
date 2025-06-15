import streamlit as st
from PIL import Image


st.title("練習アプリ")
st.caption("これは動画用のアプリである")

 # 画像の表示
image = Image.open("./date/top_soho.jpg")
st.image(image, width=200)


