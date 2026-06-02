import streamlit as st
from engine import autonomous_whale_scanner

# Configure premium dynamic layout architecture
st.set_page_config(page_title="Trident-AI Live Quant Suite", layout="wide")

# Institutional Financial Dashboard Theme Injections
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc !important; color: #1e293b !important; }
    .header-panel {
        background: linear-gradient(90deg, #0f172a 0%, #1e3a8a 100%);
        padding: 24px;
        border-radius: 12px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.15);
    }
    .dataframe { border-radius: 8px !important; overflow: hidden !important; }
    </style>
""", unsafe_allow_html=True)

# Main Application Banner
st.markdown("""
    <div class="header-panel">
        <h1 style="margin: 0; font-size: 30px; font-weight: 900; letter-spacing: -0.5px;">🔱 TRIDENT-AI QUANT INTERACTIVE</h1>
        <p style="margin: 4px 0 0 0; font-family: monospace; font-size: 13px; color: #cbd5e1;">[ Status: Fully Autonomous Market Mapping Core Active // 0% Manual Selections Required ]</p>
    </div>
""", unsafe_allow_html=True)

# MANDATORY LEGAL SHIELD DISCLOSURE BANNER
st.error(
    "⚠️ **SEBI DISCLOSURE & STATUTORY WARNING:** We are NOT registered with SEBI as an investment advisor or "
    "research analyst. This platform performs automated, algorithmic data stream calculations strictly for "
    "educational market strategy simulations. No certified financial advisory signals are generated here."
)

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🤖 Live Market Activity & News Confluence Engine")
st.write("The automation engine is actively scanning the exchanges to track down assets displaying massive "
         "buyer/seller transactions right now, processing live news streams, and generating unified signals:")

# Trigger the entire background automation script with zero manual button barriers
with st.spinner("Processing live volume vectors and analyzing real-time financial news RSS streams..."):
    automated_report = autonomous_whale_scanner()

if automated_report.empty:
    st.info("The algorithm completed its workflow loop and found no active anomalies crossing our risk shields. System auto-refreshing shortly.")
else:
    # Present the complete, unedited, automated market execution report cleanly
    st.dataframe(automated_report, use_container_width=True, hide_index=True)

st.markdown("<br><br>", unsafe_allow_html=True)
col_btn, col_empty = st.columns([1, 4])
with col_btn:
    if st.button("🔄 Force Re-Scan Market Volumes"):
        st.rerun()

st.markdown("---")
st.caption("🔒 Trident-AI Proprietary Automation Architecture. 100% Non-Commercial Educational Simulation Engine.")
