import streamlit as st
from engine import autonomous_whale_scanner

st.set_page_config(page_title="Trident-AI Market Terminal", layout="wide")

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
                <h1 style="margin: 0; font-size: 30px; font-weight: 900; letter-spacing: -0.5px;">🔱 TRIDENT-AI COMPREHENSIVE MARKET TERMINAL</h1>
                <p style="margin: 4px 0 0 0; font-family: monospace; font-size: 13px; color: #cbd5e1;">[ Status: Market-Wide Automated Scanner Pool Active // Auto-Streaming 30s Loop ]</p>
            </div>
            <div style="text-align: right;">
                <div class="pulse-indicator">📡 SCANNING ENTIRE NSE NIFTY 100</div>
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
st.subheader("⏱️ Live Indian Stock Market Automation Grid")
st.write("This grid monitors and scans the entire market list automatically every **30 seconds**. Use the search bar on the table to instantly find any stock or strategy segment:")

# ==============================================================================
# SELF-RUNNING REFRESH CONTAINER COMPONENT
# ==============================================================================
@st.fragment(run_every=30)
def render_live_streaming_feed():
    with st.spinner("Compiling full-market price metrics and syncing multi-agent sentiment arrays..."):
        automated_report = autonomous_whale_scanner()

    if automated_report.empty:
        st.info("The algorithm completed its workflow loop and found no active assets crossing our risk shields right now.")
    else:
        # ADVANCED UX INTEGRATION: Interactive searchable data grid with instant filtering
        st.dataframe(
            automated_report, 
            use_container_width=True, 
            hide_index=True,
            column_config={
                "🧬 Scoring Index": st.column_config.ProgressColumn(
                    "🧬 Scoring Index",
                    help="Unified Multi-Agent Confluence Weighting Score",
                    format="%s",
                    min_value=0,
                    max_value=100,
                )
            }
        )
    
    st.caption("Entire NSE market pool processed successfully. Next automatic workflow re-run in 30 seconds.")

# Launch the live interactive data fragment frame
render_live_streaming_feed()

st.markdown("---")
st.caption("🔒 Trident-AI Proprietary Automation Architecture. 100% Non-Commercial Educational Simulation Engine.")
