import streamlit as st
import pandas as pd

# 1. वार-रूम थीम और सजावट
st.set_page_config(page_title="Bullmoney Commander", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffd700; }
    .stSelectbox, .stButton { border: 2px solid #ffd700; border-radius: 10px; }
    .card { border: 2px solid #ffd700; padding: 20px; border-radius: 15px; background: #1c1c1c; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Bullmoney: रोहित का साम्राज्य")

# 2. कूटनीति के 5 वादे (Sidebar)
with st.sidebar:
    st.header("🔑 कूटनीति के 5 वादे")
    st.info("1. डेटा की शुद्धता 🛡️\n2. 10-लेयर की छलनी 🔍\n3. पारस पत्थर की खोज 💎\n4. व्यापारिक समझ 🛠️\n5. सिर्फ टॉप 25 की सेना ⚔️")

# 3. सेक्टर लिस्ट (Finology के मुख्य सेक्टर्स)
sectors = [
    "Aerospace & Defense", "Automobiles", "Banking", "Chemicals", 
    "IT - Software", "Railways", "Textiles", "Green Energy"
]
selected_sector = st.selectbox("🎯 घेराबंदी के लिए सेक्टर चुनें:", sectors)

# 4. 10-लेयर कूटनीति इंजन
def apply_10_layers(co):
    score = 0
    # L1: कर्ज (Debt to Equity)
    if co['debt'] < 1: score += 1
    # L2: सच्ची कीमत (Graham Value)
    intrinsic = co['eps'] * (8.5 + 2 * co['growth'])
    if co['price'] < (intrinsic * 0.7): score += 2
    # L3: प्रमोटर होल्डिंग
    if co['promoter'] > 50: score += 1
    
    status = "💎 पारस पत्थर" if score >= 3 else "❌ रिजेक्ट"
    return status, intrinsic

# 5. डमी डेटा और आपका 'सिंपल फॉर्मूला'
# यहाँ हम असली Finology डेटा की नकल कर रहे हैं
data = [
    {'name': 'Jupiter Wagons', 'price': 350, 'eps': 18, 'growth': 22, 'debt': 0.1, 'promoter': 70, 'work': 'वंदे भारत के ब्रेक और वेगन बनाना।'},
    {'name': 'RVNL', 'price': 240, 'eps': 12, 'growth': 15, 'debt': 0.8, 'promoter': 78, 'work': 'रेलवे इंफ्रास्ट्रक्चर प्रोजेक्ट्स।'}
]

st.subheader(f"⚔️ {selected_sector} की टॉप 25 सेना")

# आपका फॉर्मूला: 25 से ज्यादा पर फिल्टर, कम पर सब
if len(data) > 25:
    st.warning(f"⚠️ {len(data)} कंपनियाँ मिलीं। 10-लेयर फिल्टर से टॉप 25 चुनी जा रही हैं।")
    # यहाँ टॉप 25 सॉर्टिंग लॉजिक लगेगा
else:
    st.success(f"✅ यहाँ {len(data)} कंपनियाँ हैं। सबका विश्लेषण हाजिर है।")

for co in data:
    decision, iv = apply_10_layers(co)
    with st.container():
        st.markdown(f"""<div class='card'>
            <h3>🏢 {co['name']}</h3>
            <p><b>🛠️ काम:</b> {co['work']}</p>
            <p><b>💰 मूल्य:</b> ₹{co['price']} | <b>📉 Graham Value:</b> ₹{iv:.2f}</p>
            <p><b>🛡️ निर्णय:</b> {decision}</p>
        </div>""", unsafe_allow_html=True)
        
