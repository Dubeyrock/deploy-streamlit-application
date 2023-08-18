import streamlit as st
import pandas as pd
import numpy as  np
import seaborn as sns
import matplotlib.pyplot as plt

# line chart 
chart_data = pd.DataFrame(np.random.rand(20,3), columns=['Line-1', 'Line-2', 'Line-3'])
st.header('1. charts with Random Numbers')
st.subheader('Line chart')
st.line_chart(chart_data)

# area chart
st.subheader('Area chart')
st.area_chart(chart_data)

# # bar chart 
st.subheader('Bar chart')
st.bar_chart(chart_data)

# matplotlib and seaborn (data visualization)

st.header('2 Data Visualization with matplot & seaborn')
st.subheader('2.1 Loading the dataFrames')
df = pd.read_csv('iris (1).csv')
st.dataframe(df)

st.subheader('2.2 Distribution Bar Graph with Matplotlib')
fig = plt.figure(figsize=(15,8))
df['species'].value_counts().plot(kind = 'bar')
st.pyplot(fig)

st.subheader('2.3. Distribution Plot with Seaborn')
fig = plt.figure(figsize=(15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)


st.header('3. Multiple Graphs')

col1, col2 , col3 = st.columns(3)

with col1:
    st.subheader('KDE = False')
    fig1 = plt.figure()
    sns.histplot(df['sepal_length'], kde=False)
    st.pyplot(fig1)

with col2:
    st.subheader('KDE = True')
    fig2 = plt.figure()
    sns.histplot(df['sepal_length'], kde=True)
    st.pyplot(fig2)

with col3:
    st.subheader('KDE = True')
    fig3 = plt.figure(figsize=(5,5))
    sns.histplot(df['sepal_length'], kde=True)
    st.pyplot(fig3)


st.header('4. Changing Style')
col1, col2 , col3 = st.columns(3)
with col1:
    fig = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['petal_length'], hist = False)
    st.pyplot(fig)
with col2:
    fig = plt.figure()
    sns.set_theme(context = 'poster', style = 'darkgrid')
    sns.distplot(df['petal_length'], hist = False)
    st.pyplot(fig)


st.header('5. Exploring Different Graphs')

st.subheader('5.1 Scatter Plot')
fig,ax = plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size = (2,100)))

st.pyplot(fig)

st.subheader('5.2 Count-Plot')
fig = plt.figure(figsize=(15,8))
sns.countplot(data = df, x = 'species')
st.pyplot(fig)


st.subheader('5.3 Box-Plot')
fig,ax = plt.subplots(figsize=(15,8))
sns.boxplot(data = df , x ='species', y = 'petal_length')
st.pyplot(fig)

st.subheader('5.4  Violen-Plot')
fig,ax = plt.subplots(figsize=(15,8))
sns.violinplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(fig)
 



