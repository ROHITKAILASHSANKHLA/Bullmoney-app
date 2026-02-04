import streamlit as st

# इंटरफेस और स्वागत संदेश
st.set_page_config(page_title="Bullmoney Dashboard", layout="wide")
st.markdown("<h1 style='text-align: center; color: gold;'>🛡️ Bullmoney कमान केंद्र</h1>", unsafe_allow_html=True)
st.write("### नमस्ते रोहित! 👋 आपकी 10-लेयर कूटनीति अब लाइव है।")

# सेक्टोरल डेटा और काम की जानकारी
companies = [
    {'name': 'ABC_Rail_Tech', 'sector': 'Railways', 'price': 150, 'eps': 20, 'growth': 12, 'debt': 0.2, 'work': 'यह कंपनी वंदे भारत के लिए हाई-स्पीड ब्रेक बनाती है।'},
    {'name': 'Gear_Master_India', 'sector': 'Auto_Parts', 'price': 500, 'eps': 10, 'growth': 5, 'debt': 1.5, 'work': 'यह कंपनी भारी ट्रकों के लिए गियर बॉक्स बनाती है।'}
]

# सेक्टर चुनने का बटन
sector = st.selectbox("📂 किस सेक्टर की घेराबंदी करनी है?", ["Railways", "Auto_Parts", "Castings"])

# कूटनीति कैलकुलेटर इंजन
for co in companies:
    if co['sector'] == sector:
        with st.expander(f"📍 कंपनी: {co['name']} (पूरा विवरण)"):
            intrinsic = co['eps'] * (8.5 + 2 * co['growth'])
            buy_limit = intrinsic * 0.7
            
            st.write(f"**L2&3 (Graham Value):** ₹{intrinsic:.2f} | **Buy Below:** ₹{buy_limit:.2f}")
            st.write(f"**Layer 1 (Debt):** {'✅ मजबूत' if co['debt'] < 1 else '❌ कमजोर'} (Ratio: {co['debt']})")
            st.info(f"**🛠️ कंपनी का काम:** {co['work']}")
            
            if co['price'] <= buy_limit and co['debt'] < 1:
                st.success("💎 निर्णय: पारस पत्थर")
            else:
                st.error("❌ निर्णय: रिजेक्ट")
              
