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
        response = requests.get(url, timeout=5)
        
        if response.status_code != 200:
            return "Neutral Tone - Parsing Delayed"
        
        root = ET.fromstring(response.content)
        headlines = [item.find('title').text for item in root.findall('.//item')[:3]]
        
        if not headlines:
            return "No recent news volatility registered."
            
        positive_keywords = ['profit', 'surge', 'buy', 'order', 'growth', 'deal', 'gain', 'dividend']
        negative_keywords = ['fall', 'loss', 'drop', 'slump', 'scam', 'probe', 'penalty', 'decline']
        
        score = 0
        for headline in headlines:
            text = headline.lower()
            for p in positive_keywords:
                if p in text: score += 1
            for n in negative_keywords:
                if n in text: score -= 1
                
        if score > 0:
            return f"🟢 Bullish News Catalyst"
        elif score < 0:
            return f"🔴 Bearish News Catalyst"
        else:
            return f"⚖️ Neutral News Sentiment"
    except Exception:
        return "News Pool Temporarily Offline"

def autonomous_whale_scanner():
    """
    100% Hands-Free Engine: Scans market drivers, extracts high-activity tokens,
    and appends a precise Indian Standard Time (IST) execution stamp to every signal.
    """
    market_pool = [
        "RELIANCE.NS", "SBIN.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
        "ITC.NS", "LT.NS", "TATAMOTORS.NS", "BHARTIALRT.NS", "IRFC.NS", "IREDA.NS",
        "SUZLON.NS", "ZOMATO.NS", "TATASTEEL.NS", "PNB.NS", "HAL.NS", "BHEL.NS",
        "PFC.NS", "RECL.NS", "NHPC.NS", "GMRINFRA.NS", "TATAPOWER.NS", "ADANIPOWER.NS"
    ]
    
    raw_pool_data = []
    
    for ticker in market_pool:
        try:
            stock = yf.Ticker(ticker)
            # Fetch 1-minute interval streams to capture real-time execution timing accurately
            df = stock.history(period="1d", interval="1m")
            if df.empty or len(df) < 5:
                continue
                
            last_price = df['Close'].iloc[-1]
            last_volume = df['Volume'].iloc[-1]
            trading_activity_value = last_price * last_volume
            
            raw_pool_data.append({
                "ticker": ticker,
                "df": df,
                "price": last_price,
                "activity": trading_activity_value
            })
        except Exception:
            continue
            
    if not raw_pool_data:
        return pd.DataFrame()
        
    pool_df = pd.DataFrame(raw_pool_data)
    top_active_pool = pool_df.sort_values(by="activity", ascending=False).head(8)
    
    final_automated_feed = []
    
    # Configure timezone structure for precise local Indian market synchronization
    ist_timezone = pytz.timezone('Asia/Kolkata')
    current_time_ist = datetime.now(ist_timezone).strftime("%I:%M:%S %p")
    
    for _, row in top_active_pool.iterrows():
        try:
            ticker = row['ticker']
            df = row['df']
            current_price = row['price']
            clean_name = ticker.replace(".NS", "")
            
            df['RSI'] = ta.momentum.rsi(df['Close'], window=14)
            df['SMA_20'] = df['Close'].rolling(window=20).mean()
            
            current_rsi = df['RSI'].fillna(50).iloc[-1]
            sma_20 = df['SMA_20'].fillna(current_price).iloc[-1]
            
            live_news_vector = fetch_live_news_sentiment(clean_name)
            
            score = 0
            if current_price > sma_20: score += 40
            if 40 <= current_rsi <= 65: score += 30
            if "🟢" in live_news_vector: score += 30
            if "🔴" in live_news_vector: score -= 20
            
            # Formulate clear targets and actions based on the score matrix
            if score >= 70:
                signal = "🟢 BUY ACCUMULATE"
                target_entry = f"₹{current_price:,.2f}"
                target_exit = f"₹{current_price * 1.02:,.2f} (Take Profit)"
            elif score <= 35:
                signal = "🔴 LIQUIDATE / SELL"
                target_entry = "Avoid Entry"
                target_exit = f"₹{current_price * 0.98:,.2f} (Stop Loss Trigger)"
            else:
                signal = "🟡 CONSOLIDATION HOLD"
                target_entry = "Wait for Confluence"
                target_exit = "Monitor Range"
                
            final_automated_feed.append({
                "⏰ Detection Time (IST)": current_time_ist,
                "🔥 Active Stock": clean_name,
                "💰 Current Value": f"₹{current_price:,.2f}",
                "📊 Action Target": signal,
                "🟢 Target Entry line": target_entry,
                "🔴 Target Exit Line": target_exit,
                "🧬 Scoring Index": f"{score}/100"
            })
        except Exception:
            continue
            
    return pd.DataFrame(final_automated_feed)
