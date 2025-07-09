
import streamlit as st

# -------------------------------
# Digital Personality Test Engine
# -------------------------------

st.set_page_config(page_title="Digital Personality Test", layout="centered")
st.markdown("## 🧠 Digital Personality Test")

# Define questions and answers (sample of 6)
questions = [
    {
        "text": "How do you feel when someone sends you a long voice note?",
        "options": [
            ("Excited! I love hearing people explain in detail.", {"CID_E": ("E", 1)}),
            ("Fine, I’ll usually listen and maybe skim.", {"CID_E": ("E", 0.5)}),
            ("Annoyed — I wish they’d text instead.", {"CID_E": ("M", 1)}),
            ("I often skip them entirely.", {"CID_E": ("M", 2)})
        ],
        "multi": False
    },
    {
        "text": "When someone doesn't reply quickly, how do you feel?",
        "options": [
            ("Worried something's wrong.", {"CID_R": ("R", 1), "CID_e": ("e", 1)}),
            ("Curious, but I don’t overthink it.", {"CID_R": ("R", 0.5)}),
            ("Indifferent — I probably didn’t notice.", {"CID_R": ("D", 1)}),
            ("I’ll double-text or send a meme.", {"CID_R": ("R", 1.5)})
        ],
        "multi": False
    },
    {
        "text": "Do you usually edit a text for spelling or grammar after sending it?",
        "options": [
            ("Yes, always.", {"CID_A": ("A", 1)}),
            ("Only if it's formal.", {"CID_A": ("A", 0.5)}),
            ("No, I just leave it as is.", {"CID_A": ("T", 1)}),
            ("Only if it was a big mistake.", {"CID_A": ("T", 0.5)})
        ],
        "multi": False
    },
    {
        "text": "How fast do you typically reply to non-urgent messages?",
        "options": [
            ("Immediately — I can’t let them wait.", {"CID_F": ("F", 1)}),
            ("Pretty quickly, if I see it.", {"CID_F": ("F", 0.5)}),
            ("When I have time later.", {"CID_F": ("P", 1)}),
            ("It depends — I don’t track time much.", {"CID_F": ("P", 0.5)})
        ],
        "multi": False
    },
    {
        "text": "What best describes your posting style on social media?",
        "options": [
            ("Curated, edited, carefully crafted.", {"CID_C": ("C", 1)}),
            ("Mostly spontaneous and fun.", {"CID_C": ("F", 1)}),
            ("Rare — I mostly watch, not post.", {"CID_C": ("C", 0.5)}),
            ("I use stories more than posts.", {"CID_C": ("F", 0.5)})
        ],
        "multi": False
    },
    {
        "text": "Do you ever reread your old conversations or messages?",
        "options": [
            ("Yes — I like revisiting fun exchanges.", {"CID_e": ("e", 1)}),
            ("Only if I’m unsure about something.", {"CID_A": ("A", 0.5)}),
            ("No — the past is the past.", {"CID_e": ("t", 1)}),
            ("Yes — it helps me reflect.", {"CID_e": ("e", 1)})
        ],
        "multi": False
    }
]

# Core Interactions & Results Definitions
personality_archetypes = {
    "ERATFIL": {
        "label": "The Echo Reactor",
        "description": "Emotionally sensitive, reactive, and expressive. Needs digital warmth to feel at ease.",
    },
    "MDTPNTe": {
        "label": "The Ghost Shell",
        "description": "Minimalist, detached, patient, and thick-skinned. You prefer silence over buzz."
    }
}

# Descriptions for each CID pole
cid_descriptions = {
    "CID_E": {"E": "Expressive", "M": "Minimalist"},
    "CID_R": {"R": "Reactive", "D": "Detached"},
    "CID_A": {"A": "Analytical", "T": "Trusting"},
    "CID_F": {"F": "Fast-paced", "P": "Patient"},
    "CID_C": {"C": "Curated", "F": "Free-flowing"},
    "CID_L": {"L": "Loud", "N": "Neutral"},
    "CID_e": {"e": "Empathic", "t": "Thick-skinned"},
}

# --- App State ---
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.scores = {
        "CID_E": {"E": 0, "M": 0},
        "CID_R": {"R": 0, "D": 0},
        "CID_A": {"A": 0, "T": 0},
        "CID_F": {"F": 0, "P": 0},
        "CID_C": {"C": 0, "F": 0},
        "CID_L": {"L": 0, "N": 0},
        "CID_e": {"e": 0, "t": 0}
    }

# --- Main Logic ---
if st.session_state.question_index < len(questions):
    q = questions[st.session_state.question_index]
    st.markdown(f"### Q{st.session_state.question_index + 1}: {q['text']}")
    selected = st.radio("Select one:", [opt[0] for opt in q["options"]], index=None)

    if st.button("Next") and selected:
        for opt_text, effects in q["options"]:
            if opt_text == selected:
                for cid, (pole, pts) in effects.items():
                    st.session_state.scores[cid][pole] += pts
        st.session_state.question_index += 1
        st.rerun()
else:
    st.success("🎉 Test complete! Here's your personality breakdown.")
    st.markdown("### (This is a mock result for demo purposes)")

    code = ""
    for cid, poles in st.session_state.scores.items():
        sorted_poles = sorted(poles.items(), key=lambda x: x[1], reverse=True)
        top = sorted_poles[0][0]
        second = sorted_poles[1][0]
        code += top
        st.write(
            f"- **{cid}**: {cid_descriptions[cid][top]} {poles[top]} | {cid_descriptions[cid][second]} {poles[second]}"
        )

    label = personality_archetypes.get(code, {}).get("label", "Unique Blend")
    desc = personality_archetypes.get(code, {}).get("description", "A special digital personality profile.")
    st.markdown(f"### 🔎 Your digital personality type: **{label}** (`{code}`)")
    st.markdown(f"*{desc}*")

    st.markdown("___")
    if st.button("Restart test"):
        for k in ["question_index", "scores"]:
            del st.session_state[k]
        st.rerun()
