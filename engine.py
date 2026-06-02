import yfinance as yf
import pandas as pd
import ta  # Using the updated, stable library

def scan_stock(ticker):
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period="3mo", interval="1d")
        if df.empty:
            return None
        
        info = stock.info
        market_cap = info.get("marketCap", 0)
        avg_volume = info.get("averageVolume", 0)
        
        # SAFETY SHIELD: Filter out micro-cap pump-and-dumps (under 500 Crores)
        if market_cap < 5000000000 or avg_volume < 50000:
            return {"status": "BLOCKED", "reason": "High manipulation risk / low liquidity."}
        
        # ALGORITHMIC LOGIC using our new stable library
        df['RSI'] = ta.momentum.rsi(df['Close'], window=14)
        df['SMA_50'] = ta.trend.sma_indicator(df['Close'], window=50)
        
        current_price = df['Close'].iloc[-1]
        current_rsi = df['RSI'].iloc[-1]
        sma_50 = df['SMA_50'].iloc[-1]
        
        # SIGNAL GENERATION
        if current_price > sma_50 and current_rsi < 70:
            decision = "🟢 BUY (STRONG MOMENTUM)"
            explanation = "The stock is stable, trading above its 50-day average, and is not overbought."
        elif current_rsi >= 70:
            decision = "🟡 HOLD / WAIT"
            explanation = "The stock is in a strong uptrend but currently overbought. Wait for a minor dip."
        else:
            decision = "🔴 AVOID / SELL"
            explanation = "The stock is trading below its safety line. High risk of further falling."
            
        return {
            "status": "SUCCESS",
            "price": round(current_price, 2),
            "decision": decision,
            "explanation": explanation
        }
    except Exception as e:
        return {"status": "ERROR", "reason": str(e)}
