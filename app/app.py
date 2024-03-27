import pandas as pd
import streamlit as st

df = pd.read_csv('./data/train.csv')

passengers_cnt = df['PassengerId'].count()
survived_passengers_count = df.loc[df['Survived'] == 1, 'PassengerId'].count()


st.write("Hello! There my first streamlit app for 'Start in Data Science' bootcamp.")

left_column, right_column = st.columns(2)

with left_column:
    card1 = st.container(height=250, border=True)
    card1.title('Count of titanic passengers')
    card1.text(passengers_cnt)

with right_column:
    card2 = st.container(height=250, border=True)
    card2.title('Count of survived titanic passengers')
    card2.text(survived_passengers_count)

st.dataframe(df)
