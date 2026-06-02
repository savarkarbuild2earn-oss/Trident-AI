import streamlit as st
from engine import autonomous_whale_scanner

st.set_page_config(page_title="Trident-AI Streaming Terminal", layout="wide")

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
    .pulse-indicator {
        background: rgba(16, 185, 129, 0.2);
        color: #047857;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        border: 1px solid rgba(16, 185, 129, 0.4);
        display: inline-block;
        animation: blinker 2s linear infinite;
    }
    @keyframes blinker {
        50% { opacity: 0.5; }
    }
    </style>
""", unsafe_allow_html=True)

# Main Application Banner
st.markdown("""
    <div class="header-panel">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h1 style="margin: 0; font-size: 30px; font-weight: 900; letter-spacing: -0.5px;">🔱 TRIDENT-AI QUANT INTERACTIVE</h1>
                <p style="margin: 4px 0 0 0; font-family: monospace; font-size: 13px; color: #cbd5e1;">[ Status: Fully Autonomous Market Mapping Core Active ]</p>
            </div>
            <div style="text-align: right;">
                <div class="pulse-indicator">📡 LIVE SCANNER AUTO-STREAMING</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# MANDATORY LEGAL SHIELD DISCLOSURE BANNER
st.error(
    "⚠️ **SEBI DISCLOSURE & STATUTORY WARNING:** We are NOT registered with SEBI as an investment advisor or "
    "research analyst. This platform performs automated, algorithmic data stream calculations strictly for "
    "educational market strategy simulations. No certified financial advisory signals are generated here."
)

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("⏱️ Live Dynamic Execution Matrix Feed")
st.write("This section updates itself automatically every **30 seconds**. Watch the execution timestamps and target bounds adjust hands-free:")

# ==============================================================================
# CO-FOUNDER UPDATED: 30-SECOND REFRESH FRAGMENT
# ==============================================================================
@st.fragment(run_every=30)
def render_live_streaming_feed():
    with st.spinner("Refreshing price structures and streaming live volumes..."):
        automated_report = autonomous_whale_scanner()

    if automated_report.empty:
        st.info("The algorithm completed its workflow loop and found no active anomalies crossing our risk shields. System auto-refreshing shortly.")
    else:
        st.dataframe(automated_report, use_container_width=True, hide_index=True)
    
    st.caption("Last data pipeline sweep compiled successfully. Next automatic stream refresh in 30 seconds.")

# Trigger our self-running frontend fragment container loop
render_live_streaming_feed()

st.markdown("---")
st.caption("🔒 Trident-AI Proprietary Automation Architecture. 100% Non-Commercial Educational Simulation Engine.")
