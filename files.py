import streamlit as st
import pandas as pd
st.subheader('loading data science dataset')
df = st.file_uploader("upload the csv file:", type =['csv','xlsx'])

#if df is not None:
 #   st.dataframe(df)

df = pd.read_csv('DataScientist.csv')
st.area_chart(df.head())
st.bar_chart(df.head())
#st.table(df)
st.line_chart(df.head())

#  uploading images 
st.subheader('Dealing with Data Scientist')
st.image('images.png')

st.subheader('data science ')
st.image('download.jpg')

st.image('download (2).jpg')


# uploding data science kownledge 
st.subheader('working data scientist')
video_file = st.file_uploader("upload the video file :", type = ['mkv', 'mp4'])
if video_file is not None:
    st.video(video_file, start_time=5)

# uploading machine learning videos
st.subheader('Machine Learning Domain')
video_file = st.file_uploader("ML the video file :", type= ['mkv','mp4'])
if video_file is not None:
    st.video(video_file, start_time=5)


# uploading robot play a chess game 
st.subheader('Robot play a chess game')
video_file = st.file_uploader("Robot  the video file :", type=['mkv', 'mp4'])
if video_file is not None:
    st.video(video_file, start_time=5)

# wroking with audio
st.subheader('Good Morning shivam  ai audio')
audio_file = st.file_uploader("upload goof morning shivam audio file:", type=['mp3', 'wav'])
if audio_file is not None:
    st.audio(audio_file.read())


st.subheader('cuber tech solution ai audio')
audio_file = st.file_uploader("upload the cuber tech audio file:", type=['mp3', 'wav'])
if audio_file is not None:
    st.audio(audio_file.read())





st.subheader('welcome back data scientist ai audio')
audio_file = st.file_uploader("upload welcome back data scientist audio file:", type=['mp3', 'wav'])
if audio_file is not None:
    st.audio(audio_file.read())
