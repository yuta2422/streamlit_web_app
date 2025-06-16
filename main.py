import streamlit as st
from PIL import Image
import datetime
import pandas as pd
import matplotlib.pyplot as plt
st.title("練習アプリ")
st.caption("これは動画用のアプリである")

col1, col2 = st.columns(2)
with col1:
    st.subheader("自己紹介")
    st.text("日本大学理工学部応用情報工学科3年の西悠太です")

    # 画像の表示
    image = Image.open("top_soho.jpg")
    st.image(image, width=200)

    with st.form(key="form1"):
        # テキストboxの表示
        name = st.text_input("名前")
        address = st.text_input("住所")

        #ラジオの表示
        age_category = st.radio(
            "年齢カテゴリー",
            ["子供(１８歳未満)", "大人(１８歳以上)"]
        )

        #複数選択
        hobbies = st.multiselect(
            "趣味",
            ["読書", "映画鑑賞", "音楽鑑賞", "スポーツ", "旅行"]
        )

        # チェックボックスの表示
        agree = st.checkbox("利用規約に同意する")

        #スライダー
        height = st.slider(
            "身長(cm)",
            min_value=100,
            max_value=250,
            value=170,
            step=1
        )

        #日付
        start_date = st.date_input(
            "開始日",
            datetime.date(2025, 6, 15))
        
        #カラーピッカー
        color = st.color_picker(
            "好きな色",
            "#00f900"
        )

        # ボタンの表示
        submit_button = st.form_submit_button("送信")
        cancel_button = st.form_submit_button("キャンセル")
        print(f'submit_button:{submit_button}')
        print(f'cancel_button:{cancel_button}')

    # ボタンが押されたときの処理
    if submit_button:
        st.text(f"こんにちは、{name}さん！{name}さんの住所は{address}ですね。")
        st.text(f'年齢層:{age_category}')
        st.text(f'趣味:{", ".join(hobbies)}')
        st.text(f'身長:{height}cm')
        st.text(f'開始日:{start_date}')
        st.text(f'好きな色:{color}')
    if cancel_button:
        st.text("キャンセルされました。")



with col2:
    #データの分析
    df = pd.read_csv('平均気温.csv', index_col='月')
    st.subheader("平均気温データ")
    st.dataframe(df)
    st.line_chart(df)
    st.bar_chart(df['2023年'])

    #matplotlibのグラフ
    fig,ax= plt.subplots()
    ax.plot(df.index, df['2023年'])
    ax.set_title('matplotlib.graph')
    st.pyplot(fig)

