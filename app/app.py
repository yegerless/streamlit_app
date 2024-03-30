import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df1 = pd.read_csv('./data/train.csv')
df2 = pd.read_csv('./data/test.csv')

df = pd.concat([df1, df2])

passengers_cnt = df['PassengerId'].count()
average_passengers_age = f'{df['Age'].mean():.2f} years'


fig, ax = plt.subplots()
labels = [f'Class {i}' for i in df['Pclass'].unique()]
sizes = df.groupby('Pclass')['PassengerId'].count()
ax.pie(x=sizes, labels=labels, autopct='%.0f%%',
       textprops={'size': 'smaller'}, radius=1)

st.title('Titanic dataset')

st.write("Hello! There is my first streamlit app for 'Start in Data Science' bootcamp.")

column1, column2 = st.columns(2)

column1.metric('Count of titanic passengers', passengers_cnt)
column2.metric('Average age of titanic passengers', average_passengers_age)

st.bar_chart(data=df, x='Sex', y='PassengerId')

st.pyplot(fig)

st.image(image='https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Titanic_in_color.png/2560px-Titanic_in_color.png')

st.dataframe(df)
