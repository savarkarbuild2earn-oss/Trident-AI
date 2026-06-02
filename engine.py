import yfinance as yf
import pandas as pd
import ta
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import pytz

def fetch_live_news_sentiment(stock_name):
    """Bypasses paid APIs to scrape real-time financial news updates via RSS."""
    try:
        url = f"https://google.com{stock_name}+stock+market+india&hl=en-IN&gl=IN&ceid=IN:en"
        response = requests.get(url, timeout=1)
        if response.status_code != 200:
            return "Neutral"
        root = ET.fromstring(response.content)
        headlines = [item.find('title').text for item in root.findall('.//item')[:1]]
        if not headlines:
            return "Neutral"
        p_words = ['profit', 'surge', 'buy', 'order', 'growth', 'deal', 'gain', 'win', 'bull']
        n_words = ['fall', 'loss', 'drop', 'slump', 'scam', 'probe', 'penalty', 'decline', 'bear']
        score = 0
        text = headlines[0].lower()
        for p in p_words:
            if p in text: score += 1
        for n in n_words:
            if n in text: score -= 1
        if score > 0: return "Bullish"
        elif score < 0: return "Bearish"
        return "Neutral"
    except Exception:
        return "Neutral"

def autonomous_whale_scanner():
    """
    Hands-Free Engine: Uses sequential fallback queries to compile multi-horizon
    streams, synchronizing a 24-hour dynamic time vector only for long-term targets.
    """
    nifty_100_pool = [
        "RELIANCE.NS", "SBIN.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
        "ITC.NS", "LT.NS", "TATAMOTORS.NS", "BHARTIALRT.NS", "IRFC.NS", "IREDA.NS",
        "SUZLON.NS", "ZOMATO.NS", "TATASTEEL.NS", "PNB.NS", "HAL.NS", "BHEL.NS",
        "PFC.NS", "RECL.NS", "NHPC.NS", "GMRINFRA.NS", "TATAPOWER.NS", "ADANIPOWER.NS"
    ]
    
    intraday_list = []
    longterm_list = []
    
    # Standardize timezones for accurate Indian Standard Time operations
    ist_tz = pytz.timezone('Asia/Kolkata')
    current_time_12h = datetime.now(ist_tz).strftime("%I:%M:%S %p")
    current_time_24h = datetime.now(ist_tz).strftime("%H:%M:%S") # Dedicated 24-hour metric clock
        
    for ticker in nifty_100_pool:
        try:
            stock = yf.Ticker(ticker)
            df = stock.history(period="3mo", interval="1d")
            
            if df.empty or len(df) < 20: 
                continue
                
            current_price = df['Close'].iloc[-1]
            clean_name = ticker.replace(".NS", "")
            
            df['RSI'] = ta.momentum.rsi(df['Close'], window=14)
            df['SMA_20'] = df['Close'].rolling(window=20).mean()
            df['SMA_50'] = df['Close'].rolling(window=50).mean()
            
            current_rsi = df['RSI'].fillna(50).iloc[-1]
            sma_20 = df['SMA_20'].fillna(current_price).iloc[-1]
            sma_50 = df['SMA_50'].fillna(current_price).iloc[-1]
            
            news_sentiment = fetch_live_news_sentiment(clean_name)
            
            score = 0
            if current_price > sma_20: score += 40
            if 40 <= current_rsi <= 65: score += 30
            if news_sentiment == "Bullish": score += 30
            if news_sentiment == "Bearish": score -= 20
            
            # INTRADAY PROCESSING STREAM (Maintains standard 12H clock)
            if score >= 70:
                intra_signal = "🟢 BUY ACCUMULATE"
                intra_exit = f"₹{current_price * 1.025:,.2f}"
            elif score <= 35:
                intra_signal = "🔴 LIQUIDATE SELL"
                intra_exit = f"₹{current_price * 0.985:,.2f}"
            else:
                intra_signal = "🟡 HOLD RANGE"
                intra_exit = f"₹{current_price * 1.01:,.2f}"
                
            intraday_list.append({
                "⏰ Time (IST)": current_time_12h,
                "🔥 Stock": clean_name,
                "💰 Current Price": f"₹{current_price:,.2f}",
                "📊 Intraday Signal": intra_signal,
                "🟢 Target Entry": f"₹{current_price:,.2f}",
                "🔴 Target Exit Line": intra_exit,
                "⏳ Max Holding Period": "⏰ Same Day (Exit 3:15 PM)" if score != 50 else "⏳ 1-2 Trading Sessions",
                "🧬 Score": int(score)
            })
            
            # LONG-TERM VALUE STREAMING MATRICES (Uses the new dynamic 24-Hour time index)
            if current_price > sma_50 * 1.12:
                long_outlook = "🚀 ACCELERATED MOMENTUM"
                long_period = "💎 1 Month (Fast Momentum Capture)"
                long_target = f"₹{current_price * 1.07:,.2f}"
            elif sma_50 * 1.04 < current_price <= sma_50 * 1.12:
                long_outlook = "📈 STABLE COMPOUNDER"
                long_period = "💎 3 Months (Quarterly Trend Re-rate)"
                long_target = f"₹{current_price * 1.15:,.2f}"
            elif sma_50 <= current_price <= sma_50 * 1.04:
                long_outlook = "⚖️ BASE ACCUMULATION"
                long_period = "💎 6 Months (Structural Wealth Accumulation)"
                long_target = f"₹{current_price * 1.22:,.2f}"
            else:
                long_outlook = "📉 CYCLICAL RE-TESTING"
                long_period = "💎 12+ Months (Long-Term Value Hold)"
                long_target = f"₹{current_price * 1.35:,.2f}"
                
            longterm_list.append({
                "⏱️ Clock (24H)": current_time_24h, # Embedded dynamic 24-hour clock field
                "🔥 Stock Name": clean_name,
                "💰 Market Value": f"₹{current_price:,.2f}",
                "💎 Structural Outlook": long_outlook,
                "📅 Entry Window": "Current Trading Week",
                "🎯 Macro Target Exit Line": long_target,
                "⏳ Recommended Hold": long_period
            })
        except Exception:
            continue
            
    return pd.DataFrame(intraday_list), pd.DataFrame(longterm_list)
