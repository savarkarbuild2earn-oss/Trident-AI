import streamlit as st
from engine import autonomous_whale_scanner
import yfinance as yf
import urllib.parse

# 1. ELITE PRODUCTION ENGINE WORKSPACE VIEWPORT CONFIGURATION
st.set_page_config(
    page_title="Trident-AI Premium Live Terminal", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. MASTER "MINT PROSPERITY" LIGHT UX SKIN INJECTIONS
st.markdown("""
    <style>
    /* Premium High-Contrast Light Canvas Backdrop */
    .stApp { 
        background-color: #ffffff !important; 
        background-image: linear-gradient(180deg, #f0fdf4 0%, #ffffff 100%) !important;
        color: #0f172a !important; 
    }
    
    /* Institutional Emerald-Green Gradient Header */
    .header-panel {
        background: linear-gradient(90deg, #064e3b 0%, #059669 100%);
        padding: 26px;
        border-radius: 16px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(5, 150, 105, 0.15);
    }
    
    /* Glassmorphism White Card Components */
    .scroll-container {
        max-height: 560px !important;
        overflow-y: scroll !important;
        padding: 20px;
        background: #ffffff;
        border-radius: 14px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 20px 0 rgba(148, 163, 184, 0.08);
        margin-bottom: 24px;
    }
    
    /* System Navigation Tab Component Styles */
    button[data-baseweb="tab"] {
        font-size: 15px !important;
        font-weight: 700 !important;
        color: #475569 !important;
        padding: 14px 28px !important;
        background-color: #f8fafc !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px 8px 0 0 !important;
        margin-right: 4px !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #ffffff !important;
        background-color: #059669 !important;
        border-color: #059669 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main Application Title Banner Frame
st.markdown("""
    <div class="header-panel">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h1 style="margin: 0; font-size: 34px; font-weight: 900; letter-spacing: -1px; color: white;">🔱 TRIDENT-AI</h1>
                <p style="margin: 4px 0 0 0; font-family: monospace; font-size: 13px; color: #a7f3d0; font-weight:bold; letter-spacing:0.5px;">[ STATUS: TOTAL AUTOMATED NIFTY 100 MONITOR // LIGHT PROSPERITY THEME ACTIVE ]</p>
            </div>
            <div style="background: rgba(255,255,255,0.2); color: white; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; border: 1px solid rgba(255,255,255,0.4);">
                📡 30s REAL-TIME AUTO-REFRESH
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# SEBI LEGAL DISCLOSURE GUARDFRAIL
st.error(
    "⚠️ **SEBI DISCLOSURE & STATUTORY WARNING:** We are NOT registered with SEBI as an investment advisor or "
    "research analyst. This platform performs automated, algorithmic data stream calculations strictly for "
    "educational market strategy simulations. No certified financial advisory signals are generated here."
)

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("⏱️ Live Indian Stock Market Strategy Board")
st.write("Our multi-agent system runs background verification cycles across the exchange nodes completely hands-free. Use the filters below to monitor target lines:")

# ==============================================================================
# SELF-RUNNING SUB-WORKSPACE MONITOR CORE FRAGMENT (30s REFRESH LOOP)
# ==============================================================================
@st.fragment(run_every=30)
def render_live_segmented_terminal():
    with st.spinner("Processing entire Nifty 100 price matrix streams and syncing live financial news..."):
        df_intra, df_long = autonomous_whale_scanner()

    if df_intra.empty or df_long.empty:
        st.warning("Synchronizing cloud pipeline stream feeds. Re-running asset calculation scanner loop automatically...")
    else:
        # STRATEGY SEPARATIONS TAB CONTROLLER
        tab_intraday, tab_longterm = st.tabs([
            "⚡ REAL-TIME INTRADAY EXECUTIONS (50/50 Split View)", 
            "📈 LONG-TERM POSITION COMPOUNDER (Wide View)"
        ])
        
        with tab_intraday:
            st.subheader("⚡ Live Intraday Data Matrix — All 100 Market Leaders Displayed")
            st.caption("Left Container: Group Alpha (Stocks 1-50) // Right Container: Group Beta (Stocks 51-100)")
            
            # INTRADAY MAINTENANCE: 50/50 Balanced Horizontal Columns Rendering
            col_intra_left, col_intra_right = st.columns(2)
            
            with col_intra_left:
                st.markdown("<b style='color:#064e3b;'>🟢 GROUP ALPHA MARKET TRACKER</b>", unsafe_allow_html=True)
                st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
                # UX UPGRADE: Native sorting & absolute dynamic searching enabled implicitly
                st.dataframe(df_intra.head(50), use_container_width=True, hide_index=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
            with col_intra_right:
                st.markdown("<b style='color:#064e3b;'>🟢 GROUP BETA MARKET TRACKER</b>", unsafe_allow_html=True)
                st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
                st.dataframe(df_intra.tail(50), use_container_width=True, hide_index=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
        with tab_longterm:
            # LONG TERM RE-ENGINEERED: No split groups. Displays as a single wide-page database list.
            st.subheader("📈 Long-Term Positional Valuation Engine — Wide Ledger View")
            st.caption("Features dedicated 24-Hour clock reference logs. Holding durations calculated sequentially into explicit Day Arrays.")
            
            st.markdown('<div class="scroll-container" style="max-height: 580px !important;">', unsafe_allow_html=True)
            # UX UPGRADE: Native sorting & absolute dynamic searching enabled implicitly
            st.dataframe(df_long, use_container_width=True, hide_index=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    
    # ==============================================================================
    # CO-FOUNDER ERGONOMIC ARRANGEMENT: TRADING HOLIDAYS LOCATED AT THE BOTTOM
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
    
    st.caption("Workspace updated. Next automatic data refresh pipeline trigger in 30 seconds.")

# Launch the live "Mint Prosperity" light terminal canvas loop
render_live_segmented_terminal()

st.markdown("---")
st.caption("🔒 Trident-AI Proprietary Automation Architecture. 100% Non-Commercial Educational Simulation Engine.")
