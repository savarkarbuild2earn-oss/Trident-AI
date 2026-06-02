import streamlit as st
from engine import scan_stock
import yfinance as yf
import urllib.parse

st.set_page_config(page_title="Trident-AI Dashboard", layout="wide")
st.title("🔱 Trident-AI: Smart Indian Stock Market Engine")

st.error(
    "⚠️ **LEGAL DISCLAIMER & SEBI DISCLOSURE:** We are NOT a SEBI-registered investment advisor "
    "or research analyst. This platform is designed strictly for educational purposes and market "
    "strategy simulations. It does not provide personalized investment advice, buy/sell recommendations, "
    "or certified financial planning services under SEBI regulations. All virtual trading activities "
    "on this platform use simulated paper currency. Past performance does not guarantee future results. "
    "Consult a certified financial professional before risking real capital in the Indian Stock Markets."
)
st.caption("Empowering retail investors with institutional-grade risk safety filters.")

if 'virtual_wallet' not in st.session_state:
    st.session_state.virtual_wallet = 1000000.00
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = {}  
if 'active_ticker' not in st.session_state:
    st.session_state.active_ticker = None

col_wallet, col_empty = st.columns(2)
with col_wallet:
    st.metric(label="💰 Your Free Virtual Cash Balance", value=f"₹{st.session_state.virtual_wallet:,.2f}")

# User input field with cleanup triggers
ticker_input = st.text_input("Enter NSE Stock Ticker (e.g., RELIANCE, TCS, SBIN):", "SBIN")
cleaned_input = ticker_input.strip().upper()
if ".NS" not in cleaned_input:
    formatted_ticker = f"{cleaned_input}.NS"
else:
    formatted_ticker = cleaned_input

if st.button("Run Advanced AI Diagnostics"):
    st.session_state.active_ticker = formatted_ticker

if st.session_state.active_ticker:
    current_ticker = st.session_state.active_ticker
    result = scan_stock(current_ticker)
    
    if result is None:
        st.error("Invalid Ticker or No Data Found. Ensure you are searching a valid NSE Indian stock symbol.")
        st.session_state.active_ticker = None
    elif result["status"] == "BLOCKED":
        st.error(f"⚠️ Stock Blocked: {result['reason']}")
        st.session_state.active_ticker = None
    elif result["status"] == "SUCCESS":
        
        beginner_tab, pro_tab, paper_trade_tab = st.tabs([
            "🟢 Beginner Mode", 
            "🔵 Institutional Pro Mode", 
            "🎮 Live Paper Trading Sandbox"
        ])
        
        with beginner_tab:
            st.header(f"Action Signal: {result['decision']}")
            st.write(f"**Trident Scoring Matrix Confluence Engine Index:** {result['raw_score']}/100")
            st.progress(result['raw_score'] / 100)
            
            st.metric(label="Current Market Price", value=f"₹{result['price']}")
            st.info(f"**Why this signal?** {result['explanation']}")
            
            st.subheader("📊 3-Month Price Trend")
            stock_data = yf.Ticker(current_ticker).history(period="3mo")
            st.line_chart(stock_data['Close'])
            
        with pro_tab:
            st.subheader("Quantitative Analytics Breakdown")
            st.json({
                "Ticker Token": current_ticker,
                "Algorithmic Score Out of 100": result['raw_score'],
                "Relative Strength Index (RSI)": result['rsi'],
                "Risk Shield Engine": "PASSED & SECURE",
                "Exchange Route": "NSE India",
                "Regulatory Framework": "Educational Market Simulation Engine Only"
            })
            
        with paper_trade_tab:
            st.subheader("🎮 Execute Zero-Risk Virtual Order")
            st.write(f"Live Price for execution: **₹{result['price']}**")
            
            with st.form("sandbox_order_form"):
                quantity = st.number_input("Enter Quantity of Shares to buy:", min_value=1, value=10, step=1)
                submit_order = st.form_submit_button("Confirm Virtual Buy Order")
                
                if submit_order:
                    total_cost = quantity * result['price']
                    if total_cost > st.session_state.virtual_wallet:
                        st.error("❌ Insufficient virtual balance to execute this trade!")
                    else:
                        st.session_state.virtual_wallet -= total_cost
                        st.session_state.portfolio[current_ticker] = st.session_state.portfolio.get(current_ticker, 0) + quantity
                        st.success(f"🎉 Successfully bought {quantity} shares of {current_ticker}!")
                        st.rerun()

if st.session_state.portfolio:
    st.markdown("---")
    st.subheader("💼 Your Current Virtual Stock Portfolio Holdings")
    for ticker, shares in st.session_state.portfolio.items():
        st.info(f"Holding **{shares} shares** of **{ticker}**")
    
    clean_url = "https://streamlit.io"
    share_msg = f"I am testing my trading strategies completely risk-free using Trident-AI! Check out the metrics here: {clean_url}"
    encoded_msg = urllib.parse.quote(share_msg)
    
    st.markdown("### 🚀 Share Your Strategy & Challenge Friends!")
    col_wa, col_tg = st.columns(2)
    with col_wa:
        st.markdown(f'<a href="https://whatsapp.com{encoded_msg}" target="_blank"><button style="background-color:#25D366;color:white;border:none;padding:10px 20px;border-radius:5px;cursor:pointer;font-weight:bold;">🟢 Share on WhatsApp</button></a>', unsafe_url_allowed=True)
    with col_tg:
        st.markdown(f'<a href="https://t.me{clean_url}&text={urllib.parse.quote("Testing my algorithmic trades on Trident-AI!")}" target="_blank"><button style="background-color:#0088cc;color:white;border:none;padding:10px 20px;border-radius:5px;cursor:pointer;font-weight:bold;">🔵 Share on Telegram</button></a>', unsafe_url_allowed=True)

st.markdown("---")
st.caption(
    "🔒 **Regulatory Compliance Note:** Trident-AI is an independent, non-commercial software architecture "
    "built for simulation, learning, and software prototyping. We are not registered with SEBI. By interacting with "
    "this dashboard, you acknowledge that no financial advice is being administered."
)
