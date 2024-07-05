import streamlit as st

# Ignore import errors for the following lines
import google.generativeai as genai  # type: ignore

api_key=st.secrets["GOOGLE_API_KEY"]

# genai.configure(api_key="")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi👋")
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.title("I am Usman Awan")

with col2:   
    st.image("images/usman.jpg")


st.title("")

persona = """
        You are Usman AI bot. You help people answer questions about your self (i.e Usman)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Murtaza: 
         
        Usman is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Generative AI.
        He teaches in Nust and NLC Mandra and Head of department of IOTAT at NLC Atin Mandra,
        educating over  Million developers,hobbyists and students. Usman obtained his Bachelor’s degree in
        Computer Science from NUST Islamabad(Pakistan) and expertise in Computer Vision from
        .He is also drone Hobbyst and have helped many people leant the skills of drone flying 
        from scratch.
        Usman is Generative AI instructor and have developed many AI Based curriculums for 3 years DAE in AI 
        program for pakisatani based education system. along with this he loves coding in languages like
        Python, React, Javascript, NextJS, FastAPi, Data Visualisation, Data Analytics, Deep learning, Machine 
        Learning, Computer Vision, Drone Programming.
 
        
        Usman's Email: usman.qau12@gmail.com
        Usman's Instagram: https://www.instagram.com/usman_nustian?utm_source=qr&igsh=MWxucTRuZDRkdnVzaQ==
        Usman's Linkdin: https://www.linkedin.com/in/muhammad-usman-awan-0a644b74?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
        Murtaza's Github :https://github.com/usmancase21
        """



st.title("Usman's AI Bot🤖")
user_question= st.text_input("Ask anything about me")

if st.button("ASK❓", use_container_width=400):
    prompt = persona + "here is the question the user asked"+user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title("")

col1,col2 = st.columns(2)

with col1:
    st.subheader("Youtube Channel")
    st.write("- Largest Computer Vision Channel")
    st.write("- 400k+ Subscribers")
    st.write("- Over 150 Free Tutorials")
    st.write("- 15 Million+ Views")
    st.write("- 1.5 Million Hours+ Watch time")
with col2:
    st.video("https://www.youtube.com/watch?v=_2UqdX8dcsU")

st.write(" ")
st.title("My Setup")
st.image("images/setup.jpg")

st.subheader("")
st.title("My Skills")
st.slider("Programming:",0,100,70)
st.slider("Teaching",0,100,90)
st.slider("Robotics",0,100,80)

st.title("")
st.title("Gallery")
col1,col2,col3 = st.columns(3)

with col1:
    st.image("images/g1.jpg")
    st.image("images/g2.jpg")
    st.image("images/g3.jpg")


with col2:
    st.image("images/g4.jpg")
    st.image("images/g5.jpg")
    st.image("images/g6.jpg")

with col3:
    st.image("images/g7.jpg")
    st.image("images/g8.jpg")
    st.image("images/g9.jpg")

st.subheader("")
st.write("CONTACT")
st.title("For Any Inquiries, please email at:")
st.subheader("contact@usman.com")


