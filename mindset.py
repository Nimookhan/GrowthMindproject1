#  streamlit 
import streamlit as st

st.set_page_config(page_title= "growth mindset Project", project_icon="★")
st.title("Growth Mindset challenge: web App with streamlit!")

st.header("👋 welcome to your Growth Journey!")
st.write("Ebrace chllenges, learn from mistakes, and  unlock your full potential..This Ai-powered app Helps  you build a growth mindset with reflection,Challenges,and achivements!►")

#  Quote section
st.header("💮 Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts.-winston churchill")

st.header("☰ What's Your Challenge Today?")
user_input = st.time_input("Desribe a challenge you're facing:")


#   Conditions
if user_input:
    st.success(f"👉 You're facing: {user_input}. keep pushing forward towords your goal!")
else:
    st.warning("Tell us about your challenge to get started!")

#   Reflexing
st.header("Reflect on your Learning ")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"✨ Great Insight! Your reflections: {reflection}")
else:
    st.info("Reflecting on past experience help you growth! share your difficulties")   


#   Acheivements
st.header("👏 Celebrate Your Wins!😍")
acheivment = st.text_input("share something you've recently accomlished: ")


if acheivment:
    st.success(f"👍 Amazing! you acheived: {acheivment}")
else:
    st.info("Big or small , every acheivement counts! share one now!😉")    


    #   Footer 
st.write("- - - ")
st.write("👌 keep believing in yourself. Growth is a Journey, not a destination!👈")
st.write("**😎 Created By Nimoo khan**❤️️")    