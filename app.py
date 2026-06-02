import streamlit as st
from engine import autonomous_whale_scanner

# 1. ELITE ENGINE WORKSPACE VIEWPORT CONFIGURATION
st.set_page_config(page_title="Trident-AI Live Quant Terminal", layout="wide")

# 2. MASTER UX LIGHT THEME STYLE OVERRIDES
st.markdown("""
    <style>
    /* Premium High-Contrast Light Canvas Backdrop */
    .stApp { 
        background-color: #f8fafc !important; 
        background-image: linear-gradient(180deg, #eff6ff 0%, #f8fafc 100%) !important;
        color: #1e293b !important; 
    }
    /* Institutional Blue-Slate Header Configuration */
    .header-panel {
        background: linear-gradient(90deg, #0f172a 0%, #1e3a8a 100%);
        padding: 24px;
        border-radius: 12px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.15);
    }
    /* Elite Locked-Height Vertical Scrollbar Containers */
    .scroll-container {
        max-height: 520px !important;
        overflow-y: scroll !important;
        padding: 16px;
        background: #ffffff;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Main Application Title Banner
st.markdown("""
    <div class="header-panel">
        <h1 style="margin: 0; font-size: 32px; font-weight: 900; letter-spacing: -0.5px;">🔱 TRIDENT-AI QUANT SUPER-TERMINAL</h1>
        <p style="margin: 4px 0 0 0; font-family: monospace; font-size: 13px; color: #cbd5e1;">[ Status: Multi-Horizon Automated Array Scanner Pool Active // Auto-Streaming 30s Loop ]</p>
    </div>
""", unsafe_allow_html=True)

# SEBI LEGAL DISCLOSURE GUARD
st.error(
    "⚠️ **SEBI DISCLOSURE & STATUTORY WARNING:** We are NOT registered with SEBI as an investment advisor or "
    "research analyst. This platform performs automated, algorithmic data stream calculations strictly for "
    "educational market strategy simulations. No certified financial advisory signals are generated here."
)

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("⏱️ Live Indian Stock Market Automation Grid")
st.write("This grid monitors and scans the market list automatically every **30 seconds**. Use the search filters on the tables to instantly slice through assets:")

# ==============================================================================
# SELF-RUNNING SUB-WORKSPACE MONITOR CORE FRAGMENT
# ==============================================================================
@st.fragment(run_every=30)
def render_live_segmented_terminal():
    with st.spinner("Compiling entire Nifty price matrix streams safely..."):
        df_intra, df_long = autonomous_whale_scanner()

    if df_intra.empty or df_long.empty:
        st.warning("Synchronizing cloud pipeline stream feeds. Re-running asset calculation scanner loop automatically...")
    else:
        # STRATEGY SEPARATIONS TAB BAR
        tab_intraday, tab_longterm = st.tabs([
            "⚡ REAL-TIME INTRADAY SECTOR EXECUTIONS (Split Grid)", 
            "📈 LONG-TERM ASCENDING COMPOUNDER LEDGER (Full Grid View)"
        ])
        
        with tab_intraday:
            st.subheader("⚡ Live Intraday Data Matrix — Split Layout Feed")
            st.caption("Left Panel: Group Alpha (Stocks 1-50) // Right Panel: Group Beta (Stocks 51-100)")
            
            # INTRADAY MAINTENANCE: 50/50 Balanced Horizontal Columns
            col_intra_left, col_intra_right = st.columns(2)
            
            with col_intra_left:
                st.markdown("##### 🛡️ GROUP ALPHA MARKET TRACKER")
                st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
                st.dataframe(df_intra.head(12), use_container_width=True, hide_index=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
            with col_intra_right:
                st.markdown("##### 🛡️ GROUP BETA MARKET TRACKER")
                st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
                st.dataframe(df_intra.tail(12), use_container_width=True, hide_index=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
        with tab_longterm:
            # LONG TERM SYSTEM REDESIGN: No alpha/beta columns. Renders as an absolute full-page display grid.
            st.subheader("📈 Macro Long-Term Value Board — Wide View")
            st.caption("Features dedicated 24-Hour calculation timestamps with holding periods starting from 1 Month in clean ascending order.")
            
            st.markdown('<div class="scroll-container" style="max-height: 560px !important;">', unsafe_allow_html=True)
            st.dataframe(df_long, use_container_width=True, hide_index=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    
    # ==============================================================================
    # ERGONOMIC POSITION SHIFT: UPCOMING NSE TRADING HOLIDAYS DISPLAYED AT THE BOTTOM
    # ==============================================================================
    st.info(
        "📆 **UPCOMING LIVE NSE TRADING HOLIDAYS RISK MONITOR (REMAINDER OF 2026 CALENDAR CYCLE):**\n"
        "*   **Bakri Id (Id-Ul-Zuha)**: Wednesday, June 17, 2026\n"
        "*   **Independence Day**: Saturday, August 15, 2026\n"
        "*   **Mahatma Gandhi Jayanti**: Friday, October 02, 2026\n"
        "*   **Diwali (Laxmi Puja)**: Sunday, November 08, 2026 *(Special 1-Hour Muhurat Trading session will open in evening)*\n"
        "*   **Gurunanak Jayanti**: Monday, November 23, 2026\n"
        "*   **Christmas**: Friday, December 25, 2026"
    )
    
    st.caption("Full grid workspace recalculated cleanly. Next automated 30s loop re-run initiated.")

# Run our premium light institutional terminal canvas
render_live_segmented_terminal()

st.markdown("---")
st.caption("🔒 Trident-AI Proprietary Automation Architecture. 100% Non-Commercial Educational Simulation Engine.")
