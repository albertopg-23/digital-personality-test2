
import streamlit as st

# ----------------------------
# Data: Full question structure
# ----------------------------
questions = [
    {
        "question": "How do you feel when someone sends you a long voice note?",
        "type": "single",
        "options": {
            "Excited! I love hearing people explain in detail.": {"CID3_A": 2, "CID7_Re": 1},
            "Fine, I’ll usually listen and maybe skim.": {"CID3_A": 1},
            "Annoyed — I wish they’d text instead.": {"CID3_T": 2},
            "I often skip them entirely.": {"CID3_T": 3}
        }
    },
    {
        "question": "Do you listen to your own voice notes after sending them?",
        "type": "single",
        "options": {
            "Always, to check how I sound.": {"CID7_Re": 3, "CID5_F": 1},
            "Sometimes.": {"CID7_Re": 2},
            "Rarely or never.": {"CID7_Dt": 2}
        }
    },
    {
        "question": "How do you usually react when someone sends you a meme or a reel?",
        "type": "single",
        "options": {
            "React immediately or reply with something funny.": {"CID2_R": 2, "CID4_F": 1},
            "Just like it, maybe react with an emoji.": {"CID2_R": 1},
            "I laugh but don’t reply.": {"CID2_D": 2},
            "Ignore them.": {"CID2_D": 3}
        }
    },
    {
        "question": "Which of the following reflects your sticker or emoji style best?",
        "type": "single",
        "options": {
            "I love animated GIFs or weird animal stickers.": {"CID5_C": 2},
            "I use expressive emojis all the time.": {"CID5_C": 1},
            "I keep it minimal – maybe just a thumbs-up.": {"CID5_F": 2},
            "No stickers or emojis for me.": {"CID5_F": 3}
        }
    },
    {
        "question": "How often do you delete or redo stories/posts?",
        "type": "single",
        "options": {
            "Frequently, I’m always tweaking my posts.": {"CID7_Re": 3, "CID1_E": 1},
            "Sometimes, if something feels off.": {"CID7_Re": 2},
            "Hardly ever, I just let it be.": {"CID7_Dt": 2},
            "Never. Once it's up, it's up.": {"CID7_Dt": 3}
        }
    },
    {
        "question": "How do you name people in your contacts?",
        "type": "single",
        "options": {
            "Funny nicknames or emojis.": {"CID5_C": 2},
            "Something descriptive (e.g., 'Laura Uni Class').": {"CID6_L": 2},
            "Full formal names.": {"CID6_L": 3, "CID5_F": 1}
        }
    }
]

# Personality cluster names
personality_clusters = {
    "ERATFIL": "The Echo Reactor",
    "EMATFIL": "The Filtered Flow",
    "ERATFNL": "The Calm Reactor",
    "EMDTFNL": "The Minimalist Observer",
    # Default cluster
    "default": "The Digital Chameleon"
}

# ----------------------------
# State initialization
# ----------------------------
if 'index' not in st.session_state:
    st.session_state.index = 0
    st.session_state.scores = {
        "CID1_E": 0, "CID1_M": 0,
        "CID2_R": 0, "CID2_D": 0,
        "CID3_T": 0, "CID3_A": 0,
        "CID4_F": 0, "CID4_P": 0,
        "CID5_C": 0, "CID5_F": 0,
        "CID6_L": 0, "CID6_N": 0,
        "CID7_Re": 0, "CID7_Dt": 0
    }
    st.session_state.finished = False

# ----------------------------
# Main logic
# ----------------------------
st.title("🧠 Digital Personality Test")

if not st.session_state.finished:
    q = questions[st.session_state.index]
    st.subheader(f"Q{st.session_state.index + 1}: {q['question']}")
    if q["type"] == "single":
        choice = st.radio("Select one:", list(q["options"].keys()))
    else:
        choice = st.multiselect("Select all that apply:", list(q["options"].keys()))

    if st.button("Next"):
        if isinstance(choice, str):
            choice = [choice]
        for c in choice:
            impacts = q["options"][c]
            for k, v in impacts.items():
                st.session_state.scores[k] += v
        st.session_state.index += 1
        if st.session_state.index >= len(questions):
            st.session_state.finished = True
        # Removed deprecated st.experimental_rerun()

else:
    st.header("🎉 Your Digital Personality Result")

    # Construct personality code
    final_code = ""
    result_pairs = [("CID1_E", "CID1_M"), ("CID2_R", "CID2_D"), ("CID3_T", "CID3_A"),
                    ("CID4_F", "CID4_P"), ("CID5_C", "CID5_F"), ("CID6_L", "CID6_N"),
                    ("CID7_Re", "CID7_Dt")]
    for a, b in result_pairs:
        final_code += a[-1] if st.session_state.scores[a] >= st.session_state.scores[b] else b[-1]

    # Find matching cluster
    main_type = personality_clusters.get(final_code, personality_clusters["default"])

    # Display summary
    st.subheader(f"✨ You are: **{main_type}**")
    st.write("Your overall digital personality shows how you interact emotionally, socially, and structurally with the online world.")

    st.markdown(f"**Your Code:** `{final_code}`")

    # Display CID scores and dominant poles
    st.write("---")
    st.subheader("Your Personality Breakdown")
    for a, b in result_pairs:
        score_a = st.session_state.scores[a]
        score_b = st.session_state.scores[b]
        dominant = a[-1] if score_a >= score_b else b[-1]
        st.write(f"**CID{a[4]}**: {dominant} ({a[-1]}: {score_a} | {b[-1]}: {score_b})")

    st.success("You can now share your personality type with others or retake the test!")
