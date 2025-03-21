import streamlit as st
import random

# Page title
st.set_page_config(page_title="Growth Mindset Project", page_icon="★")

# Title and introduction
st.title("Growth Mindset Challenge: Web App with Streamlit!")

st.header("👋 Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements!")

# Quote Section
st.header("💮 Today's Growth Mindset Quote") 
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill")

# Challenge Section
st.header("☰ What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

# If user has entered a challenge
if user_input:  
    st.success(f"👉 You're facing: {user_input}. Keep pushing forward toward your goal!")  
else:  
    st.warning("Tell us about your challenge to get started!")

# Reflection Section
st.header("📝 Reflect on Your Learning") 
reflection = st.text_area("Write your reflections here:")

if reflection:  
    st.success(f"✨ Great Insight! Your reflection: {reflection}")  
else:  
    st.info("Reflecting on past experiences helps you grow! Share your thoughts.")

# Achievements Section
st.header("👏 Celebrate Your Wins! 😍") 
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:  
    st.success(f"👍 Amazing! You achieved: {achievement}")  
else:  
    st.info("Big or small, every achievement counts! Share one now! 😉")

# Need More Motivation? (Looks like a natural part of the code)
st.header("🔥 Need More Motivation?")

motivational_quotes = [
    "Believe you can, and you're halfway there. – Theodore Roosevelt",
    "Difficulties in life are intended to make us better, not bitter. – Dan Reeves",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Every day is a new beginning. Take a deep breath and start again.",
    "Growth begins at the end of your comfort zone. – Neale Donald Walsch",
    "Your limitation—it’s only your imagination. Push beyond it!"
]

st.info(f"💡 {random.choice(motivational_quotes)}")

# Footer
st.write("---")  
st.write("👌 Keep believing in yourself. Growth is a journey, not a destination! 👈")  
st.write("😎 Created by Nimoo Khan ❤️")
