
import streamlit as st
from datetime import datetime
import time

# Page settings
st.set_page_config(page_title="KulCare - Your Mood Buddy", layout="centered")

# Sidebar for theme toggle
with st.sidebar:
    st.title("🌗 Display Mode")
    mode = st.radio("Choose theme", ["🌞 Light Mode", "🌙 Dark Mode"])

# Colors
if mode == "🌙 Dark Mode":
    background = "#1e1e1e"
    font_color = "#ffffff"
    button_color = "#374151"
else:
    background = "#f6f6f6"
    font_color = "#000000"
    button_color = "#e0e0e0"

# Apply CSS
st.markdown(
    f"""
    <style>
    body {{
        background-color: {background};
        color: {font_color};
    }}
    .stButton>button {{
        background-color: {button_color};
        color: {font_color};
        padding: 0.5em 1em;
        border-radius: 8px;
        border: none;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Mood data
moods = {
    "😰 Anxious": {
        "quote": "Breathe. You are safe.",
        "video": "https://youtu.be/w6T02g5hnT4"
    },
    "😡 Angry": {
        "quote": "Take a pause. You are in control.",
        "video": "https://youtu.be/YFSc7Ck0Ao0"
    },
    "😔 Sad": {
        "quote": "It's okay to cry. You're not alone.",
        "video": "https://youtu.be/2OEL4P1Rz04"
    },
    "😵 Stressed": {
        "quote": "You're doing your best. That is enough.",
        "video": "https://youtu.be/mNBmG24djoY"
    },
    "🥺 Lonely": {
        "quote": "You matter. Someone cares about you.",
        "video": "https://youtu.be/kvtYjdriSpM"
    },
    "😊 Happy": {
        "quote": "That's awesome! Keep the vibe alive.",
        "video": "https://youtu.be/ZbZSe6N_BXs"
    }
}

# App UI
st.title("🌿 KulCare")
st.subheader("How are you feeling today?")

mood = st.selectbox("Choose your current mood:", list(moods.keys()))

if mood:
    selected = moods[mood]
    st.markdown(f"### ✨ {selected['quote']}")
    st.video(selected["video"])

    # Breathing
    st.markdown("---")
    st.markdown("### 🧘‍♀️ Breathe with me")
    with st.empty():
        for i in range(1, 11):
            st.progress(i / 10)
            time.sleep(0.3)
    st.success("Better? You're doing great 🌸")

    # Journal
    st.markdown("---")
    st.markdown("### 📓 Would you like to reflect?")
    journal = st.text_area("What made you feel this way today?", height=150)

    if journal:
        filename = f"kulcare_reflection_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        st.download_button(
            label="📥 Download My Journal Entry",
            data=journal,
            file_name=filename,
            mime="text/plain"
        )

    # Feedback
    st.markdown("---")
    st.markdown("💌 Want to share your thoughts anonymously?")
    st.markdown("[Submit Feedback Here](https://forms.gle/your-google-form-link)")
