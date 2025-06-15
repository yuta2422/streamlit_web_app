import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#データの分析
df = pd.read_csv('./date/平均気温.csv', index_col='月')
st.subheader("平均気温データ")
st.dataframe(df)
st.line_chart(df)
st.bar_chart(df['2023年'])

#matplotlibのグラフ
fig,ax= plt.subplots()
ax.plot(df.index, df['2023年'])
ax.set_title('matplotlib.graph')
st.pyplot(fig)