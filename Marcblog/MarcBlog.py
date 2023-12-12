import requests
import streamlit as st
import PIL as iamge
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Blogspot", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/3eeddf6c-a596-406e-bcd9-c9135b2bc1b3/yrXkERhEJo.json")

with st.container():
    st.subheader("Hi, i am Marc Ryan:wave:")
    st.write("A Computer Engineering student")
    st.title("Welcome to my Blogspot")
    st.write("---")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.image("profile.jpg")
        
        st.title("About Me")
        st.write("##")
        st.write("Meet Marc Ryan B. Cordoto: A Young Driven Programming Enthusiast")
        
        st.write("Hi everyone! I'm Marc Ryan B. Cordoto, a 17-year-old young programmer from the beautiful town of Placer, Surigao del Norte. Born on March 14, 2006, I'm currently pursuing a Bachelor of Science in Computer Engineering at Surigao del Norte State University.")
        
        st.write("Ever since I was young, I've always been fascinated by technology and how it works. This curiosity led me to explore the world of programming, and I quickly discovered a passion for it. Learning code can be challenging, but the satisfaction of creating something new and functional is truly rewarding.")
        
        st.write("Choosing computer engineering as my course was a natural decision fueled by my intrinsic interest in programming and technology. I'm excited about the vast possibilities that this field offers, from developing innovative software applications to contributing to the advancement of artificial intelligence.")
        
        st.write("While I recognize the challenges ahead, I'm driven by a strong sense of determination and a willingness to learn. I believe that with hard work and perseverance, I can overcome any obstacle and achieve my goals in the field of computer engineering.")
    
        st.subheader("From Discordant Notes to Harmonious Melodies: Leading the Band")
        st.image("dlc.jpg")
        st.write("Music allows me to express myself in ways that code simply cannot. As a passionate DLC musical trainor/director, I find immense joy in guiding young musicians and helping them unlock their musical potential. Watching them learn, grow, and come together to create beautiful music is a truly rewarding experience. This passion has translated into tangible success as well, with my total earnings exceeding 15k as a minor. The recent championship win at the BSP district-wide scout camporee DLC competition serves as a testament to the dedication and hard work of both me and my band.")
    
    with right_column:
     st.lottie(lottie_coding, height=500, key="coding")
        
     st.write("---")
        
     st.title("My hobbies")
     st.write("##")
     st.write("Today, we delve into My hobbies and achievements, showcasing diverse personality and unwavering dedication.")
        
     st.write(
            """
            My Hobbies:
            - Playing Chess
            - Watching Movies
            - Playing Basketball
            - Calisthenic Exercises
            - Also a passionate DLC Musical Trainor/Director
            """)
        
     st.subheader("Checkmating My Way to Success: Adventures in Chess")
     st.image("chess.jpg")
        
     st.write("Chess is more than just a game for me; it's a battlefield where I can test my strategic mind and outwit my opponents. With a current rating of 958 in blitz and 837 in bullet, I'm constantly pushing myself to improve, analyzing every move and learning from every defeat. My dedication paid off when I became the youngest top 10 contender in the senior division of our municipality's inter-barangay tournament. This achievement solidified my passion for the game and fueled my desire to reach even greater heights in the chess world.")
     
     st.subheader("Beyond the Code: Staying Active and Engaged")
    
     st.write("While I spend a significant amount of time immersed in the world of computers, I recognize the importance of maintaining a balanced lifestyle. Basketball provides a welcome escape from the screen, allowing me to stay active, challenge myself physically, and build camaraderie with my teammates. Engaging in calisthenic exercises pushes my physical limits and helps me stay focused and disciplined. These activities serve as important reminders to step away from the keyboard, explore different avenues, and maintain a healthy body and mind.")
        
        
        
            
            
            
            
        
        
        
        
        
        
        
        