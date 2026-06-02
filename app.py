import streamlit as st
from engine import scan_stock
import yfinance as yf
import urllib.parse

# 1. VISUAL ENGINE LAYOUT CONFIGURATION
st.set_page_config(
    page_title="🔱 TRIDENT-AI // Institutional Quant Terminal", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. CYBERPUNK GLASSMORPHISM INFRASTRUCTURE
st.markdown("""
    <style>
    /* Global Canvas Dark Mode Override */
    .stApp {
        background-color: #030712 !important;
        background-image: radial-gradient(circle at 50% 0%, #1e1b4b 0%, #030712 70%) !important;
        color: #f3f4f6 !important;
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    }
    
    /* Neon Frosted Glassmorphism Containers */
    .quant-panel {
        background: rgba(17, 24, 39, 0.7) !important;
        backdrop-filter: blur(16px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        margin-bottom: 24px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .quant-panel:hover {
        border-color: rgba(99, 102, 241, 0.4) !important;
        box-shadow: 0 12px 40px 0 rgba(99, 102, 241, 0.15) !important;
        transform: translateY(-2px);
    }
    
    /* Sleek Institutional Metric Font Typography */
    div[data-testid="stMetricValue"] {
        font-size: 36px !important;
        font-weight: 800 !important;
        color: #6366f1 !important;
        letter-spacing: -1px;
        text-shadow: 0 0 12px rgba(99, 102, 241, 0.4);
    }
    
    /* Hyper-Premium Glowing Tactical Execution Control */
    .stButton>button {
        background: linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        letter-spacing: 0.5px !important;
        border: none !important;
        padding: 16px 32px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 20px rgba(79, 70, 229, 0.4) !important;
        transition: all 0.2s ease-in-out !important;
        width: 100%;
        text-transform: uppercase;
    }
    .stButton>button:hover {
        box-shadow: 0 0 30px rgba(79, 70, 229, 0.7) !important;
        transform: translateY(-1px);
    }
    
    /* Custom Stylings for Selectboxes and System Tabs */
    .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important;
    }
    button[data-baseweb="tab"] {
        font-size: 14px !important;
        font-weight: 600 !important;
        color: #9ca3af !important;
        padding: 12px 24px !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #6366f1 !important;
        border-bottom-color: #6366f1 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. HIGH-END CYBER FINTECH HEADER HERO CARD
st.markdown("""
    <div class="quant-panel" style="border-left: 6px solid #6366f1; background: linear-gradient(90deg, rgba(79,70,229,0.1) 0%, rgba(17,24,39,0.7) 100%) !important;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h1 style="color:#ffffff; margin:0; font-size:36px; font-weight:900; letter-spacing:-1px;">🔱 TRIDENT-AI</h1>
                <p style="color:#9ca3af; margin:4px 0 0 0; font-family:monospace; font-size:13px; letter-spacing:1px;">⚡ [ ALGORITHMIC DATA ENGINE CORE v2.5 ]</p>
            </div>
            <div style="text-align: right;">
                <span style="background: rgba(99,102,241,0.2); color: #a5b4fc; padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; border: 1px solid rgba(99,102,241,0.3);">🟢 EXCHANGE DATA LIVE</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# SEBI REGULATORY COMPLIANCE SYSTEM GUARD
with st.expander("⚖️ SECURE LEGAL ARCHITECTURE DIRECTIVE & SEBI COMPLIANCE SHIELD", expanded=False):
    st.markdown("""
        <div style="font-size:12px; color:#9ca3af; line-height:1.6; padding:10px; background: rgba(0,0,0,0.2); border-radius:8px;">
            <strong>MANDATORY STATUTORY WARNING:</strong> We are <strong>NOT</strong> registered with SEBI as an investment advisor or research analyst. 
            This quantitative suite operations engine functions entirely as a decentralized, non-commercial software calculation simulator for educational modeling purposes. 
            No financial advice is given, and past metrics hold zero validation toward prospective price curves. Always protect capital through certified wealth advisors.
        </div>
    """, unsafe_allow_html=True)

# Session Allocation Initializations
if 'virtual_wallet' not in st.session_state:
    st.session_state.virtual_wallet = 1000000.00
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = {}  
if 'active_ticker' not in st.session_state:
    st.session_state.active_ticker = None
if 'active_strategy' not in st.session_state:
    st.session_state.active_strategy = "Swing"

st.markdown("<br>", unsafe_allow_html=True)

# TOP ROW: SECURE SANDBOX BALANCES CARD
col_balance_card, col_spacing = st.columns(2)
with col_balance_card:
    st.markdown('<div class="quant-panel" style="padding: 16px 24px !important;">', unsafe_allow_html=True)
    st.metric(label="💰 SANDBOX SIMULATION LEDGER", value=f"₹{st.session_state.virtual_wallet:,.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

# CENTRAL OPERATION: CONTROL PARAMETERS
st.markdown('<div class="quant-panel">', unsafe_allow_html=True)
st.markdown("<h3 style='color:white; margin-top:0; margin-bottom:15px; font-size:18px;'>⚙️ CONFIGURATION ENGINE RADAR</h3>", unsafe_allow_html=True)
col_inputs, col_timeframe = st.columns(2)

stock_dictionary = {
    "Reliance Industries (RELIANCE)": "RELIANCE.NS",
    "State Bank of India (SBIN)": "SBIN.NS",
    "Tata Consultancy Services (TCS)": "TCS.NS",
    "HDFC Bank (HDFCBANK)": "HDFCBANK.NS",
    "Infosys (INFY)": "INFY.NS",
    "ICICI Bank (ICICIBANK)": "ICICIBANK.NS",
    "ITC Limited (ITC)": "ITC.NS",
    "Larsen & Toubro (LT)": "LT.NS",
    "Tata Motors (TATAMOTORS)": "TATAMOTORS.NS",
    "Bharti Airtel (BHARTIALRT)": "BHARTIALRT.NS",
    "Adani Ports (ADANIPORTS)": "ADANIPORTS.NS",
    "NTPC Limited (NTPC)": "NTPC.NS",
    "Power Grid Corporation (POWERGRID)": "POWERGRID.NS",
    "Oil & Natural Gas Corp (ONGC)": "ONGC.NS",
    "Coal India (COALINDIA)": "COALINDIA.NS",
    "Indian Railway Finance Corp (IRFC)": "IRFC.NS",
    "Indian Renewable Energy Dev Agency (IREDA)": "IREDA.NS",
    "Suzlon Energy (SUZLON)": "SUZLON.NS",
    "Zomato Limited (ZOMATO)": "ZOMATO.NS",
    "Tata Steel (TATASTEEL)": "TATASTEEL.NS",
    "Jio Financial Services (JIOFIN)": "JIOFIN.NS"
}

with col_inputs:
    selected_stock_label = st.selectbox("📊 SELECT TARGET NSE STOCK MATRIX:", list(stock_dictionary.keys()))
    formatted_ticker = stock_dictionary[selected_stock_label]
with col_timeframe:
    strategy_select = st.selectbox("⚡ SELECT MOMENTUM HORIZON EXECUTION:", ["Swing / Long-Term Investing", "Intraday Trading Momentum"])

chosen_mode = "Intraday" if "Intraday" in strategy_select else "Swing"

st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 INITIALIZE DUAL-HORIZON DIAGNOSTIC LOOP"):
    st.session_state.active_ticker = formatted_ticker
    st.session_state.active_strategy = chosen_mode
st.markdown('</div>', unsafe_allow_html=True)

# ANALYSIS OUTPUT GRID
if st.session_state.active_ticker:
    current_ticker = st.session_state.active_ticker
    current_mode = st.session_state.active_strategy
    
    result = scan_stock(current_ticker, current_mode)
    
    if result is None:
        st.error("System Core Interrupted: Price stream connection timed out. Please retry.")
        st.session_state.active_ticker = None
    elif result["status"] == "BLOCKED":
        st.error(f"⚠️ Security Shield Lockout: {result['reason']}")
        st.session_state.active_ticker = None
    elif result["status"] == "SUCCESS":
        
        beginner_tab, pro_tab, paper_trade_tab, leaderboard_tab = st.tabs([
            "🟢 STRATEGY BIAS SCANNER", 
            "🔵 INSTITUTIONAL CONFLUENCE", 
            "🎮 SANDBOX ORDER ROUTER",
            "🏆 GLOBAL SYSTEM LEADERBOARD"
        ])
        
        with beginner_tab:
            st.markdown('<div class="quant-panel">', unsafe_allow_html=True)
            st.markdown(f"<h2 style='color:#ffffff; font-weight:700; font-size:22px; margin-top:0;'>Bias Analysis Direction: {result['decision']}</h2>", unsafe_allow_html=True)
            
            st.write(f"**Trident Confluence Index Score:** {result['raw_score']}/100")
            st.progress(result['raw_score'] / 100)
            
            # FIXED INDENTATION SPACING LOOPS HERE
            if result['raw_score'] >= 75:
                st.markdown("<div style='background:rgba(16,185,129,0.1); color:#34d399; padding:15px; border-radius:8px; border:1px solid rgba(16,185,129,0.2); font-size:14px; margin-bottom:20px;'><strong>🔥 CONFLUENCE RATING CRITICAL:</strong> Multiple tracking agents have mapped out strong buyer support structures with minimal distribution trends. Setup matches institutional criteria.</div>", unsafe_allow_html=True)
            elif 40 <= result['raw_score'] < 74:
