import os
from apikey import apikey

import streamlit as st
from langchain_openai import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

st.audio("Lofi hiphop.mp3")
st.image("girl.gif")

st.title(" 🦜️🔗Ask your Homework problem 🧟‍♂️")
prompt = st.text_input("Type your homework question below")


#llms
llm = OpenAI(temperature=0.9)
if prompt:
    response = llm(prompt)
    st.write(response)

with st.sidebar:
    st.write("About me")
    st.image("cutie-cat.gif")
    st.write("My [GitHub](https://github.com/PratikPhysics)")
    st.write("My [Linkedin](https://www.linkedin.com/in/pratik-ramteke-21573317a/)")
    st.write("My [YouTube](https://www.youtube.com/@pratikgizmo6436)")





