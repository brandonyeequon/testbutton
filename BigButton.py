import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_loving_message():
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            temperature=0.9,
            messages=[
                {
                    "role": "user", 
                    "content": """
                    You name is Brandon Lee. You love Guitar and coding. You absolutly love your wife Lizzy. Here are facts about her:
                    - She is drop dead gorgeous 
                    - She is studying marketing. She is EXTREMELY good at it
                    - She loves Pokemon
                    - She is a straight A student. Very, very smart.
                    - She loves the TV show NIKITA
                    - She loves to include people
                    - She cooks a killer creamy tomato pasta
                    - She speaks fluent Japanese. We met in Japan. 
                    - She loves reading. Recently she's read fourth wing and mistborn.
                    
                    Based on the above facts about my wife Lizzy, write a creative, witty, note or poem. keep it really short! No more than 5 lines. Don't be cheezy or Chiche. Write it either completly in English, or completly in Japanese. (mostly write in english)"""
                }
            ]
        )
        
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating message: {str(e)}")
        return "I love you more than words can express! ❤️"

# Streamlit UI
st.set_page_config(page_title="Love Button", page_icon="❤️")

# Custom CSS for the fancy button
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #ff69b4, #ff1493);
        color: white;
        padding: 2rem 4rem;
        border-radius: 20px;
        border: none;
        font-size: 24px;
        font-weight: bold;
        text-transform: uppercase;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        width: 100%;
        margin: 20px 0;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    div.stButton > button:first-child:active {
        transform: translateY(1px);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Just for Lizzy, from Brandon</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>愛してる</h3>", unsafe_allow_html=True)

# Center the button using columns
col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("Press Here", key="love_button", use_container_width=True):
        with st.spinner("Let's keep this between us..."):
            message = generate_loving_message()
            
            # Display message with animation
            st.markdown("""
                <div style='padding: 20px; 
                            background: rgba(255,192,203,0.1); 
                            border-radius: 10px; 
                            margin: 20px 0;
                            text-align: center;
                            font-size: 20px;
                            font-style: italic;
                            animation: fadeIn 1s;'>
                {}
                </div>
                <style>
                @keyframes fadeIn {{
                    0% {{ opacity: 0; }}
                    100% {{ opacity: 1; }}
                }}
                </style>
            """.format(message), unsafe_allow_html=True)
            