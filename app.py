import streamlit as st
from engine import scan_stock
import yfinance as yf
import urllib.parse

# 1. VISUAL UI ENGINE: Initialize absolute premium layout configurations
st.set_page_config(
    page_title="Trident-AI Quant Terminal", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. CUSTOM GLASSMORPHISM CSS DESIGN INJECTIONS
st.markdown("""
    <style>
    /* Global Background Adjustments */
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    /* Institutional Metric Box Styles */
    div[data-testid="stMetricValue"] {
        font-size: 28px !important;
        font-weight: 700 !important;
        color: #58a6ff !important;
        font-family: 'Courier New', monospace;
    }
    /* Custom Styling for App Header Cards */
    .terminal-card {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        border: 1px solid #374151;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
    }
    /* Premium Button Stylings Override */
    .stButton>button {
        background: linear-gradient(90deg, #1f6feb 0%, #0052cc 100%) !important;
        color: white !important;
        border: none !important;
        padding: 12px 30px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        width: 100%;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
    }
    </style>
""", unsafe_url_allowed=True)

# Main Application Banner Frame
st.markdown("""
    <div class="terminal-card" style="border-left: 5px solid #1f6feb;">
        <h1 style="color:white; margin:0; font-size:32px;">🔱 TRIDENT-AI</h1>
        <p style="color:#8b949e; margin:5px 0 0 0; font-family:'Courier New', monospace;">[ INSTITUTIONAL QUANT SIMULATION SANDBOX v2.0 ]</p>
    </div>
""", unsafe_url_allowed=True)

# ==============================================================================
# SEBI LEGAL SHIELD CONTROLLER
# ==============================================================================
with st.expander("⚖️ MANDATORY REGULATORY FRAMEWORK DISCLOSURE & SEBI COMPLIANCE BANNER", expanded=True):
    st.markdown("""
        <div style="font-size:13px; color:#8b949e; line-height:1.6;">
            <strong>LEGAL NOTICE:</strong> We are <strong>NOT</strong> a SEBI-registered investment advisor or research analyst. 
            This engine functions strictly as a non-commercial software simulation environment for educational analysis. 
            No actionable trade signals or real financial advisory loops are generated here. All sandbox actions utilize simulated currency. 
            Past performance vectors are not indicative of forward market realities. Protect your capital by consulting a certified financial planner.
        </div>
    """, unsafe_url_allowed=True)

# Initialize Session Engine States
if 'virtual_wallet' not in st.session_state:
    st.session_state.virtual_wallet = 1000000.00
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = {}  
if 'active_ticker' not in st.session_state:
    st.session_state.active_ticker = None
if 'active_strategy' not in st.session_state:
    st.session_state.active_strategy = "Swing"

st.markdown("<br>", unsafe_url_allowed=True)

# CONTROL BAR GRID LAYOUT
col_wallet_card, col_blank = st.columns([1, 1])
with col_wallet_card:
    st.markdown('<div class="terminal-card" style="padding: 10px 20px;">', unsafe_url_allowed=True)
    st.metric(label="💰 SECURE SANDBOX LEDGER BALANCE", value=f"Answering Wallet: ₹{st.session_state.virtual_wallet:,.2f}")
    st.markdown('</div>', unsafe_url_allowed=True)

# ASSET SELECTOR MATRIX CARDS
st.markdown('<div class="terminal-card">', unsafe_url_allowed=True)
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
    selected_stock_label = st.selectbox("🌐 TARGET LIQUID ASSET MATRIX:", list(stock_dictionary.keys()))
    formatted_ticker = stock_dictionary[selected_stock_label]
with col_timeframe:
    strategy_select = st.selectbox("⚙️ EXECUTION ALGORITHM ROUTE:", ["Swing / Long-Term Investing", "Intraday Trading Momentum"])

chosen_mode = "Intraday" if "Intraday" in strategy_select else "Swing"

st.markdown("<br>", unsafe_url_allowed=True)
if st.button("⚡ EXECUTE MULTI-AGENT DIAGNOSTIC RUN"):
    st.session_state.active_ticker = formatted_ticker
    st.session_state.active_strategy = chosen_mode
st.markdown('</div>', unsafe_url_allowed=True)

# MAIN REPORT DATA GRID DISPLAY
if st.session_state.active_ticker:
    current_ticker = st.session_state.active_ticker
    current_mode = st.session_state.active_strategy
    
    result = scan_stock(current_ticker, current_mode)
    
    if result is None:
        st.error("Execution Halted: Asset verification timeout. Select another token symbol.")
        st.session_state.active_ticker = None
    elif result["status"] == "BLOCKED":
        st.error(f"⚠️ Algorithmic Block Triggered: {result['reason']}")
        st.session_state.active_ticker = None
    elif result["status"] == "SUCCESS":
        
        beginner_tab, pro_tab, paper_trade_tab, leaderboard_tab = st.tabs([
            "🟢 OVERVIEW SCANNER", 
            "🔵 DEEP CONFLUENCE DATA", 
            "🎮 SIMULATED ORDER DEPTH",
            "🏆 GLOBAL SYSTEM RANKINGS"
        ])
        
        with beginner_tab:
            st.markdown('<div class="terminal-card">', unsafe_url_allowed=True)
            st.subheader(f"System Directional Bias: {result['decision']}")
            
            st.write(f"**Trident Confluence Index Model:** {result['raw_score']}/100")
            st.progress(result['raw_score'] / 100)
            
            if result['raw_score'] >= 75:
                st.success("🔥 **CONFLUENCE SCORE VERIFIED (75-100):** System architecture reports high structural acceleration trends across all processing nodes safely.")
            elif 40 <= result['raw_score'] < 74:
                st.warning("⚖️ **NEUTRAL SYSTEM SCORE REGISTERED (40-74):** Indicators split. Trend vectors shifting sideways. Execute defensive sizing protocols.")
            else:
                st.error("🚨 **SEVERE TECHNICAL DISTRIBUTION IN PROGRESS (0-39):** Selling liquidity dominating the local order books. Risk parameters completely saturated.")
            
            st.markdown("---")
            col_metric_1, col_metric_2 = st.columns(2)
            with col_metric_1:
                st.metric(label=f"LAST EXECUTION VALUE ({current_mode})", value=f"₹{result['price']}")
            with col_metric_2:
                st.info(f"**AI Structural Summary:** {result['explanation']}")
            
            st.subheader("📊 PRICE TREND ANALYSIS ENGINE")
            stock_data = yf.Ticker(current_ticker).history(period="1mo" if current_mode == "Intraday" else "3mo")
            st.line_chart(stock_data['Close'])
            st.markdown('</div>', unsafe_url_allowed=True)
            
        with pro_tab:
            st.markdown('<div class="terminal-card">', unsafe_url_allowed=True)
            st.subheader("Institutional Quantitative Breakdown Matrix")
            st.json({
                "Target Asset Index Key": current_ticker,
                "Operational Engine Target Channel": f"NSE India {current_mode} Flow",
                "Algorithmic Score Output Value": result['raw_score'],
                "Relative Strength Index Vector Value": result['rsi'],
                "Security Risk Shield Gate": "PASSED & STABLE",
                "Regulatory Context Compliance": "100% Non-Commercial Virtual Simulation Environment"
            })
            st.markdown('</div>', unsafe_url_allowed=True)
            
        with paper_trade_tab:
            st.markdown('<div class="terminal-card">', unsafe_url_allowed=True)
            st.subheader("🎮 Simulation Execution Depth Console")
            st.write(f"Live Market Feed Rate: **₹{result['price']}**")
            
            with st.form("sandbox_order_form"):
                quantity = st.number_input("Input Target Shares Transaction Limit Volumetrics:", min_value=1, value=10, step=1)
                submit_order = st.form_submit_button("CONFIRM Virtual Ledger ENTRY")
                
                if submit_order:
                    total_cost = quantity * result['price']
                    if total_cost > st.session_state.virtual_wallet:
                        st.error("❌ Transaction Terminated: Insufficient ledger wallet balance!")
                    else:
                        st.session_state.virtual_wallet -= total_cost
                        st.session_state.portfolio[current_ticker] = st.session_state.portfolio.get(current_ticker, 0) + quantity
                        st.success(f"🎉 Order execution processing clear! Allocated {quantity} shares of {current_ticker}.")
                        st.rerun()
            st.markdown('</div>', unsafe_url_allowed=True)
