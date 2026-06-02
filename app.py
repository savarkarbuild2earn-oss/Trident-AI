import streamlit as st
from engine import scan_stock
import yfinance as yf
import urllib.parse

# Setup complete wide-viewport application template
st.set_page_config(page_title="Trident-AI Dashboard", layout="wide")
st.title("🔱 Trident-AI: Smart Indian Stock Market Engine")

# ==============================================================================
# MANDATORY LEGAL GUARD: TOP BANNER DISCLOSURE
# ==============================================================================
st.error(
    "⚠️ **LEGAL DISCLAIMER & SEBI DISCLOSURE:** We are NOT a SEBI-registered investment advisor "
    "or research analyst. This platform is designed strictly for educational purposes and market "
    "strategy simulations. It does not provide personalized investment advice, buy/sell recommendations, "
    "or certified financial planning services under SEBI regulations. All virtual trading activities "
    "on this platform use simulated paper currency. Past performance does not guarantee future results. "
    "Consult a certified financial professional before risking real capital in the Indian Stock Markets."
)
st.caption("Empowering retail investors with institutional-grade risk safety filters.")

# INITIALIZE ADVANCED SESSION MEMORY OBJECTS
if 'virtual_wallet' not in st.session_state:
    st.session_state.virtual_wallet = 1000000.00
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = {}  
if 'active_ticker' not in st.session_state:
    st.session_state.active_ticker = None
if 'active_strategy' not in st.session_state:
    st.session_state.active_strategy = "Swing"

# PERSISTENT SCOREBOARD SEED DATA FOR SIMULATION CHALLENGE
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = [
        {"Rank": 1, "Trader Name": "Alpha_Quant_IN", "Virtual Balance": "₹12,45,200.00", "Weekly Gain": "+24.5%"},
        {"Rank": 2, "Trader Name": "NiftyWhale", "Virtual Balance": "₹11,12,000.00", "Weekly Gain": "+11.2%"},
        {"Rank": 3, "Trader Name": "You", "Virtual Balance": f"₹{st.session_state.virtual_wallet:,.2f}", "Weekly Gain": "0.0%"}
    ]

# Dynamically synchronize user ranking data on live UI updates
st.session_state.leaderboard[2]["Virtual Balance"] = f"₹{st.session_state.virtual_wallet:,.2f}"

# Display Wallet Balance prominently across the application dashboard layout
col_wallet, col_empty_space = st.columns(2)
with col_wallet:
    st.metric(label="💰 Your Free Virtual Cash Balance", value=f"₹{st.session_state.virtual_wallet:,.2f}")

# SYSTEM CONTROLS SPLIT CARD RENDER
col_inputs, col_timeframe = st.columns(2)
with col_inputs:
    ticker_input = st.text_input("Enter NSE Stock Ticker Symbol:", "SBIN")
with col_timeframe:
    strategy_select = st.selectbox("Select Target Strategy Window Execution:", ["Swing / Long-Term Investing", "Intraday Trading Momentum"])

# Clean formatting triggers
cleaned_input = ticker_input.strip().upper()
formatted_ticker = f"{cleaned_input}.NS" if ".NS" not in cleaned_input else cleaned_input
chosen_mode = "Intraday" if "Intraday" in strategy_select else "Swing"

if st.button("Run Advanced Multi-Agent AI Diagnostics"):
    st.session_state.active_ticker = formatted_ticker
    st.session_state.active_strategy = chosen_mode

