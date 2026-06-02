import yfinance as yf
import pandas as pd
import ta

def scan_stock(ticker):
    try:
        # Standardize the symbol
        ticker_clean = ticker.strip().upper()
        if not ticker_clean.endswith(".NS"):
            ticker_clean = f"{ticker_clean}.NS"
            
        stock = yf.Ticker(ticker_clean)
        # Pull 6 months of historical data directly
        df = stock.history(period="6mo", interval="1d")
        
        if df.empty or len(df) < 50:
            return None
        
        # Calculate historical price metrics directly to check safety without needing stock.info
        current_price = df['Close'].iloc[-1]
        avg_volume = df['Volume'].mean()
        
        # CO-FOUNDER SHIELD: Block highly volatile micro-cap tokens
        if avg_volume < 5000:
            return {"status": "BLOCKED", "reason": "Low daily trading activity criteria flagged."}
        
        # QUANTITATIVE INDICATOR MATHEMATICS
        df['RSI'] = ta.momentum.rsi(df['Close'], window=14)
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
        
        indicator_bb = ta.volatility.BollingerBands(close=df["Close"], window=20, window_dev=2)
        df['BB_Low'] = indicator_bb.bollinger_lband()
        
        current_rsi = df['RSI'].iloc[-1]
        sma_50 = df['SMA_50'].iloc[-1]
        ema_20 = df['EMA_20'].iloc[-1]
        bb_low = df['BB_Low'].iloc[-1]
        
        # MULTI-AGENT SCORE CARD PIPELINE
        score = 0
        reasons = []
        
        if current_price > sma_50:
            score += 35
            reasons.append("Trading over long-term support metrics.")
        else:
            reasons.append("Trading below long-term moving baseline.")
            
        if current_price > ema_20:
            score += 25
            reasons.append("Short-term buying acceleration confirmed.")
            
        if 40 <= current_rsi <= 65:
            score += 25
            reasons.append("RSI shows sustainable buyer momentum.")
        elif current_rsi > 65:
            reasons.append("Asset values flag near-term overbought conditions.")
        else:
            reasons.append("RSI indicators signal markdown structural weakness.")
            
        if current_price < bb_low * 1.05:
            score += 15
            reasons.append("Price action trading near lower volatility boundaries.")
            
        # GENERATE SYSTEM RATINGS
        if score >= 75:
            decision = "🟢 BUY (STRONG ALGORITHMIC EDGE)"
            explanation = f"Trident Engine Score: {score}/100. Confluence verified. " + " ".join(reasons)
        elif 40 <= score < 75:
            decision = "🟡 HOLD / WATCH FOR DIAL-IN"
            explanation = f"Trident Engine Score: {score}/100. Mixed conditions tracked. " + " ".join(reasons)
        else:
            decision = "🔴 AVOID / SELL (HIGH DISTRIBUTION)"
            explanation = f"Trident Engine Score: {score}/100. Major distribution trends. " + " ".join(reasons)
            
        return {
            "status": "SUCCESS",
            "price": round(current_price, 2),
            "decision": decision,
            "explanation": explanation,
            "raw_score": score,
            "rsi": round(current_rsi, 2)
        }
    except Exception as e:
        return {"status": "ERROR", "reason": str(e)}
