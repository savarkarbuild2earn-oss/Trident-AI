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
        max-height: 560px !important; overflow-y: scroll !important; padding: 20px;
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
                <p style="margin: 4px 0 0 0; font-family: monospace; font-size: 13px; color: #a7f3d0; font-weight:bold;">[ STATUS: UNIFIED MARKET AUTOMATION TERMINAL // ALL COMPONENTS OUTWARD FIXED ]</p>
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
with col_nifty: st.metric(label="📈 NIFTY 50 INDEX", value=benchmarks["Nifty50"], delta=f"{benchmarks['NiftyChange']}%")
with col_sensex: st.metric(label="🏛️ BSE SENSEX INDEX", value=benchmarks["Sensex"], delta=f"{benchmarks['SensexChange']}%")
with col_status:
    market_state = "🟢 EXCHANGES OPEN" if is_market_open() else "🔴 EXCHANGES CLOSED"
    st.metric(label="📡 FEED PIPELINE STATUS", value=market_state)

st.markdown("<br>", unsafe_allow_html=True)

# INITIALIZE PORSTFOLIO AND ALGO MATRIX RESERVES
if 'user_portfolio' not in st.session_state:
    st.session_state.user_portfolio = [] 
if 'cached_df_intra' not in st.session_state:
    st.session_state.cached_df_intra = None
if 'cached_df_long' not in st.session_state:
    st.session_state.cached_df_long = None
if 'cached_top_10' not in st.session_state:
    st.session_state.cached_top_10 = None

# ==============================================================================
# UNIFIED OPENING BELL REFRESH FRAGMENT CONTAINER
# ==============================================================================
@st.fragment(run_every=60)
def process_synchronized_terminal_grid():
    ist_tz = pytz.timezone('Asia/Kolkata')
    now_time = datetime.now(ist_tz)
    is_opening_bell = (now_time.hour == 9 and now_time.minute == 15)
    
    if st.session_state.cached_df_intra is None or st.session_state.cached_df_long is None or st.session_state.cached_top_10 is None:
        with st.spinner("Compiling unified daily baseline data streams safely..."):
            st.session_state.cached_df_intra, st.session_state.cached_df_long = autonomous_index_scanner()
            st.session_state.cached_top_10 = fetch_top_10_active_momentum_stocks()
            
    if is_opening_bell:
        st.session_state.cached_df_intra, st.session_state.cached_df_long = autonomous_index_scanner()
        st.session_state.cached_top_10 = fetch_top_10_active_momentum_stocks()
        st.toast("🔔 Opening bell triggered! Complete workspace, counters, and review nodes auto-refreshed successfully.")

    df_intra = st.session_state.cached_df_intra
    df_long = st.session_state.cached_df_long
    top_10_stocks = st.session_state.cached_top_10

    # RENDER STRATEGY VIEWS
    tab_intraday, tab_longterm, tab_command_console = st.tabs([
        "⚡ REAL-TIME INTRADAY EXECUTIONS (50/50 Split View)", 
        "📈 LONG-TERM POSITION COMPOUNDER (Wide View)",
        "💼 FOUNDER STRATEGY COMMAND CONSOLE"
    ])
    
    with tab_intraday:
        st.subheader("⚡ Live Intraday Data Matrix — Nifty & Sensex Combined Assets")
        st.caption("Left Container: Group Alpha (Index Stocks 1-25) // Right Container: Group Beta (Index Stocks 26-50)")
        col_intra_left, col_intra_right = st.columns(2)
        with col_intra_left:
            st.markdown("<b style='color:#064e3b;'>🟢 GROUP ALPHA MARKET TRACKER</b>", unsafe_allow_html=True)
            st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
            st.dataframe(df_intra.head(25), use_container_width=True, hide_index=True)
            st.markdown('</div>', unsafe_allow_html=True)
        with col_intra_right:
            st.markdown("<b style='color:#064e3b;'>🟢 GROUP BETA MARKET TRACKER</b>", unsafe_allow_html=True)
            st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
            st.dataframe(df_intra.tail(25), use_container_width=True, hide_index=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
    with tab_longterm:
        st.subheader("📈 Long-Term Positional Valuation Engine — Wide Ledger View")
        st.caption("Features dedicated 24-Hour clock reference logs. Holding durations calculated sequentially into explicit Day Arrays.")
        st.markdown('<div class="scroll-container" style="max-height: 580px !important;">', unsafe_allow_html=True)
        st.dataframe(df_long, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with tab_command_console:
        st.subheader("🛠️ Founder Strategic Execution & Portfolio Console")
        st.caption("This entire interactive interface space updates and synchronizes with the data scanner automatically at market open.")
        
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
                st.caption("Your saved asset ledger is empty. Add a position above to compute strategy report logs down here.")
            else:
                for item in st.session_state.user_portfolio:
                    report_analysis = analyze_user_position(item["ticker"], item["posture"])
                    st.info(f"Asset: **{item['ticker']}** | Posture: **{item['posture']}**\n\n👉 *Strategy Action:* {report_analysis}")
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col_form_right:
            st.markdown('<div class="user-card">', unsafe_allow_html=True)
            st.write("##### 📊 Capital Allocation & Momentum Sizer (Unrestricted)")
            capital_input = st.number_input("Input total cash amount (INR) to deploy across today's active volume metrics:", min_value=1, value=50000, step=1000)
            
            st.write("###### 🤖 Automated Capital Diversification Breakdown:")
            st.caption("Calculated across the top 10 highest-volume stocks dynamically extracted by the analyzer today:")
            
            split_allocation_data = []
            per_stock_capital = capital_input / 10
