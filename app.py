import streamlit as st
from engine import scan_stock
import yfinance as yf
import urllib.parse

# 1. VISUAL ENGINE LAYOUT CONFIGURATION
st.set_page_config(
    page_title="🔱 TRIDENT-AI // Live Stock Analytics Terminal", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. DYNAMIC FINANCIAL BLUEPRINT DESIGN INJECTIONS
st.markdown("""
    <style>
    /* Global Canvas Institutional Refresh */
    .stApp {
        background-color: #f8fafc !important;
        background-image: linear-gradient(180deg, #eff6ff 0%, #f8fafc 100%) !important;
        color: #1e293b !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Institutional Premium Trading Cards */
    .trade-panel {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: 0 4px 15px 0 rgba(148, 163, 184, 0.1) !important;
        border-radius: 12px !important;
        padding: 24px !important;
        margin-bottom: 24px !important;
        transition: all 0.2s ease-in-out;
    }
    .trade-panel:hover {
        box-shadow: 0 10px 25px 0 rgba(148, 163, 184, 0.2) !important;
        border-color: #cbd5e1 !important;
    }
    
    /* Premium Financial Typography */
    div[data-testid="stMetricValue"] {
        font-size: 38px !important;
        font-weight: 800 !important;
        color: #0f172a !important;
        letter-spacing: -1px;
    }
    
    /* High-Contrast Interactive Execution Controller */
    .stButton>button {
        background: linear-gradient(135deg, #059669 0%, #10b981 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        border: none !important;
        padding: 14px 28px !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2) !important;
        transition: all 0.2s ease !important;
        width: 100%;
        text-transform: uppercase;
    }
    .stButton>button:hover {
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.35) !important;
        transform: translateY(-1px);
    }
    
    /* Custom Stylings for System Input Boxes & Navigation Elements */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 6px !important;
    }
    button[data-baseweb="tab"] {
        font-size: 14px !important;
        font-weight: 600 !important;
        color: #64748b !important;
        padding: 12px 24px !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #059669 !important;
        border-bottom-color: #059669 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. PREMIUM BULL RUN HEADER BANNER
st.markdown("""
    <div class="trade-panel" style="border-left: 6px solid #10b981; background: linear-gradient(90deg, rgba(16,185,129,0.06) 0%, #ffffff 100%) !important;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h1 style="color:#0f172a; margin:0; font-size:32px; font-weight:900; letter-spacing:-1px;">🔱 TRIDENT-AI</h1>
                <p style="color:#64748b; margin:2px 0 0 0; font-family:monospace; font-size:12px; font-weight:bold; letter-spacing:0.5px;">📈 [ LIVE STOCK MARKET ANALYTICS SANDBOX v2.5 ]</p>
            </div>
            <div style="text-align: right;">
                <span style="background: rgba(16,185,129,0.15); color: #065f46; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; border: 1px solid rgba(16,185,129,0.3);">🟢 NSE LIVE POOL CONNECTED</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# SEBI REGULATORY COMPLIANCE BANNER
with st.expander("⚖️ SECURE LEGAL ARCHITECTURE DIRECTIVE & SEBI COMPLIANCE SHIELD", expanded=False):
    st.markdown("""
        <div style="font-size:12px; color:#475569; line-height:1.6; padding:10px; background: #f1f5f9; border-radius:6px; border-left:3px solid #64748b;">
            <strong>MANDATORY STATUTORY WARNING:</strong> We are <strong>NOT</strong> registered with SEBI as an investment advisor or research analyst. 
            This quantitative suite operations engine functions entirely as a decentralized, non-commercial software calculation simulator for educational modeling purposes. 
            No financial advice is given, and past metrics hold zero validation toward prospective price curves. Always protect capital through certified wealth advisors.
        </div>
    """, unsafe_allow_html=True)

# Initialize Session Engine States
if 'virtual_wallet' not in st.session_state:
    st.session_state.virtual_wallet = 1000000.00
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = {}  
if 'active_ticker' not in st.session_state:
    st.session_state.active_ticker = None
if 'active_strategy' not in st.session_state:
    st.session_state.active_strategy = "Swing"

st.markdown("<br>", unsafe_allow_html=True)

# BALANCE SHEET BANNER CARD
col_balance_card, col_spacing = st.columns(2)
with col_balance_card:
    st.markdown('<div class="trade-panel" style="padding: 14px 20px !important; background:#ffffff;">', unsafe_allow_html=True)
    st.metric(label="💰 PRACTICE SANDBOX WALLET BALANCE", value=f"₹{st.session_state.virtual_wallet:,.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

# CENTRAL OPERATION CONTROL PANEL
st.markdown('<div class="trade-panel">', unsafe_allow_html=True)
st.markdown("<h3 style='color:#0f172a; margin-top:0; margin-bottom:15px; font-size:18px; font-weight:800;'>📊 ASSET AND HORIZON MATRIX</h3>", unsafe_allow_html=True)
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
    selected_stock_label = st.selectbox("🎯 SELECT NSE MARKET TICKER:", list(stock_dictionary.keys()))
    formatted_ticker = stock_dictionary[selected_stock_label]
with col_timeframe:
    strategy_select = st.selectbox("⚙️ SCANNING STRATEGY CHANNEL:", ["Swing / Long-Term Investing", "Intraday Trading Momentum"])

chosen_mode = "Intraday" if "Intraday" in strategy_select else "Swing"

st.markdown("<br>", unsafe_allow_html=True)
if st.button("⚡ EXECUTE MULTI-AGENT SCAN LOOP"):
    st.session_state.active_ticker = formatted_ticker
    st.session_state.active_strategy = chosen_mode
st.markdown('</div>', unsafe_allow_html=True)

# DYNAMIC RADAR OUTPUT GRID
if st.session_state.active_ticker:
    current_ticker = st.session_state.active_ticker
    current_mode = st.session_state.active_strategy
    
    result = scan_stock(current_ticker, current_mode)
    
    if result is None:
        st.error("System Error: Market data loop interrupted. Please re-run selection.")
        st.session_state.active_ticker = None
    elif result["status"] == "BLOCKED":
        st.error(f"⚠️ Risk Guard Triggered: {result['reason']}")
        st.session_state.active_ticker = None
    elif result["status"] == "SUCCESS":
        
        beginner_tab, pro_tab, paper_trade_tab, leaderboard_tab = st.tabs([
            "🟢 STRATEGY DIRECTIONAL BIAS", 
            "🔵 INSTITUTIONAL METRICS", 
            "🎮 SIMULATED ORDER ROUTER",
            "🏆 SYSTEM CHALLENGE LEADERBOARD"
        ])
        
        with beginner_tab:
            st.markdown('<div class="trade-panel">', unsafe_allow_html=True)
            st.markdown(f"<h2 style='color:#0f172a; font-weight:800; font-size:22px; margin-top:0;'>Diagnostic Output: {result['decision']}</h2>", unsafe_allow_html=True)
            
            st.write(f"**Trident Mathematical Weight Confluence Index:** {result['raw_score']}/100")
            st.progress(result['raw_score'] / 100)
            
            st.markdown("---")
            col_metric_1, col_metric_2 = st.columns(2)
            with col_metric_1:
                st.metric(label=f"LIVE MARKET VALUATION ({current_mode})", value=f"₹{result['price']}")
            with col_metric_2:
                st.info(f"**System Diagnostic Logic Breakdown:** {result['explanation']}")
            
            st.markdown("<br><h4 style='color:#0f172a; font-weight:800; margin-bottom:10px;'>📊 HISTORICAL PRICE VECTOR FEED</h4>", unsafe_allow_html=True)
            stock_data = yf.Ticker(current_ticker).history(period="1mo" if current_mode == "Intraday" else "3mo")
            st.line_chart(stock_data['Close'])
            st.markdown('</div>', unsafe_allow_html=True)
            
        with pro_tab:
            st.markdown('<div class="trade-panel">', unsafe_allow_html=True)
            st.markdown("<h3 style='color:#0f172a; font-weight:800; margin-top:0;'>📊 Quantitative Metric Stream Matrix</h3>", unsafe_allow_html=True)
            # CO-FOUNDER REPAIR: SECURELY BALANCED JSON BRACKETS HERE
            st.json({
                "Target Asset Ticker Key": current_ticker,
                "Operational Pipeline Routing": f"NSE India {current_mode} Feed",
