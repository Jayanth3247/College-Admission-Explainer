from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from main import send_email

st.title('College Course Explainer')
name = st.text_input('What is your name')
mid = st.text_input('Please type your mail id')
course = st.text_input('Which course are you interested in')
marks = st.number_input('How much marks did you score in 12th')

if st.button('Submit'):
    try: 
        send_email(name,mid,course,marks)
        st.write('The email was sent successfully')
    except:
        st.write('There was an error. ')
