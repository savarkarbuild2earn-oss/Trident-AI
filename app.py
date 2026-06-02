import streamlit as st
from engine import scan_stock
import yfinance as yf

st.set_page_config(page_title="Trident-AI Dashboard", layout="wide")
st.title("🔱 Trident-AI: Smart Indian Stock Market Engine")
st.caption("Empowering retail investors with institutional-grade risk safety filters.")

# INITIALIZE VIRTUAL WALLET SESSION MEMORY (10 Lakhs INR)
if 'virtual_wallet' not in st.session_state:
    st.session_state.virtual_wallet = 1000000.00
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = {}  # Tracks format: {TICKER: SHARES}

# Display Live Wallet Balance across the top of the app
col_wallet, col_empty = st.columns([1, 3])
with col_wallet:
    st.metric(label="💰 Your Free Virtual Cash Balance", value=f"₹{st.session_state.virtual_wallet:,.2f}")

ticker_input = st.text_input("Enter NSE Stock Ticker (e.g., RELIANCE, TCS, SBIN):", "SBIN")
formatted_ticker = f"{ticker_input.strip().upper()}.NS"

if st.button("Run Advanced AI Diagnostics"):
    with st.spinner("Analyzing financials, volume patterns, and chart structures..."):
        result = scan_stock(formatted_ticker)
        
        if result is None:
            st.error("Invalid Ticker or No Data Found. Please check the NSE symbol.")
        elif result["status"] == "BLOCKED":
            st.error(f"⚠️ Stock Blocked: {result['reason']}")
        elif result["status"] == "SUCCESS":
            
            beginner_tab, pro_tab, paper_trade_tab = st.tabs([
                "🟢 Beginner Mode", 
                "🔵 Institutional Pro Mode", 
                "🎮 Live Paper Trading Sandbox"
            ])
            
            with beginner_tab:
                st.header(f"Action Signal: {result['decision']}")
                st.metric(label="Current Market Price", value=f"₹{result['price']}")
                st.info(f"**Why this signal?** {result['explanation']}")
                
                st.subheader("📊 3-Month Price Trend")
                stock_data = yf.Ticker(formatted_ticker).history(period="3mo")
                st.line_chart(stock_data['Close'])
                
            with pro_tab:
                st.subheader("Quantitative Analytics Breakdown")
                st.json({
                    "Ticker Token": formatted_ticker,
                    "Risk Shield Engine": "PASSED & SECURE",
                    "Exchange Route": "NSE India",
                    "Data Interval Source": "Yahoo Finance Live Stream Feed"
                })
                
            with paper_trade_tab:
                st.subheader("🎮 Execute Zero-Risk Virtual Order")
                st.write(f"Live Price for execution: **₹{result['price']}**")
                
                # Input fields for order execution
                quantity = st.number_input("Enter Quantity of Shares to buy:", min_value=1, value=10, step=1)
                total_cost = quantity * result['price']
                st.write(f"Total Order Value: **₹{total_cost:,.2f}**")
                
                if st.button("Confirm Virtual Buy Order"):
                    if total_cost > st.session_state.virtual_wallet:
                        st.error("❌ Insufficient virtual balance to execute this trade!")
                    else:
                        # Deduct from wallet cash
                        st.session_state.virtual_wallet -= total_cost
                        # Add shares to our digital portfolio
                        st.session_state.portfolio[formatted_ticker] = st.session_state.portfolio.get(formatted_ticker, 0) + quantity
                        st.success(f"🎉 Successfully bought {quantity} shares of {formatted_ticker} in your Sandbox!")
                        st.rerun()

# Display current holdings box if user owns stocks
if st.session_state.portfolio:
    st.markdown("---")
    st.subheader("💼 Your Current Virtual Stock Portfolio Holdings")
    for ticker, shares in st.session_state.portfolio.items():
        st.info(f"Holding **{shares} shares** of **{ticker}**")
