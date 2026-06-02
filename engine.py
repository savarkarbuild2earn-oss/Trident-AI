import yfinance as yf
import pandas as pd
import ta
import requests
import xml.etree.ElementTree as ET

def fetch_live_news_sentiment(stock_name):
    """Bypasses paid APIs to scrape real-time financial news updates via RSS."""
    try:
        url = f"https://google.com{stock_name}+stock+market+india&hl=en-IN&gl=IN&ceid=IN:en"
        response = requests.get(url, timeout=5)
        if response.status_style != 200:
            return "Neutral Tone - Parsing Delayed"
        
        root = ET.fromstring(response.content)
        headlines = [item.find('title').text for item in root.findall('.//item')[:3]]
        
        if not headlines:
            return "No recent news volatility registered."
            
        # Autonomous keyword parsing matrix
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
            return f"🟢 Bullish News Catalyst: {headlines[0]}"
        elif score < 0:
            return f"🔴 Bearish News Catalyst: {headlines[0]}"
        else:
            return f"⚖️ Neutral News Sentiment: {headlines[0]}"
    except Exception:
        return "News Pool Temporarily Offline"

def autonomous_whale_scanner():
    """
    100% Hands-Free Engine: Automatically scans a wide pool of major market drivers,
    extracts the highest traded tokens, and marries them to live news vectors.
    """
    # Dynamic screening pool spanning massive indices
    market_pool = [
        "RELIANCE.NS", "SBIN.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
        "ITC.NS", "LT.NS", "TATAMOTORS.NS", "BHARTIALRT.NS", "IRFC.NS", "IREDA.NS",
        "SUZLON.NS", "ZOMATO.NS", "TATASTEEL.NS", "PNB.NS", "HAL.NS", "BHEL.NS",
        "PFC.NS", "RECL.NS", "NHPC.NS", "GMRINFRA.NS", "TATAPOWER.NS", "ADANIPOWER.NS"
    ]
    
    raw_pool_data = []
    
    # Resource 1: Dynamic Buying & Selling Activity Stream Filter
    for ticker in market_pool:
        try:
            stock = yf.Ticker(ticker)
            df = stock.history(period="5d", interval="1d")
            if df.empty or len(df) < 3:
                continue
                
            # Measure actual transaction velocity (Current volume multiplied by target price)
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
        
    # AUTOMATION FILTER: Pick only the top 8 assets with the absolute highest buyer/seller activity right now
    pool_df = pd.DataFrame(raw_pool_data)
    top_active_pool = pool_df.sort_values(by="activity", ascending=False).head(8)
    
    final_automated_feed = []
    
    for _, row in top_active_pool.iterrows():
        try:
            ticker = row['ticker']
            df = row['df']
            current_price = row['price']
            clean_name = ticker.replace(".NS", "")
            
            # Resource 2: Technical & Volume Trend Multi-Agents
            df['RSI'] = ta.momentum.rsi(df['Close'], window=14)
            df['SMA_20'] = df['Close'].rolling(window=2).mean()
            
            current_rsi = df['RSI'].iloc[-1]
            sma_20 = df['SMA_20'].iloc[-1]
            
            # Resource 3: Run real-time news scraper for this specific stock
            live_news_vector = fetch_live_news_sentiment(clean_name)
            
            # Core Quantum Score Logic
            score = 0
            if current_price > sma_20: score += 40
            if 40 <= current_rsi <= 65: score += 30
            if "🟢" in live_news_vector: score += 30
            if "🔴" in live_news_vector: score -= 20
            
            # Assign Actionable Direct Labels
            if score >= 70:
                signal = "🟢 STRONG BUY (HIGH VELOCITY)"
            elif 40 <= score < 70:
                signal = "🟡 HOLD / WAIT FOR BREAKOUT"
            else:
                signal = "🔴 AVOID / SELL (HEAVY DISTRIBUTION)"
                
            final_automated_feed.append({
                "🔥 Active Stock": clean_name,
                "💰 Live Price": f"₹{current_price:,.2f}",
                "📊 Automated Signal": signal,
                "🧬 Quant Score": f"{score}/100",
                "📰 Real-Time Live News Stream": live_news_vector
            })
        except Exception:
            continue
            
    return pd.DataFrame(final_automated_feed)
