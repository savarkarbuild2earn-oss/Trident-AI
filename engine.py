import yfinance as yf
import pandas as pd
import ta
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import pytz

def fetch_live_news_sentiment(stock_name):
    """Scrapes real-time financial headlines via Google News RSS."""
    try:
        url = f"https://google.com{stock_name}+stock+market+india&hl=en-IN&gl=IN&ceid=IN:en"
        response = requests.get(url, timeout=1.5)
        if response.status_code != 200:
            return "Neutral"
        root = ET.fromstring(response.content)
        headlines = [item.find('title').text for item in root.findall('.//item')[:2]]
        if not headlines:
            return "Neutral"
            
        p_words = ['profit', 'surge', 'buy', 'order', 'growth', 'deal', 'gain', 'dividend', 'win', 'bull']
        n_words = ['fall', 'loss', 'drop', 'slump', 'scam', 'probe', 'penalty', 'decline', 'bear']
        
        score = 0
        for headline in headlines:
            text = headline.lower()
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
    Hands-Free Engine: Processes the entire official Nifty 100 pool,
    sorting long-term structures into precise ascending monthly holdings.
    """
    # ENTIRE 100 STOCKS COMPREHENSIVE NSE LIST POOL
    nifty_100_pool = [
        "ABB.NS", "ADANIENT.NS", "ADANIPORTS.NS", "ADANIPOWER.NS", "ATGL.NS", "AMBUJACEM.NS", "APOLLOHOSP.NS",
        "ASIANPAINT.NS", "DMART.NS", "AXISBANK.NS", "BAJAJ-AUTO.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS", 
        "BALKRISIND.NS", "BANKBARODA.NS", "BEL.NS", "BHEL.NS", "BPCL.NS", "BHARTIALRT.NS", "BOSCHLTD.NS",
        "BRITANNIA.NS", "CANBK.NS", "CGPOWER.NS", "CHOLAFIN.NS", "CIPLA.NS", "COALINDIA.NS", "COFORGE.NS",
        "COLPAL.NS", "CONCOR.NS", "CUMMINSIND.NS", "DLF.NS", "DABUR.NS", "DIVISLAB.NS", "DRREDDY.NS",
        "EICHERMOT.NS", "GAIL.NS", "GMRINFRA.NS", "GODREJCP.NS", "GRASIM.NS", "HCLTECH.NS", "HDFCBANK.NS",
        "HDFCLIFE.NS", "HAVELLS.NS", "HEROMOTOCO.NS", "HINDALCO.NS", "HINDUNILVR.NS", "ICICIBANK.NS",
        "ICICIGI.NS", "ICICIPRULI.NS", "IDFCFIRSTB.NS", "ITC.NS", "INDIANB.NS", "INDHOTEL.NS",
        "IOC.NS", "IRCTC.NS", "IRFC.NS", "IREDA.NS", "IGL.NS", "JSWSTEEL.NS", "JINDALSTEL.NS", "JIOFIN.NS",
        "JUBLFOOD.NS", "KOTAKBANK.NS", "LT.NS", "LTIM.NS", "LTTS.NS", "LICHSGFIN.NS", "LICI.NS", "MRF.NS",
        "M&M.NS", "MARUTI.NS", "MAXHEALTH.NS", "MUTHOOTFIN.NS", "NTPC.NS", "NESTLEIND.NS", "NHPC.NS",
        "OBEROIRLTY.NS", "ONGC.NS", "PIDILITIND.NS", "PFC.NS", "POWERGRID.NS", "PNB.NS", "RECL.NS",
        "RELIANCE.NS", "SBICARD.NS", "SBILIFE.NS", "SHRIRAMFIN.NS", "SIEMENS.NS", "SBIN.NS", "SUNPHARMA.NS",
        "SUPREMEIND.NS", "SUZLON.NS", "TVSMOTOR.NS", "TATACOMM.NS", "TATACONSUM.NS", "TATAELXSI.NS",
        "TATAMOTORS.NS", "TATAPOWER.NS", "TATASTEEL.NS", "TCS.NS", "TECHM.NS", "TITAN.NS", "TRENT.NS",
        "ULTRACEMCO.NS", "UNITDSPR.NS", "VBL.NS", "WIPRO.NS", "YESBANK.NS", "ZOMATO.NS"
    ]
    
    intraday_list = []
    longterm_list = []
    
    ist_tz = pytz.timezone('Asia/Kolkata')
    current_time_ist = datetime.now(ist_tz).strftime("%I:%M %p")
    
    # Bulk pulling daily slices for full 6 months to maintain rapid calculation speeds
    tickers_string = " ".join(nifty_100_pool)
    try:
        bulk_data = yf.download(tickers_string, period="6mo", interval="1d", group_by='ticker', verbose=False)
    except Exception:
        return pd.DataFrame(), pd.DataFrame()
        
    for ticker in nifty_100_pool:
        try:
            df = bulk_data[ticker].dropna()
            if df.empty or len(df) < 50: continue
                
            current_price = df['Close'].iloc[-1]
            clean_name = ticker.replace(".NS", "")
            
            # Indicator matrices
            df['RSI'] = ta.momentum.rsi(df['Close'], window=14)
            df['SMA_20'] = df['Close'].rolling(window=20).mean()
            df['SMA_50'] = df['Close'].rolling(window=50).mean()
            
            current_rsi = df['RSI'].fillna(50).iloc[-1]
            sma_20 = df['SMA_20'].fillna(current_price).iloc[-1]
            sma_50 = df['SMA_50'].fillna(current_price).iloc[-1]
            
            news_sentiment = fetch_live_news_sentiment(clean_name)
            
            # Calculate underlying confluence weights
            score = 0
            if current_price > sma_20: score += 40
            if 40 <= current_rsi <= 65: score += 30
            if news_sentiment == "Bullish": score += 30
            if news_sentiment == "Bearish": score -= 20
            
            # 1. INTRADAY DATA LAYER STREAM
            if score >= 70:
                intra_signal = "🟢 ACCUMULATE"
                intra_exit = f"₹{current_price * 1.02:,.2f}"
            elif score <= 35:
                intra_signal = "🔴 LIQUIDATE"
                intra_exit = f"₹{current_price * 0.985:,.2f}"
            else:
                intra_signal = "官方 HOLD RANGE"
                intra_exit = f"₹{current_price * 1.005:,.2f}"
                
            intraday_list.append({
                "⏰ Time": current_time_ist,
                "🔥 Stock": clean_name,
                "💰 Price": f"₹{current_price:,.2f}",
                "📊 Intraday Signal": intra_signal,
                "🟢 Entry Line": f"₹{current_price:,.2f}",
                "🔴 Exit Line": intra_exit,
                "⏳ Hold Duration": "⏰ Same Day (Exit 3:15 PM)" if score != 50 else "⏳ 1-2 Trading Days",
                "🧬 Score": int(score)
            })
            
            # 2. LONG-TERM ASCENDING VALUE MATURATION LAYER
            # Sort holding structures sequentially based on standard moving line distances
            if current_price > sma_50 * 1.15:
                long_outlook = "🚀 ACCELERATED RUN"
                long_period = "💎 1 Month (Fast Swing Momentum)"
                long_target = f"₹{current_price * 1.08:,.2f}"
            elif sma_50 * 1.05 < current_price <= sma_50 * 1.15:
                long_outlook = "📈 SOLID COMPOUNDER"
                long_period = "💎 3 Months (Quarterly Trend Re-rate)"
                long_target = f"₹{current_price * 1.15:,.2f}"
            elif sma_50 <= current_price <= sma_50 * 1.05:
                long_outlook = "⚖️ BASE ACCUMULATION"
                long_period = "💎 6 Months (Structural Rebuilding)"
                long_target = f"₹{current_price * 1.22:,.2f}"
            else:
                long_outlook = "📉 BEARING RE-TEST"
                long_period = "💎 12+ Months (Macro Cyclical Hold)"
                long_target = f"₹{current_price * 1.35:,.2f}"
                
            longterm_list.append({
                "🔥 Stock": clean_name,
                "💰 Value": f"₹{current_price:,.2f}",
                "📊 Long-Term Outlook": long_outlook,
                "📅 Entry Execution Window": "Current Trading Week",
                "🎯 Macro Target Exit Line": long_target,
                "⏳ Recommended Hold Period": long_period
            })
        except Exception:
            continue
            
    return pd.DataFrame(intraday_list), pd.DataFrame(longterm_list)
