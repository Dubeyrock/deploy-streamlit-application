import streamlit as st


st.title(' Welcome , CuberTech Solution')
st.header(' its a new firms. ')
st.header('establish in 1898.')
st.text('basically works in ml / domain.')

st.markdown('# Hii DataScientist')

st.success( 'successfully created your Account')
st.info('thanks for giving me your information.')
st.warning('please check your email id again its correct or not')
st.error('something went worng')

exp = ZeroDivisionError('divsion not possible')
st.help(ZeroDivisionError)

st.write("range(1,10)")
st.write(range(1,10))
st.write('1+2+ 3')
st.write(1+2+4)

st.code('x = 1000'
        'for i in range(x):\n'
            '\tprint(i)')


# checkbox 
st.checkbox('Male')
st.checkbox('female')
st.checkbox('correct information fill')


if (st.checkbox('male')):    # checkbox with validation
     st.write("You 're an adult! ")

st.radio('select  gender : ' , {'male', 'female', 'other'})   # radio 

st.radio('select country :', {'INDIA', 'Australia', 'America', 'England', 'none of above'})

# selectbox
st.subheader('select box')
selectBox = st.selectbox("Data Science :" , ['Data Analysis', 'web Scrapping', 
            'machine learning' , 'deep learning', 'Data Science', 'image processing'])

st.write("you 've selected :" , selectBox)

# multi select box 
st.subheader('multiSelect Box')
multiselBox = st.multiselect("Data Science :" , ['Data Analysis', 'web Scrapping', 
            'machine learning' , 'deep learning', 'Data Science', 'image processing'])

# button 
st.subheader("Button")
if(st.button('click me')):
     st.write('thanks for clicking me')

# slider 
st.subheader("slider ")
st.slider('select the rating ', 1,10, step = 1)


# text input data from the user 

st.subheader("Text Input")
name = st.text_input('Name : ')
password = st.text_input('password :',type = 'password')
if (name):
     st.write('Hi,', name)

# text_area 
st.subheader("Text Area")
textArea = st.text_area('write about us in 500 words')
st.write(textArea)


# input - number 
st.subheader("inputnumber")
st.number_input('select your expect salary ', 10000, 33000000 )
# input-date 
st.subheader("input date")
st.date_input('Date')
# input time 
st.subheader("input time")
st.time_input('Time')


