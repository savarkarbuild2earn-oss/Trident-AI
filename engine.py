import yfinance as yf
import pandas as pd
import ta
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import pytz

def fetch_live_news_sentiment(stock_name):
    """Bypasses paid APIs to scrape real-time financial news loops via Google News RSS."""
    try:
        url = f"https://google.com{stock_name}+stock+market+india&hl=en-IN&gl=IN&ceid=IN:en"
        response = requests.get(url, timeout=2)
        if response.status_code != 200:
            return "Neutral"
        
        root = ET.fromstring(response.content)
        headlines = [item.find('title').text for item in root.findall('.//item')[:2]]
        
        if not headlines:
            return "Neutral"
            
        positive_keywords = ['profit', 'surge', 'buy', 'order', 'growth', 'deal', 'gain', 'dividend', 'win', 'bull']
        negative_keywords = ['fall', 'loss', 'drop', 'slump', 'scam', 'probe', 'penalty', 'decline', 'bear']
        
        score = 0
        for headline in headlines:
            text = headline.lower()
            for p in positive_keywords:
                if p in text: score += 1
            for n in negative_keywords:
                if n in text: score -= 1
                
        if score > 0: return "Bullish"
        elif score < 0: return "Bearish"
        return "Neutral"
    except Exception:
        return "Neutral"

def autonomous_whale_scanner():
    """
    Hands-Free Engine: Processes market drivers and appends dedicated columns 
    for Target Execution Windows and Recommended Holding Durations.
    """
    market_pool = [
        "RELIANCE.NS", "SBIN.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
        "ITC.NS", "LT.NS", "TATAMOTORS.NS", "BHARTIALRT.NS", "IRFC.NS", "IREDA.NS",
        "SUZLON.NS", "ZOMATO.NS", "TATASTEEL.NS", "PNB.NS", "HAL.NS", "BHEL.NS",
        "PFC.NS", "RECL.NS", "NHPC.NS", "GMRINFRA.NS", "TATAPOWER.NS", "ADANIPOWER.NS"
    ]
    
    intraday_feed = []
    long_term_feed = []
    
    ist_timezone = pytz.timezone('Asia/Kolkata')
    current_time_ist = datetime.now(ist_timezone).strftime("%I:%M:%S %p")
        
    for ticker in market_pool:
        try:
            stock = yf.Ticker(ticker)
            df = stock.history(period="6mo", interval="1d")
            
            if df.empty or len(df) < 50:
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
            
            # 1. TIMED INTRADAY METRICS GENERATION
            if score >= 70:
                intra_signal = "🟢 ACCUMULATE (BUY)"
                intra_entry = f"₹{current_price:,.2f}"
                intra_exit = f"₹{current_price * 1.025:,.2f}"
                holding_period_intra = "⏰ Same Day (Exit before 3:15 PM IST)"
            elif score <= 35:
                intra_signal = "🔴 LIQUIDATE (SELL)"
                intra_entry = "Avoid Entry"
                intra_exit = f"₹{current_price * 0.985:,.2f}"
                holding_period_intra = "⚡ Immediate Action Required"
            else:
                intra_signal = "🟡 CONSOLIDATION HOLD"
                intra_entry = f"₹{current_price:,.2f}"
                intra_exit = f"₹{current_price * 1.01:,.2f}"
                holding_period_intra = "⏳ 1 to 3 Trading Sessions"
                
            intraday_feed.append({
                "🔥 Stock Name": clean_name,
                "💰 Live Value": f"₹{current_price:,.2f}",
                "📊 Intraday Signal": intra_signal,
                "🟢 Target Entry Line": intra_entry,
                "🔴 Target Exit Line": intra_exit,
                "⏱️ Target Window (IST)": "9:15 AM - 3:30 PM",
                "⏳ Max Holding Period": holding_period_intra,
                "🧬 Score": int(score)
            })
            
            # 2. TIMED LONG-TERM METRICS GENERATION
            if current_price > sma_50 and news_sentiment != "Bearish":
                long_outlook = "📈 STABLE COMPOUNDER"
                long_action = "🟢 ACCUMULATE HOLD"
                long_target = f"₹{current_price * 1.25:,.2f}"
                holding_period_long = "💎 12 Months to 3+ Years"
            else:
                long_outlook = "📉 WEAK / RE-TESTING"
                long_action = "🟡 WAIT / REDUCE SIZING"
                long_target = "Await Macro Reversal"
                holding_period_long = "❌ Cash Preservation Mode"
                
            long_term_feed.append({
                "🔥 Stock Name": clean_name,
                "💰 Market Value": f"₹{current_price:,.2f}",
                "💎 Structural Outlook": long_outlook,
                "📊 Strategic Action": long_action,
                "🎯 Macro Target Exit Line": long_target,
                "📅 Target Window": "Next 12-36 Months",
                "🛡️ Safe Holding Period": holding_period_long
            })
            
        except Exception:
            continue
            
    return pd.DataFrame(intraday_feed), pd.DataFrame(long_term_feed)
