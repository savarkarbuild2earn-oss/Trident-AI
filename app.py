import streamlit as st
from engine import autonomous_whale_scanner

# Configure wide institutional theme viewport canvas layout
st.set_page_config(page_title="Trident-AI Live Quant Terminal", layout="wide")

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
    /* ENFORCE VERTICAL SCROLLBAR WRAPPER LAYOUT DESIGN */
    .scroll-container {
        max-height: 500px !important;
        overflow-y: scroll !important;
        padding: 15px;
        background: #ffffff;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Main Application Banner Frame
st.markdown("""
    <div class="header-panel">
        <h1 style="margin: 0; font-size: 32px; font-weight: 900; letter-spacing: -0.5px;">🔱 TRIDENT-AI QUANT TERMINAL</h1>
        <p style="margin: 4px 0 0 0; font-family: monospace; font-size: 13px; color: #cbd5e1;">[ Status: Nifty 100 50/50 Balanced Matrix Active // Auto-Streaming 30s Loop ]</p>
    </div>
""", unsafe_allow_html=True)

# LEGAL COMPLIANCE GUARDFRAIL
st.error(
    "⚠️ **SEBI DISCLOSURE & STATUTORY WARNING:** We are NOT registered with SEBI as an investment advisor or "
    "research analyst. This platform performs automated, algorithmic data stream calculations strictly for "
    "educational market strategy simulations. No certified financial advisory signals are generated here."
)

# REFRESHED TRADING HOLIDAYS RISK MONITOR
st.info(
    "📆 **UPCOMING LIVE NSE TRADING HOLIDAYS (2026 CYCLE):**\n"
    "*   **Bakri Id (Id-Ul-Zuha)**: Wednesday, June 17, 2026\n"
    "*   **Independence Day**: Saturday, August 15, 2026\n"
    "*   **Mahatma Gandhi Jayanti**: Friday, October 02, 2026\n"
    "*   **Diwali (Laxmi Puja)**: Sunday, November 08, 2026 *(Special 1-Hour Muhurat Trading session)*\n"
    "*   **Gurunanak Jayanti**: Monday, November 23, 2026\n"
    "*   **Christmas**: Friday, December 25, 2026"
)

st.markdown("<br>", unsafe_allow_html=True)

# ==============================================================================
# SELF-RUNNING REFRESH TERMINAL WORKSPACE FRAGMENT
# ==============================================================================
@st.fragment(run_every=30)
def render_live_segmented_terminal():
    with st.spinner("Compiling entire Nifty 100 price matrix streams safely..."):
        df_intra, df_long = autonomous_whale_scanner()

    if df_intra.empty or df_long.empty:
        st.warning("Synchronizing cloud pipeline stream feeds. Re-running asset calculation scanner loop automatically...")
    else:
        # CHOOSE HORIZON SEPARATIONS VIA TABS
        tab_intraday, tab_longterm = st.tabs([
            "⚡ REAL-TIME INTRADAY SECTOR EXECUTIONS", 
            "📈 LONG-TERM ASCENDING COMPOUNDER LEDGER"
        ])
        
        with tab_intraday:
            st.subheader("⚡ Nifty 100 Live Intraday Stream — Split Layout Feed")
            st.caption("Left Panel: Group Alpha (Stocks 1-50) // Right Panel: Group Beta (Stocks 51-100)")
            
            col_intra_left, col_intra_right = st.columns(2)
            
            with col_intra_left:
                st.markdown("##### 🛡️ GROUP ALPHA MARKET TRACKER")
                # Wrap dataframe inside html div to lock height and force the vertical scrollbar
                st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
                st.dataframe(df_intra.head(50), use_container_width=True, hide_index=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
            with col_intra_right:
                st.markdown("##### 🛡️ GROUP BETA MARKET TRACKER")
                st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
                st.dataframe(df_intra.tail(50), use_container_width=True, hide_index=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
        with tab_longterm:
            st.subheader("📈 Macro Long-Term Value Maturation Board — Split Layout Feed")
            st.caption("Holding periods scale sequentially in ascending order starting straight from 1 Month")
            
            col_long_left, col_long_right = st.columns(2)
            
            with col_long_left:
                st.markdown("##### 💎 GROUP ALPHA VALUE MARGINS")
                st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
                st.dataframe(df_long.head(50), use_container_width=True, hide_index=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
            with col_long_right:
                st.markdown("##### 💎 GROUP BETA VALUE MARGINS")
                st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
                st.dataframe(df_long.tail(50), use_container_width=True, hide_index=True)
                st.markdown('</div>', unsafe_allow_html=True)

    st.caption("Full grid workspace recalculated cleanly. Next automated 30s loop re-run initiated.")

# Run the live dual horizontal split loop grid layout
render_live_segmented_terminal()

st.markdown("---")
st.caption("🔒 Trident-AI Proprietary Automation Architecture. 100% Non-Commercial Educational Simulation Engine.")
