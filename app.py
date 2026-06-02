import streamlit as st
from engine import analyze_user_position, optimize_capital_allocation, fetch_index_benchmarks, is_market_open, autonomous_whale_scanner

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
        background: #ffffff; border: 1px solid #e2e8f0; padding: 20px; border-radius: 14px;
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
                <p style="margin: 4px 0 0 0; font-family: monospace; font-size: 13px; color: #a7f3d0; font-weight:bold;">[ STATUS: NIFTY & SENSEX LIVE SCANNERS ACTIVE // ALL RECONCILED STOCKS DEPLOYED ]</p>
            </div>
            <div style="background: rgba(255,255,255,0.2); color: white; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; border: 1px solid rgba(255,255,255,0.4);">
                📡 1-HOUR COMPILER RUNNING
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# SEBI LEGAL DISCLOSURE GUARDFRAIL
st.error("⚠️ **SEBI DISCLOSURE & STATUTORY WARNING:** We are NOT SEBI-registered advisors. All code handles simulated strategy layouts.")

# FETCH DYNAMIC MARKET BENCHMARKS
benchmarks = fetch_index_benchmarks()
col_nifty, col_sensex, col_status = st.columns(3)
with col_nifty: st.metric(label="📈 NIFTY 50 INDEX", value=benchmarks["Nifty50"], delta=f"{benchmarks['NiftyChange']}%")
with col_sensex: st.metric(label="🏛️ BSE SENSEX INDEX", value=benchmarks["Sensex"], delta=f"{benchmarks['SensexChange']}%")
with col_status:
    market_state = "🟢 EXCHANGES OPEN" if is_market_open() else "🔴 EXCHANGES CLOSED"
    st.metric(label="📡 FEED PIPELINE STATUS", value=market_state)

st.markdown("<br>", unsafe_allow_html=True)

# ==============================================================================
# INDEPENDENT AUTO-REFRESH MATRIX FRAGMENT (CALIBRATED TO EVERY 1 HOUR / 3600 SECONDS)
# ==============================================================================
@st.fragment(run_every=3600)
def render_live_segmented_terminal():
    with st.spinner("Processing Nifty & Sensex indices data streams safely..."):
        df_intra, df_long = autonomous_whale_scanner()

    if df_intra.empty or df_long.empty:
        st.warning("Re-running asset calculation scanner loop automatically...")
    else:
        tab_intraday, tab_longterm, tab_user_dashboard = st.tabs([
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
            
        with tab_user_dashboard:
            st.subheader("🛠️ Interactive Allocation and Review Node")
            col_form_left, col_form_right = st.columns(2)
            with col_form_left:
                st.markdown('<div class="user-card">', unsafe_allow_html=True)
                st.write("##### 💼 Active Position Review Module")
                user_stock = st.text_input("Enter stock ticker symbol:", "RELIANCE")
                user_action = st.selectbox("Select your position posture:", ["Holding", "Buying", "Selling"])
                if st.button("🔍 Fetch AI Review"):
                    st.info(f"**Trident-AI Analyst Feedback:** {analyze_user_position(user_stock, user_action)}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown('<div class="user-card">', unsafe_allow_html=True)
                st.write("##### 📦 Brokerage Integration Router")
                broker_select = st.selectbox("Which brokerage platform do you use?", ["Zerodha (Kite)", "Groww", "AngelOne", "Upstox", "Other"])
                st.success(f"💡 Custom Guidance Track Optimized for **{broker_select}** terminal execution structures.")
                st.markdown('</div>', unsafe_allow_html=True)
            with col_form_right:
                st.markdown('<div class="user-card">', unsafe_allow_html=True)
                st.write("##### 💰 Capital Allocation & Strategy Sizer")
                capital_input = st.number_input("How much capital (INR) are you looking to allocate today?", min_value=5000, value=50000, step=5000)
                if st.button("⚡ Calculate Optimal Diversification"):
                    st.write("###### 🤖 Recommended Capital Split Matrix for Today:")
                    st.table(optimize_capital_allocation(capital_input))
                st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.info(
        "📆 **UPCOMING LIVE NSE TRADING HOLIDAYS RISK MONITOR (REMAINDER OF 2026 CALENDAR CYCLE):**\n"
        "*   **Bakri Id (Id-Ul-Zuha)**: Wednesday, June 17, 2026\n"
        "*   **Independence Day**: Saturday, August 15, 2026\n"
        "*   **Mahatma Gandhi Jayanti**: Friday, October 02, 2026\n"
        "*   **Diwali (Laxmi Puja)**: Sunday, November 08, 2026 *(Special 1-Hour Muhurat Trading session in evening)*\n"
        "*   **Gurunanak Jayanti**: Monday, November 23, 2026\n"
        "*   **Christmas**: Friday, December 25, 2026"
    )
    st.caption("Workspace updated. Next automatic data refresh pipeline trigger in 1 hour.")

# Launch the live "Mint Prosperity" light terminal canvas loop
render_live_segmented_terminal()
