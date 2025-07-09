
import streamlit as st

st.set_page_config(page_title="Digital Personality Test", page_icon="🧠", layout="centered")

# ========== APP STATE ==========
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "scores" not in st.session_state:
    st.session_state.scores = {
        "CID_E": {"E": 0, "M": 0},
        "CID_R": {"R": 0, "D": 0},
        "CID_A": {"A": 0, "T": 0},
        "CID_F": {"F": 0, "P": 0},
        "CID_C": {"C": 0, "F2": 0},
        "CID_L": {"L": 0, "N": 0},
        "CID_e": {"e": 0, "t": 0},
    }
if "finished" not in st.session_state:
    st.session_state.finished = False

# ========== QUESTIONS & MAPPINGS ==========

questions = [
    {
        "text": "How do you feel when someone sends you a long voice note?",
        "type": "single",
        "options": {
            "Excited! I love hearing people explain in detail.": [("CID_E", "E", 1)],
            "Fine, I’ll usually listen and maybe skim.": [("CID_E", "E", 0.5)],
            "Annoyed — I wish they’d text instead.": [("CID_E", "M", 1)],
            "I often skip them entirely.": [("CID_E", "M", 1)],
        }
    },
    {
        "text": "How do you usually save contacts on your phone?",
        "type": "single",
        "options": {
            "Full name, formal.": [("CID_C", "C", 1)],
            "Nicknames or funny names.": [("CID_C", "F2", 1)],
            "Just first names.": [("CID_C", "F2", 0.5)],
        }
    },
    # ... Add 26 more questions here following same structure ...
]

# ========== FUNCTIONS ==========

def show_question(index):
    q = questions[index]
    st.subheader(f"Q{index+1}: {q['text']}")
    if q["type"] == "single":
        selected = st.radio("Select one:", list(q["options"].keys()), key=index)
        if st.button("Next"):
            for cid, pole, pts in q["options"][selected]:
                st.session_state.scores[cid][pole] += pts
            st.session_state.current_q += 1
            if st.session_state.current_q >= len(questions):
                st.session_state.finished = True
                st.experimental_rerun()

def show_results():
    st.success("🎉 Test complete! Here's your personality breakdown.")
    st.markdown("**(This is a mock result for demo purposes)**")
    final_code = ""
    for cid, poles in st.session_state.scores.items():
        poles_sorted = sorted(poles.items(), key=lambda x: -x[1])
        main_pole = poles_sorted[0][0]
        final_code += main_pole
        st.markdown(f"- **{cid}**: {poles_sorted[0][0]} {poles_sorted[0][1]} | {poles_sorted[1][0]} {poles_sorted[1][1]}")

    personality_names = {
        "ERATFIL": "The Echo Reactor",
        "DMTPCNe": "The Detached Observer",
        "ERAFCLe": "Unique Blend",
    }
    name = personality_names.get(final_code, "Unique Blend")
    st.markdown(f"### 🔍 Your digital personality type: **{name}** ({final_code})")
    st.markdown("_A special digital personality profile._")

    if st.button("Restart test"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()

# ========== MAIN LOGIC ==========

st.title("🧠 Digital Personality Test")

if not st.session_state.finished:
    show_question(st.session_state.current_q)
else:
    show_results()
