import streamlit as st
from engine import analyze_user_position, fetch_top_10_active_momentum_stocks, fetch_index_benchmarks, is_market_open, autonomous_index_scanner
import yfinance as yf
from datetime import datetime
import pytz

# 1. ELITE PRODUCTION ENGINE WORKSPACE VIEWPORT CONFIGURATION
st.set_page_config(page_title="Trident-AI Premium Live Terminal", layout="wide", initial_sidebar_state="collapsed")

# 2. MASTER "MINT PROSPERITY" LIGHT UX SKIN INJECTIONS
st.markdown("""
    <style>
    .stApp { 
        background-color: #ffffff !important; 
        background-image: linear-gradient(180deg, #f0fdf4 0%, #ffffff 100%) !important;
        color: #0f172a !important; 
    }
    .header-panel {
        background: linear-gradient(90deg, #064e3b 0%, #059669 100%);
        padding: 26px; border-radius: 16px; color: white; margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(5, 150, 105, 0.15);
    }
    .scroll-container {
        max-height: 450px !important; overflow-y: scroll !important; padding: 20px;
        background: #ffffff; border-radius: 14px; border: 1px solid #e2e8f0;
        box-shadow: 0 4px 20px 0 rgba(148, 163, 184, 0.08); margin-bottom: 24px;
    }
    .user-card {
        background: #ffffff; border: 1px solid #e2e8f0; padding: 22px; border-radius: 14px;
        box-shadow: 0 4px 15px rgba(148, 163, 184, 0.05); margin-bottom: 20px;
    }
    button[data-baseweb="tab"] {
        font-size: 15px !important; font-weight: 700 !important; color: #475569 !important;
        padding: 14px 28px !important; background-color: #f8fafc !important;
        border: 1px solid #e2e8f0 !important; border-radius: 8px 8px 0 0 !important; margin-right: 4px !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #ffffff !important; background-color: #059669 !important; border-color: #059669 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main Application Title Banner Frame
st.markdown("""
    <div class="header-panel">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h1 style="margin: 0; font-size: 34px; font-weight: 900; letter-spacing: -1px; color: white;">🔱 TRIDENT-AI</h1>
                <p style="margin: 4px 0 0 0; font-family: monospace; font-size: 13px; color: #a7f3d0; font-weight:bold;">[ STATUS: UNIFIED MARKET AUTOMATION TERMINAL // ALL STOCKS ACTIVE ]</p>
            </div>
            <div style="background: rgba(255,255,255,0.2); color: white; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; border: 1px solid rgba(255,255,255,0.4);">
                📡 AUTOMATED 09:15 AM SYNC
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# SEBI LEGAL DISCLOSURE GUARDFRAIL
st.error("⚠️ **SEBI DISCLOSURE & STATUTORY WARNING:** We are NOT registered with SEBI as an investment advisor or research analyst. All metrics simulate educational strategies.")

# FETCH DYNAMIC INDEX TRACKERS
benchmarks = fetch_index_benchmarks()
col_nifty, col_sensex, col_status = st.columns(3)
with col_nifty: st.metric(label="📈 NIFTY 50 INDEX", value=benchmarks["Nifty50"], delta="+0.43%")
with col_sensex: st.metric(label="🏛️ BSE SENSEX INDEX", value=benchmarks["Sensex"], delta="+0.52%")
with col_status:
    market_state = "🟢 EXCHANGES OPEN" if is_market_open() else "🔴 EXCHANGES CLOSED"
    st.metric(label="📡 FEED PIPELINE STATUS", value=market_state)

st.markdown("<br>", unsafe_allow_html=True)

# INITIALIZE PORTFOLIO STATE STORAGE
if 'user_portfolio' not in st.session_state:
    st.session_state.user_portfolio = []

# ==============================================================================
# UNIFIED OPENING BELL REFRESH CONTAINER LOOPS
# ==============================================================================
@st.fragment(run_every=60)
def process_synchronized_terminal_grid():
    df_intra, df_long = autonomous_index_scanner()
    top_10_stocks = fetch_top_10_active_momentum_stocks()

    # ==============================================================================
    # DYNAMIC BLUEPRINT REFERENCE: PROFESSIONAL TRADER'S DAILY TIMELINE GUIDE
    # ==============================================================================
    with st.expander("📖 PROFESSIONAL TRADER'S MASTER STRATEGY BLUEPRINT & TIMELINE BOOK", expanded=True):
        st.markdown("""
        ### ⏱️ Core Daily Operational Schedules
        *   **07:30 AM | Monitor GIFT Nifty:** Analyze price structures on the NSE International Exchange (NSE IX) to establish macro opening bias vectors.
        *   **08:00 AM | Review Institutional Flows:** Inspect previous session FII / DII net turnover aggregates to determine underlying directional bias.
        *   **08:30 AM | Filter Corporate News:** Scan systemic alerts on the corporate announcements board for corporate actions or earnings revisions.
        *   **09:00 AM | Pre-Open Session Metrics:** Track institutional price clustering (09:00 - 09:08 AM) and pin a high-momentum 3-stock watch target grid.
        *   **09:15 AM | Open Range Breakout (ORB):** Execute execution breakouts over high-volume parameters from the initial 15-minute range boundary line.
        *   **09:45 AM | Options Scalping Engine:** Ride velocity surges near-the-money options using an exponential moving average crossing trigger.
        *   **11:00 AM | Avoid Mid-Day Chop:** Scale sizing down. Protect cash capital pools from horizontal sideways chop and option theta distribution decay.
        *   **12:30 PM | European Markets Cross:** Track FTSE & DAX opening moves to capture macro algorithms switching directional trends locally.
        *   **01:00 PM | Open Interest (OI) Chain Scan:** Identify hard multi-strike target floors (Put Open Interest) and ceiling resistances (Call Open Interest).
        *   **02:00 PM | Hero-or-Zero Expiry Strategy:** Stagger speculative allocation weights into low-premium index option lines specifically on expiry sessions.
        *   **03:15 PM | Forced Squaring Off:** Clear all intraday simulation postures to preserve sandbox currency metrics securely.
        *   **03:40 PM | Post-Market Adjustments:** Verify closing weighted averages and audit Peak Margin bounds to comply with regulatory shields.
        *   **05:00 PM | Delivery Volume Filtering:** Identify small and mid-cap assets logging extreme delivery percentages to lock in short-term swing trading targets.
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    # RENDER STRATEGY WORKSPACE VIEWS
    tab_intraday, tab_longterm, tab_command_console = st.tabs([
        "⚡ REAL-TIME INTRADAY EXECUTIONS (50/50 Split View)", 
        "📈 LONG-TERM POSITION COMPOUNDER (Wide View)",
        "💼 FOUNDER STRATEGY COMMAND CONSOLE"
    ])
    
    with tab_intraday:
        st.subheader("⚡ Live Intraday Data Matrix — Complete Nifty & Sensex Assets Deployed")
        col_intra_left, col_intra_right = st.columns(2)
        with col_intra_left:
            st.markdown("<b style='color:#064e3b;'>🟢 GROUP ALPHA MARKET TRACKER (Stocks 1-26)</b>", unsafe_allow_html=True)
            st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
            st.dataframe(df_intra.head(26), use_container_width=True, hide_index=True)
            st.markdown('</div>', unsafe_allow_html=True)
        with col_intra_right:
            st.markdown("<b style='color:#064e3b;'>🟢 GROUP BETA MARKET TRACKER (Stocks 27-52)</b>", unsafe_allow_html=True)
            st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
            st.dataframe(df_intra.tail(26), use_container_width=True, hide_index=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
    with tab_longterm:
        st.subheader("📈 Long-Term Positional Valuation Engine — All Nifty & Sensex Assets (Wide View)")
        st.markdown('<div class="scroll-container" style="max-height: 520px !important;">', unsafe_allow_html=True)
        st.dataframe(df_long, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with tab_command_console:
        st.subheader("🛠️ Founder Strategic Execution & Portfolio Console")
        col_form_left, col_form_right = st.columns(2)
        
        with col_form_left:
            st.markdown('<div class="user-card">', unsafe_allow_html=True)
            st.write("##### 💼 Multi-Stock Active Portfolio Ledger Scanner")
            
            col_ticker_in, col_posture_in = st.columns(2)
            with col_ticker_in:
                input_symbol = st.text_input("Enter Asset Ticker (e.g., RELIANCE, TCS, SBIN):", "RELIANCE").strip().upper()
            with col_posture_in:
                input_posture = st.selectbox("Select Target Posture Condition:", ["Holding", "Buying", "Selling"])
                
            if st.button("💾 Add Position to saved Portfolio Ledger"):
                if input_symbol and {"ticker": input_symbol, "posture": input_posture} not in st.session_state.user_portfolio:
                    st.session_state.user_portfolio.append({"ticker": input_symbol, "posture": input_posture})
                    st.success(f"Successfully pinned {input_symbol} into ledger.")
                    st.rerun()
            
            if st.session_state.user_portfolio:
                if st.button("🗑️ Clear saved Ledger Data"):
                    st.session_state.user_portfolio = []
                    st.rerun()
                    
            st.markdown("---")
            st.write("📂 **Your Current Active Saved Portfolio Strategy Reports:**")
            if not st.session_state.user_portfolio:
                st.caption("Your saved asset ledger is empty. Add positions above to view strategy logs.")
            else:
                # ABSOLUTE SPACING REPAIR: Fixed loop block alignment permanently
                for item in st.session_state.user_portfolio:
