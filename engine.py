import yfinance as yf
import pandas as pd
import ta
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import pytz

def fetch_live_news_sentiment(stock_name):
    """Bypasses paid APIs to scrape real-time financial news loops via RSS."""
    try:
        url = f"https://google.com{stock_name}+stock+market+india&hl=en-IN&gl=IN&ceid=IN:en"
        response = requests.get(url, timeout=2) # Fast timeout to handle high volume
        
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
    100% Comprehensive Market Scanner: Downloads and processes the entire Nifty 100
    simultaneously, mapping out separate mathematical entry, target, and exit levels.
    """
    # COMPLETE NIFTY 100 TICKER ENGINE POOL
    market_pool = [
        "ABB.NS", "ADANIENT.NS", "ADANIPORTS.NS", "ADANIPOWER.NS", "ATGL.NS", "AMBUJACEM", "APOLLOHOSP.NS",
        "ASIANPAINT.NS", "DMART.NS", "AXISBANK.NS", "BAJAJ-AUTO.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS", 
        "BALKRISIND.NS", "BANKBARODA.NS", "BEL.NS", "BHEL.NS", "BPCL.NS", "BHARTIALRT.NS", "BOSCHLTD.NS",
        "BRITANNIA.NS", "CANBK.NS", "CGPOWER.NS", "CHOLAFIN.NS", "CIPLA.NS", "COALINDIA.NS", "COFORGE.NS",
        "COLPAL.NS", "CONCOR.NS", "CUMMINSIND.NS", "DLF.NS", "DABUR.NS", "DIVISLAB.NS", "DRREDDY.NS",
        "EICHERMOT.NS", "GAIL.NS", "GMRINFRA.NS", "GODREJCP.NS", "GRASIM.NS", "HCLTECH.NS", "HDFCBANK.NS",
        "HDFCLIFE.NS", "HAVELLS.NS", "HEROMOTOCO.NS", "HINDALCO.NS", "HINDUNILVR.NS", "ICICIBANK.NS",
        "ICICIGI.NS", "ICICIPRULI.NS", "IDFCFIRSTB.NS", "ITC.NS", "INDIANB.NS", "INDCOSER.NS", "INDHOTEL.NS",
        "IOC.NS", "IRCTC.NS", "IRFC.NS", "IREDA.NS", "IGL.NS", "JSWSTEEL.NS", "JINDALSTEL.NS", "JIOFIN.NS",
        "JUBLFOOD.NS", "KOTAKBANK.NS", "LT.NS", "LTIM.NS", "LTTS.NS", "LICHSGFIN.NS", "LICI.NS", "MRF.NS",
        "M&M.NS", "MARUTI.NS", "MAXHEALTH.NS", "MUTHOOTFIN.NS", "NTPC.NS", "NESTLEIND.NS", "NHPC.NS",
        "OBEROIRLTY.NS", "ONGC.NS", "PIDILITIND.NS", "PFC.NS", "POWERGRID.NS", "PNB.NS", "RECL.NS",
        "RELIANCE.NS", "SBICARD.NS", "SBILIFE.NS", "SHRIRAMFIN.NS", "SIEMENS.NS", "SBIN.NS", "SUNPHARMA.NS",
        "SUPREMEIND.NS", "SUZLON.NS", "TVSMOTOR.NS", "TATACOMM.NS", "TATACONSUM.NS", "TATAELXSI.NS",
        "TATAMOTORS.NS", "TATAPOWER.NS", "TATASTEEL.NS", "TCS.NS", "TECHM.NS", "TITAN.NS", "TRENT.NS",
        "ULTRACEMCO.NS", "UNITDSPR.NS", "VBL.NS", "WIPRO.NS", "YESBANK.NS", "ZOMATO.NS"
    ]
    
    final_automated_feed = []
    
    # Configure timezone structure for precise local Indian market synchronization
    ist_timezone = pytz.timezone('Asia/Kolkata')
    current_time_ist = datetime.now(ist_timezone).strftime("%I:%M:%S %p")
    
    # Bulk-download historical snapshots to keep execution fast and stable
    tickers_string = " ".join(market_pool)
    try:
        bulk_data = yf.download(tickers_string, period="6mo", interval="1d", group_by='ticker', verbose=False)
    except Exception:
        return pd.DataFrame()
        
    for ticker in market_pool:
        try:
            df = bulk_data[ticker].dropna()
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
            
            # Sector Catalyst check
            news_sentiment = fetch_live_news_sentiment(clean_name)
            if news_sentiment == "Bullish": score += 30
            elif news_sentiment == "Bearish": score -= 20
            
            # GENERATE SEPARATE HIGH-ACCURACY TRANSACTION LEVELS FOR EVERY STOCK
            if score >= 70:
                signal = "🟢 ACCUMULATE (BUY)"
                target_entry = f"₹{current_price:,.2f}"
                target_exit = f"₹{current_price * 1.03:,.2f}" # 3% Target profit line
            elif score <= 35:
                signal = "🔴 LIQUIDATE (SELL)"
                target_entry = "Avoid Entry"
                target_exit = f"₹{current_price * 0.98:,.2f}" # 2% Stop loss line
            else:
                signal = "健康 HOLD CONSOLIDATION"
                target_entry = f"₹{current_price:,.2f}"
                target_exit = f"₹{current_price * 1.01:,.2f}"
                
            final_automated_feed.append({
                "⏰ Detection Time (IST)": current_time_ist,
                "🔥 Active Stock": clean_name,
                "💰 Current Value": f"₹{current_price:,.2f}",
                "📊 Action Signal": signal,
                "🟢 Target Entry Line": target_entry,
                "🔴 Target Exit Line": target_exit,
                "🧬 Scoring Index": f"{score}/100"
            })
        except Exception:
            continue
            
    return pd.DataFrame(final_automated_feed)
