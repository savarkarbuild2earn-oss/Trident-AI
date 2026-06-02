import streamlit as st
from engine import autonomous_whale_scanner

# Configure wide responsive fin-tech layout format
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
                <p style="margin: 4px 0 0 0; font-family: monospace; font-size: 13px; color: #cbd5e1;">[ Status: Fully Autonomous Market Mapping Core Active // Auto-Streaming 30s Loop ]</p>
            </div>
            <div style="text-align: right;">
                <div class="pulse-indicator">📡 LIVE MULTI-HORIZON SCANNER RUNNING</div>
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

# ==============================================================================
# CO-FOUNDER INTEGRATION: UPCOMING NSE HOLIDAY RISK ENGINE
# ==============================================================================
st.info(
    "📆 **UPCOMING NSE TRADING HOLIDAYS ALERT (2026):** "
    "Please plan your simulation allocations accordingly. The National Stock Exchange (NSE) will remain closed on:\n"
    "*   **Bakri Id (Id-Ul-Zuha)**: Wednesday, October 28, 2026\n"
    "*   **Diwali (Laxmi Puja)**: Sunday, November 08, 2026 *(Special 1-Hour Muhurat Trading session will open in evening)*\n"
    "*   **Gurunanak Jayanti**: Monday, November 23, 2026\n"
    "*   **Christmas**: Friday, December 25, 2026\n"
    "⚠️ *Intraday positions are strictly barred from rolling over into market holidays to avoid liquidity shocks.*"
)

st.markdown("<br>", unsafe_allow_html=True)

# ==============================================================================
# SELF-RUNNING REFRESH FRAGMENT COMPONENT
# ==============================================================================
@st.fragment(run_every=30)
def render_segregated_workspace_feeds():
    with st.spinner("Processing market streams and updating target execution time windows..."):
        df_intraday, df_longterm = autonomous_whale_scanner()

    if df_intraday.empty or df_longterm.empty:
        st.info("The algorithm completed its workflow loop and found no active assets crossing our risk shields right now.")
    else:
        tab_intraday, tab_longterm = st.tabs([
            "⚡ INTRADAY MOMENTUM MONITOR (High Speed)", 
            "📈 LONG-TERM WEALTH COMPOUNDER (Macro Valuation)"
        ])
        
        with tab_intraday:
            st.subheader("⚡ Live Time-Stamped Intraday Execution Feed")
            st.write("Ensure all trades align with the daily session window. Targets refresh automatically every 30 seconds:")
            st.dataframe(df_intraday, use_container_width=True, hide_index=True)
            
        with tab_longterm:
            st.subheader("📈 Macro Fair-Value Long Term Allocation Board")
            st.write("Bypasses short-term pricing noise to evaluate macro target lines and safe compounding holding durations:")
            st.dataframe(df_longterm, use_container_width=True, hide_index=True)
            
    st.caption("Last full market time-horizon sync completed successfully. Next automatic scan in 30 seconds.")

# Trigger our self-running frontend fragment container loop
render_segregated_workspace_feeds()

st.markdown("---")
st.caption("🔒 Trident-AI Proprietary Automation Architecture. 100% Non-Commercial Educational Simulation Engine.")
