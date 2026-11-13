import streamlit as st

st.set_page_config(page_title="SignConnect AI", layout="wide")

# RAINBOW HEADER
st.markdown(
"<div style='background:linear-gradient(90deg,#FF6B6B,#FFA500,#FFD93D,#6BCB77,#4D96FF,#9B5DE5);"
"padding:25px;border-radius:18px;text-align:center;color:white'>"
"<h1>SignConnect AI</h1>"
"<p>Smart Accessibility Platform</p>"
"<p>Telugu - English - Hindi - Kannada</p></div>",
unsafe_allow_html=True)

if "s" not in st.session_state:
    st.session_state.s = ""
if "p" not in st.session_state:
    st.session_state.p = "Home"

st.markdown("### Explore Our 6 Features")

# 6 CARDS
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("#### 🎤 Speech to Text")
    st.write("Spoken words to text")
    if st.button("Try Feature", key="b1"):
        st.session_state.p = "Speech to Text"
        st.rerun()
with c2:
    st.markdown("#### ✋ Sign to Text")
    st.write("Hand signs to text")
    if st.button("Try Feature", key="b2"):
        st.session_state.p = "Sign to Text"
        st.rerun()
with c3:
    st.markdown("#### 🧩 Sentence Builder")
    st.write("Build sentences easily")
    if st.button("Try Feature", key="b3"):
        st.session_state.p = "Sentence Builder"
        st.rerun()

d1, d2, d3 = st.columns(3)
with d1:
    st.markdown("#### 🔊 Text to Speech")
    st.write("Text to clear speech")
    if st.button("Try Feature", key="b4"):
        st.session_state.p = "Text to Speech"
        st.rerun()
with d2:
    st.markdown("#### 🌐 Multi Language")
    st.write("Telugu, Hindi, Kannada")
    if st.button("Try Feature", key="b5"):
        st.session_state.p = "Multi Language"
        st.rerun()
with d3:
    st.markdown("#### 📚 Learning Mode")
    st.write("Learn A-Z signs")
    if st.button("Try Feature", key="b6"):
        st.session_state.p = "Learning Mode"
        st.rerun()

st.info("Current Sentence: " + st.session_state.s)
if st.button("Clear Sentence"):
    st.session_state.s = ""
    st.rerun()

pg = st.session_state.p

# 1
if pg == "Speech to Text":
    st.markdown("## 🎤 Speech to Text")
    au = st.audio_input("Record chey")
    if au:
        st.success("Audio record ayyindi!")
    t = st.text_input("Maata type chey")
    if st.button("Add to Sentence", key="s1"):
        st.session_state.s += " " + t
        st.rerun()

# 2
elif pg == "Sign to Text":
    st.markdown("## ✋ Sign to Text")
    pic = st.camera_input("Sign chupinchi photo theey")
    if pic:
        st.success("Photo vachindi!")
    sg = st.selectbox("Sign", ["HELLO","THANK YOU","YES","NO","PLEASE","HELP","LOVE"])
    if st.button("Add Sign", key="s2"):
        st.session_state.s += " " + sg
        st.rerun()

# 3
elif pg == "Sentence Builder":
    st.markdown("## 🧩 Sentence Builder")
    words = ["I","YOU","WANT","NEED","WATER","FOOD","HELP","PLEASE","HELLO","GO"]
    cols = st.columns(5)
    for i, w in enumerate(words):
        if cols[i % 5].button(w, key=f"w{i}"):
            st.session_state.s += " " + w
            st.rerun()

# 4
elif pg == "Text to Speech":
    st.markdown("## 🔊 Text to Speech")
    txt = st.text_input("Text", st.session_state.s)
    if st.button("Convert to Speech", key="s4"):
        try:
            from gtts import gTTS
            import io
            b = io.BytesIO()
            gTTS(txt, lang="en").write_to_fp(b)
            b.seek(0)
            st.audio(b, format="audio/mp3")
            st.success("Speech ready!")
        except:
            st.error("Terminal lo: pip install gtts")

# 5
elif pg == "Multi Language":
    st.markdown("## 🌐 Multi Language")
    lang = st.selectbox("Language", ["Telugu","Hindi","Kannada","English"])
    D = {
        "HELLO": {"Telugu":"Namaste","Hindi":"Namaste","Kannada":"Namaskara","English":"Hello"},
        "THANK YOU": {"Telugu":"Dhanyavadalu","Hindi":"Dhanyavad","Kannada":"Dhanyavadagalu","English":"Thank You"},
        "YES": {"Telugu":"Avunu","Hindi":"Haan","Kannada":"Howdu","English":"Yes"},
        "NO": {"Telugu":"Kadu","Hindi":"Nahi","Kannada":"Illa","English":"No"},
        "HELP": {"Telugu":"Sahayam","Hindi":"Madad","Kannada":"Sahaya","English":"Help"},
        "WATER": {"Telugu":"Neellu","Hindi":"Paani","Kannada":"Neeru","English":"Water"},
        "FOOD": {"Telugu":"Annam","Hindi":"Khana","Kannada":"Oota","English":"Food"},
    }
    w2 = st.selectbox("Word", list(D.keys()))
    st.markdown(f"### {w2} = {D[w2][lang]}")
    if st.button("Add Translation", key="s5"):
        st.session_state.s += " " + D[w2][lang]
        st.rerun()

# 6 - Learning Mode
elif pg == "Learning Mode":
    st.markdown("## 📚 Learning Mode")
    S = {"A":"Fist close","B":"Fingers straight","C":"C shape","D":"Index paina","E":"Fingers curl","F":"Index+Thumb circle","G":"Index+Thumb munduku","H":"Index+Middle munduku","I":"Chinna finger paina","J":"J rayi","K":"Index+Middle paina","L":"L shape","M":"3 fingers thumb meedha","N":"2 fingers thumb meedha","O":"O shape","P":"K kindhaki","Q":"G kindhaki","R":"Cross","S":"Fist thumb mundu","T":"Thumb madhya","U":"Index+Middle kalipi","V":"V shape","W":"3 fingers paina","X":"Hook","Y":"Thumb+Chinna finger","Z":"Z rayi"}
    L = st.selectbox("Letter", list(S.keys()))
    st.markdown(f"### {L} - {S[L]}")
    if st.button("Add Letter", key="s6"):
        st.session_state.s += " " + L
        st.rerun()