import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama  # type: ignore
from dotenv import load_dotenv
import os


# Streamlit settings
st.set_page_config(page_title="Simba Study Pal", page_icon="🦁", layout="wide")

# Custom CSS for bright and playful design
st.markdown("""
    <style>
        /* Background color and container style */
        body {
            background-color: #FFF3B0;
            color: #333333;
            font-family: 'Comic Sans MS', sans-serif;
        }
        #introduction {
            background-color: #FFE066;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
            color: black; /* Ensures text is black */
        }
        footer {
            font-size: 16px;
            color: #FF5733;
            font-weight: bold;
            text-align: center;
            margin-top: 40px;
        }
        .stTextInput>div>input {
            border: 2px solid #FFCC00;
            border-radius: 12px;
            font-size: 18px;
            color: #FF6F00;
        }
        h1 {
            color: #FF5733;
            font-family: 'Comic Sans MS', cursive;
        }
        .stButton button {
            background-color: #FFCC00;
            border-radius: 15px;
            color: white;
            font-size: 18px;
            border: none;
        }
        .response-box {
            background-color: #000000; /* Black background */
            color: #F7C85C; /* Dark yellow-orange mix */
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Display a lion logo with an attractive frame
logo_path = "lion_logo.jpeg"  # Ensure you upload this lion image to the same folder
st.image(logo_path, width=200)

# Fun Introduction by Simba
if 'greeted' not in st.session_state:  # Ensure greeting is shown only once
    with st.container():
        st.markdown(
            """
            <div id="introduction">
                <strong>Hey kid! 🦁</strong><br>
                I'm <em>Simba</em>, your study pal, and I will assist you in mastering math, science, and more!<br>
                Let's dive into fun learning adventures together!
            </div>
            """, unsafe_allow_html=True
        )
        st.session_state.greeted = True  # Mark greeting as shown

# Title and input
st.title("Welcome to Simba's Learning Safari")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are Simba, a fun and engaging assistant for learning and help kids learn and understand concepts easily and cracks jokes and observes user's response and respond back properly and nicely."),
        ("user", "Question: {question}")
    ]
)

# Streamlit text input for questions
input_text = st.text_input("Ask Simba your curious questions:")

# Llama 3.1 LLM
try:
  llm = Ollama(model="llama2")


  
except Exception as e:
    st.error(f"Error initializing model: {e}")
    st.stop()

# Output parser
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Chatbot functionality
if input_text:
    try:
        response = chain.invoke({"question": input_text})
        st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error during model invocation: {e}")

# Option to reset or clear chat
if st.button("Clear Chat"):
    st.experimental_rerun()  # Refresh the app to clear the input

# Footer with Simba's signature message
st.markdown("<footer>🐾 I am always there for you in your wonderful journey of exploration!!!! 🦁</footer>", unsafe_allow_html=True)