if st.session_state.active_ticker:
    current_ticker = st.session_state.active_ticker
    current_mode = st.session_state.active_strategy
    
    # Process calculations using our new multi-timeframe brain matrix
    result = scan_stock(current_ticker, current_mode)
    
    if result is None:
        st.error("Invalid Ticker or Empty Stream Pool. Verify token symbols are valid NSE assets.")
        st.session_state.active_ticker = None
    elif result["status"] == "BLOCKED":
        st.error(f"⚠️ Stock Pipeline Halted: {result['reason']}")
        st.session_state.active_ticker = None
    elif result["status"] == "SUCCESS":
        
        beginner_tab, pro_tab, paper_trade_tab, leaderboard_tab = st.tabs([
            "🟢 Beginner Mode", 
            "🔵 Institutional Pro Mode", 
            "🎮 Live Paper Trading Sandbox",
            "🏆 Viral Public Leaderboard"
        ])
        
        with beginner_tab:
            st.header(f"Strategy Routing: {result['decision']}")
            st.write(f"**Trident Confluence Calculation Metric Index:** {result['raw_score']}/100")
            st.progress(result['raw_score'] / 100)
            
            st.metric(label=f"Current Market Price ({current_mode} Stream)", value=f"₹{result['price']}")
            st.info(f"**Unified Diagnostic Reasoning:** {result['explanation']}")
            
            st.subheader("📊 Price Action Analytics Stream")
            stock_data = yf.Ticker(current_ticker).history(period="1mo" if current_mode == "Intraday" else "3mo")
            st.line_chart(stock_data['Close'])
            
        with pro_tab:
            st.subheader("Institutional Quantitative Breakdown Matrix")
            st.json({
                "Target Asset Index Key": current_ticker,
                "Operational Engine Target Channel": f"NSE India {current_mode} Flow",
                "Algorithmic Score Output Value": result['raw_score'],
                "Relative Strength Index Vector Value": result['rsi'],
                "Security Risk Shield Gate": "PASSED & STABLE",
                "Regulatory Context Compliance": "100% Non-Commercial Virtual Simulation Environment"
            })
            
        with paper_trade_tab:
            st.subheader("🎮 Execute Zero-Risk Virtual Order Execution")
            st.write(f"Live Asset Value for current ticket loop: **₹{result['price']}**")
            
            with st.form("sandbox_order_form"):
                quantity = st.number_input("Input Target Shares Quantity:", min_value=1, value=10, step=1)
                submit_order = st.form_submit_button("Confirm Virtual Buy Order")
                
                if submit_order:
                    total_cost = quantity * result['price']
                    if total_cost > st.session_state.virtual_wallet:
                        st.error("❌ Transaction Halted: Insufficient sandbox wallet currency reserves!")
                    else:
                        st.session_state.virtual_wallet -= total_cost
                        st.session_state.portfolio[current_ticker] = st.session_state.portfolio.get(current_ticker, 0) + quantity
                        st.success(f"🎉 Successfully executed purchase sequence for {quantity} shares of {current_ticker}!")
                        st.rerun()
                        
        with leaderboard_tab:
            st.subheader("🏆 Trident-AI Global Practice Leaderboard")
            st.caption("Compete with elite retail portfolio managers risk-free across the globe.")
            st.table(st.session_state.leaderboard)

if st.session_state.portfolio:
    st.markdown("---")
    st.subheader("💼 Your Current Virtual Stock Portfolio Holdings")
    for ticker, shares in st.session_state.portfolio.items():
        st.info(f"Holding **{shares} shares** of **{ticker}**")
    
    clean_url = "https://streamlit.app"
    share_msg = f"I am practicing my stock strategy metrics completely risk-free using Trident-AI! Check out the platform: {clean_url}"
    encoded_msg = urllib.parse.quote(share_msg)
    
    st.markdown("### 🚀 Invite Trading Communities & Share Records!")
    col_wa, col_tg = st.columns(2)
    with col_wa:
        # BULLETPROOF NON-CONFLICTING STRING FORMATTING FOR THE SHARE BUTTONS
        whatsapp_html = f'<a href="https://whatsapp.com{encoded_msg}" target="_blank"><button style="background-color:#25D366;color:white;border:none;padding:10px 20px;border-radius:5px;cursor:pointer;font-weight:bold;">🟢 Share to WhatsApp Trading Groups</button></a>'
        st.markdown(whatsapp_html, unsafe_url_allowed=True)
    with col_tg:
        telegram_html = f'<a href="https://t.me{clean_url}&text={urllib.parse.quote("Practicing my algorithmic stock metrics completely risk-free using Trident-AI!")}" target="_blank"><button style="background-color:#0088cc;color:white;border:none;padding:10px 20px;border-radius:5px;cursor:pointer;font-weight:bold;">🔵 Post to Telegram Community Channels</button></a>'
        st.markdown(telegram_html, unsafe_url_allowed=True)

st.markdown("---")
st.caption(
    "🔒 **Regulatory Compliance Note:** Trident-AI is an independent, non-commercial software architecture "
    "built for simulation, learning, and software prototyping. We are not registered with SEBI. By interacting with "
    "this dashboard, you acknowledge that no financial advice is being administered."
)
