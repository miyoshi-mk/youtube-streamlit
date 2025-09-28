import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')
# st.write('DataFrame')
# df = pd.DataFrame( {
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

# st.write(df)　どちらでも同じ表示(writeは引数を指定できない)
# st.dataframe(df, width=100, height=100)
# axis=0は行、1は列
# st.dataframe(df.style.highlight_max(axis=0))

# staticな表（静的、ただの表）
# st.table(df.style.highlight_max(axis=0))

# マークダウン記法（見出し１～３）
# """
# # 章 
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
# 20行3列の表（乱数）
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
#折れ線グラフ
# st.line_chart(df)
# st.area_chart(df)

# 棒グラフ
# st.bar_chart(df)

# MAP(緯度、経度)
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

# 画像表示(引数で幅を自動にしている)
# st.write('Display Image')

# img = Image.open('icon.jpg')
# st.image(img, caption='image photo', use_column_width=True)


# チェックボックスで画像を表示させる
# st.write('Display Image')

# if st.checkbox('Show Image'):
#     img = Image.open('icon.jpg')
#     st.image(img, caption='image photo', use_column_width=True)

# st.write('Interactive Widgets')

# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：', text

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、', option, 'です。'

# サイドバーに表示する
# st.sidebar.write('Interactive Widgets')
# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition

# 2カラムのレイアウトにする
st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

# 表示を隠す
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition


st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)