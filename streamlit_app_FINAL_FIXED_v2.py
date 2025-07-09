
import streamlit as st

st.set_page_config(page_title="Digital Personality Test", layout="centered")

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.answers = []

questions = [
    {
        "question": "Q1: How do you feel when someone sends you a long voice note?",
        "options": [
            "Excited! I love hearing people explain in detail.",
            "Fine, I’ll usually listen and maybe skim.",
            "Annoyed — I wish they’d text instead.",
            "I often skip them entirely."
        ]
    },
    {
        "question": "Q2: Do you check who viewed/reacted to your stories?",
        "options": [
            "Always, I care who sees/reacts.",
            "Sometimes, out of curiosity.",
            "Rarely, unless it’s important.",
            "Never, I just post and forget."
        ]
    },
    {
        "question": "Q3: Do you listen to your own voice notes after sending them?",
        "options": [
            "Yes, always — I want to check how I sound.",
            "Sometimes, if I'm unsure what I said.",
            "Rarely — I don't like hearing my voice.",
            "Never — I just send and move on."
        ]
    },
    {
        "question": "Q4: How do you name your contacts in your phone?",
        "options": [
            "Full names, like 'Laura Gonzalez'",
            "Nicknames or emojis like '🦄Laurita!'",
            "Inside jokes or memes",
            "Whatever I feel in the moment"
        ]
    },
    {
        "question": "Q5: How quickly do you usually reply to non-urgent messages?",
        "options": [
            "Immediately — I feel bad leaving people waiting",
            "Within a few hours",
            "I reply when I feel like it, no pressure",
            "I often forget or ignore them"
        ]
    },
    {
        "question": "Q6: Do you re-read your old conversations?",
        "options": [
            "Yes, I love reliving memories and reactions",
            "Only when I need info or context",
            "Rarely — I avoid looking back",
            "Never — once it’s sent, it’s gone"
        ]
    }
]

# Show questions
if st.session_state.current_question < len(questions):
    q = questions[st.session_state.current_question]
    st.markdown(f"### {q['question']}")
    selected = st.radio("Select one:", q["options"], key=f"q{st.session_state.current_question}")
    if st.button("Next"):
        st.session_state.answers.append(selected)
        st.session_state.current_question += 1
        st.rerun()
else:
    st.success("🎉 Test complete! Here's your personality breakdown.")
    st.markdown("**(This is a mock result for demo purposes)**")
    st.markdown("- CID_E: Expressive 3 | Minimalist 1")
    st.markdown("- CID_R: Reactive 2 | Detached 0")
    st.markdown("- CID_A: Analytical 1 | Trusting 3")
    st.markdown("- CID_F: Fast-paced 4 | Patient 0")
    st.markdown("- CID_C: Curated 3 | Free-flowing 2")
    st.markdown("- CID_L: Loud 2 | Neutral 1")
    st.markdown("- CID_e: Empathic 4 | Thick-skinned 2")
    st.markdown("📘 *Want to try again?*")

    if st.button("Restart test"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
