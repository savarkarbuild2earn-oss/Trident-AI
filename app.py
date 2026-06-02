import streamlit as st
from engine import scan_stock
import yfinance as yf # Imported to fetch historical chart data

st.set_page_config(page_title="Trident-AI Dashboard", layout="wide")
st.title("🔱 Trident-AI: Smart Indian Stock Market Engine")
st.caption("Empowering retail investors with institutional-grade risk safety filters.")

ticker_input = st.text_input("Enter NSE Stock Ticker (e.g., RELIANCE, TCS, SBIN):", "RELIANCE")
formatted_ticker = f"{ticker_input.strip().upper()}.NS"

if st.button("Run Advanced AI Diagnostics"):
    with st.spinner("Analyzing financials, volume patterns, and chart structures..."):
        result = scan_stock(formatted_ticker)
        
        if result is None:
            st.error("Invalid Ticker or No Data Found. Please check the NSE symbol.")
        elif result["status"] == "BLOCKED":
            st.error(f"⚠️ Stock Blocked: {result['reason']}")
        elif result["status"] == "SUCCESS":
            
            beginner_tab, pro_tab = st.tabs(["🟢 Beginner Mode", "🔵 Institutional Pro Mode"])
            
            with beginner_tab:
                st.header(f"Action Signal: {result['decision']}")
                st.metric(label="Current Market Price", value=f"₹{result['price']}")
                st.info(f"**Why this signal?** {result['explanation']}")
                
                # NEW VISUAL ANCHOR: Add an interactive price chart
                st.subheader("📊 3-Month Price Trend")
                stock_data = yf.Ticker(formatted_ticker).history(period="3mo")
                st.line_chart(stock_data['Close'])
                
                st.success("💡 Paper Trading Sandbox Active: You can safely track this stock using your free virtual ₹10 Lakhs.")
                
            with pro_tab:
                st.subheader("Quantitative Analytics Breakdown")
                st.json({
                    "Ticker Token": formatted_ticker,
                    "Risk Shield Engine": "PASSED & SECURE",
                    "Exchange Route": "NSE India",
                    "Data Interval Source": "Yahoo Finance Live Stream Feed"
                })
