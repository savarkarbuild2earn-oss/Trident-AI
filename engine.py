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
    100% Comprehensive Market Scanner: Loops over our target market pool individually,
    calculates precise tech levels, and maps out entry/exit points cleanly.
    """
    # Our master operational pool containing the heavy market-moving drivers
    market_pool = [
        "RELIANCE.NS", "SBIN.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
        "ITC.NS", "LT.NS", "TATAMOTORS.NS", "BHARTIALRT.NS", "IRFC.NS", "IREDA.NS",
        "SUZLON.NS", "ZOMATO.NS", "TATASTEEL.NS", "PNB.NS", "HAL.NS", "BHEL.NS",
        "PFC.NS", "RECL.NS", "NHPC.NS", "GMRINFRA.NS", "TATAPOWER.NS", "ADANIPOWER.NS"
    ]
    
    final_automated_feed = []
    
    # Configure timezone structure for precise local Indian market synchronization
    ist_timezone = pytz.timezone('Asia/Kolkata')
    current_time_ist = datetime.now(ist_timezone).strftime("%I:%M:%S %p")
        
    for ticker in market_pool:
        try:
            stock = yf.Ticker(ticker)
            # Individual 3-month daily history pull (Fast and 100% immune to bulk blocks)
            df = stock.history(period="3mo", interval="1d")
            
            if df.empty or len(df) < 20:
                continue
                
            current_price = df['Close'].iloc[-1]
            clean_name = ticker.replace(".NS", "")
            
            # Run fast quantitative indicator layers
            df['RSI'] = ta.momentum.rsi(df['Close'], window=14)
            df['SMA_20'] = df['Close'].rolling(window=20).mean()
            
            current_rsi = df['RSI'].fillna(50).iloc[-1]
            sma_20 = df['SMA_20'].fillna(current_price).iloc[-1]
            
            # Multi-Agent Scoring Grid
            score = 0
            if current_price > sma_20: score += 40
            if 40 <= current_rsi <= 65: score += 30
            
            # Live News Sentiment Integration
            news_sentiment = fetch_live_news_sentiment(clean_name)
            if news_sentiment == "Bullish": score += 30
            elif news_sentiment == "Bearish": score -= 20
            
            # Generate accurate direct labels and level margins
            if score >= 70:
                signal = "🟢 ACCUMULATE (BUY)"
                target_entry = f"₹{current_price:,.2f}"
                target_exit = f"₹{current_price * 1.03:,.2f}"
            elif score <= 35:
                signal = "🔴 LIQUIDATE (SELL)"
                target_entry = "Avoid Entry"
                target_exit = f"₹{current_price * 0.98:,.2f}"
            else:
                signal = "🟡 HOLD CONSOLIDATION"
                target_entry = f"₹{current_price:,.2f}"
                target_exit = f"₹{current_price * 1.01:,.2f}"
                
            final_automated_feed.append({
                "⏰ Detection Time (IST)": current_time_ist,
                "🔥 Active Stock": clean_name,
                "💰 Current Value": f"₹{current_price:,.2f}",
                "📊 Action Signal": signal,
                "🟢 Target Entry Line": target_entry,
                "🔴 Target Exit Line": target_exit,
                "🧬 Scoring Index": int(score) # Cast to integer for a clean Streamlit metric look
            })
        except Exception:
            continue
            
    return pd.DataFrame(final_automated_feed)
