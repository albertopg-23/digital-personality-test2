
import streamlit as st

# Title
st.markdown("# 🧠 Digital Personality Test")

# All CID dimensions and poles
CIDs = {
    "E": ("Expressive", "Minimalist"),
    "R": ("Reactive", "Detached"),
    "A": ("Timely", "Asynchronous"),
    "F": ("Fast-paced", "Paced"),
    "C": ("Coordinated", "Fragmented"),
    "L": ("Loud", "Neutral"),
    "e": ("Engaged", "Thick-skinned")
}

# State initialization
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = []
if "scores" not in st.session_state:
    st.session_state.scores = {cid: [0, 0] for cid in CIDs}  # [Pole1, Pole2]

# Questionnaire
questions = [
    {
        "q": "How do you feel when someone sends you a long voice note?",
        "type": "single",
        "options": [
            ("Excited! I love hearing people explain in detail.", {"E": (1, 0)}),
            ("Fine, I’ll usually listen and maybe skim.", {"E": (0.5, 0.5)}),
            ("Annoyed — I wish they’d text instead.", {"E": (0, 1)}),
            ("I often skip them entirely.", {"E": (0, 1)})
        ]
    },
    {
        "q": "How quickly do you usually reply to non-urgent messages?",
        "type": "single",
        "options": [
            ("Within a few minutes, even if I'm busy.", {"A": (1, 0)}),
            ("When I’m free — usually same day.", {"A": (0.7, 0.3)}),
            ("A day or two later. I don’t rush.", {"A": (0.3, 0.7)}),
            ("Sometimes I forget completely.", {"A": (0, 1)})
        ]
    }
]

# Display question
if st.session_state.step < len(questions):
    qdata = questions[st.session_state.step]
    st.subheader(f"Q{st.session_state.step + 1}: {qdata['q']}")
    selected = st.radio("Select one:", [opt[0] for opt in qdata["options"]], key=st.session_state.step)

    if st.button("Next"):
        for opt_text, impacts in qdata["options"]:
            if selected == opt_text:
                for cid, (p1, p2) in impacts.items():
                    st.session_state.scores[cid][0] += p1
                    st.session_state.scores[cid][1] += p2
        st.session_state.step += 1
        st.rerun()

# Final result
else:
    st.markdown("## Your Personality Breakdown")
    for cid, (pole1, pole2) in CIDs.items():
        score1, score2 = st.session_state.scores[cid]
        st.markdown(f"**{cid}** — **{pole1} vs {pole2}**")
        st.write(f"- {pole1}: {score1:.1f}")
        st.write(f"- {pole2}: {score2:.1f}")
        if score1 > score2:
            st.success(f"You lean toward **{pole1}**")
        elif score2 > score1:
            st.warning(f"You lean toward **{pole2}**")
        else:
            st.info(f"Balanced between **{pole1}** and **{pole2}**")

    st.markdown("---")
    st.markdown("🔁 [Restart Test](#)", unsafe_allow_html=True)
