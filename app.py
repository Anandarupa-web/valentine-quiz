import streamlit as st
import os

st.set_page_config(page_title="Valentine Quiz 💖")

st.title("💘 CDS Valentine Quiz")

# Absolute image folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")

# Who are you?
person = st.radio(
    "1. Your name?",
    ["Sneha 🌹", "Nausheen 🔥", "Samadrita 💙"]
)

score = {
    "Sneha 🌹": 0,
    "Nausheen 🔥": 0,
    "Samadrita 💙": 0
}

q2 = st.radio(
    "2. If you had the power to magically eliminate someone, who would it be?",
    ["Modi 🗳️", "Epstein ✈️", "Trump 🎩"]
)

q3 = st.radio(
    "3. Your fav beach destination?",
    ["Kovalam 🌊", "Varkala 🌅", "Sanghamukham 🌴"]
)

q4 = st.radio(
    "4. Who among the following is the best human being?",
    ["Atif Aslam 🎤", "Himesh Reshammiya 🎶", "Sajid 🎧"]
)

q5 = st.radio(
    "5. Whom do you like more?",
    ["Long tail - the cat 🐱", 
     "The dog Aritra brought 🐶", 
     "Fuchka - the cat 🐾"]
)

q6 = st.radio(
    "6. Your favourite dinner?",
    ["Friday - Alfahm 🍗", 
     "Alfahm Mandi 🍖", 
     "Chetta food 🤢"]
)

q7 = st.radio(
    "7. Ideal night?",
    ["Sleep early 😴", 
     "Talk till 3am 🌙", 
     "Nap all day 🛌"]
)

q8 = st.radio(
    "8. You like sleeping with?",
    ["Cats 🐱", 
     "Girls 💅", 
     "Lot of girls 😈"]
)

q9 = st.radio(
    "9. Your fav person?",
    ["Pillow 🛏️", 
     "Cutie 💖", 
     "V 💘"]
)

q10 = st.radio(
    "10. Your toxic trait? 😌",
    ["Overthinking 💭", 
     "Sleeping too much 😴", 
     "Obsessing over one person 💘"]
)

q11 = st.radio(
    "11. Your comfort activity?",
    ["Listening to sad songs 🎧", 
     "Scrolling reels 📱", 
     "Staring at ceiling 🌌"]
)

q12 = st.radio(
    "12. Pick a vibe:",
    ["Soft romance 🌸", 
     "Dramatic love story 🎭", 
     "Chaotic energy ⚡"]
)

import random

if st.button("Your Valentine is 💘"):

    # Political vibe → Sneha
    if q2 == "Modi 🗳️":
        score["Sneha 🌹"] += 2

    # Beach logic
    if q3 == "Varkala 🌅":
        score["Sneha 🌹"] += 2
        score["Samadrita 💙"] -= 1
        score["Nausheen 🔥"] -= 1

    # Atif bias toward Nausheen (not guaranteed)
    if q4 == "Atif Aslam 🎤":
        score["Nausheen 🔥"] += 2
        score["Sneha 🌹"] += 1  # small competing boost

    # Cats logic
    if q5 in ["Long tail - the cat 🐱", "Fuchka - the cat 🐾"]:
        score["Sneha 🌹"] += 1
        score["Samadrita 💙"] += 1

    # Dinner logic
    if q6 == "Chetta food 🤢":
        score["Samadrita 💙"] -= 2
        score["Nausheen 🔥"] -= 2

    # Lazy logic → Samadrita
    if q7 in ["Sleep early 😴", "Nap all day 🛌"]:
        score["Samadrita 💙"] += 2

    # V logic → Strong Nausheen boost
    if q9 == "V 💘":
        score["Nausheen 🔥"] += 3

    # Toxic trait logic
    if q10 == "Sleeping too much 😴":
        score["Samadrita 💙"] += 2
    elif q10 == "Obsessing over one person 💘":
        score["Nausheen 🔥"] += 2
    else:
        score["Sneha 🌹"] += 1

    # Comfort activity
    if q11 == "Listening to sad songs 🎧":
        score["Nausheen 🔥"] += 2
    elif q11 == "Staring at ceiling 🌌":
        score["Samadrita 💙"] += 1

    # Vibe logic
    if q12 == "Soft romance 🌸":
        score["Sneha 🌹"] += 2
    elif q12 == "Dramatic love story 🎭":
        score["Nausheen 🔥"] += 2
    else:
        score["Samadrita 💙"] += 1

    # Mild randomness (prevents deterministic results)
    score[random.choice(list(score.keys()))] += 1

    score.pop(person)

    result = max(score, key=score.get)

    st.success(f"💘 Your Valentine is: {result} 💘")

    if result == "Sneha 🌹":
        st.image(os.path.join(IMAGE_DIR, "sneha.jpg.jpg"), width=350)

    elif result == "Nausheen 🔥":
        st.image(os.path.join(IMAGE_DIR, "nausheen.jpg.jpg"), width=350)

    elif result == "Samadrita 💙":
        st.image(os.path.join(IMAGE_DIR, "samadrita.jpg.jpg"), width=350)

    st.balloons()
    if st.button("Play Again 🔁"):
        st.rerun()
