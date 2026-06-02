import yfinance as yf
import pandas as pd
import ta

def scan_stock(ticker):
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period="6mo", interval="1d")
        if df.empty:
            return None
        
        info = stock.info
        market_cap = info.get("marketCap", 0)
        avg_volume = info.get("averageVolume", 0)
        
        # ==============================================================================
        # CO-FOUNDER GUARDRAIL: ANTI-PUMP-AND-DUMP FILTER
        # ==============================================================================
        if market_cap < 5000000000 or avg_volume < 50000:
            return {"status": "BLOCKED", "reason": "High manipulation risk / low liquidity criteria flagged."}
        
        # BULLETPROOF MATHEMATICAL CALCULATIONS (Using Pandas direct rolling math)
        df['RSI'] = ta.momentum.rsi(df['Close'], window=14)
        df['SMA_50'] = df['Close'].rolling(window=50).mean() # Native Pandas (Zero error risk)
        df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean() # Native Pandas (Zero error risk)
        
        # Bollinger Bands using standard ta utilities
        indicator_bb = ta.volatility.BollingerBands(close=df["Close"], window=20, window_dev=2)
        df['BB_High'] = indicator_bb.bollinger_hband()
        df['BB_Low'] = indicator_bb.bollinger_lband()
        
        current_price = df['Close'].iloc[-1]
        current_rsi = df['RSI'].iloc[-1]
        sma_50 = df['SMA_50'].iloc[-1]
        ema_20 = df['EMA_20'].iloc[-1]
        bb_high = df['BB_High'].iloc[-1]
        bb_low = df['BB_Low'].iloc[-1]
        
        # ==============================================================================
        # ALGOCALC: MULTI-AGENT SCORING MATRIX
        # ==============================================================================
        score = 0
        reasons = []
        
        # Analyst 1: Long-Term Trend Agent
        if current_price > sma_50:
            score += 35
            reasons.append("Stock is trading over its long-term baseline (Bullish Structure).")
        else:
            reasons.append("Stock is trading under its long-term baseline (Bearish Structure).")
            
        # Analyst 2: Short-Term Velocity Agent
        if current_price > ema_20:
            score += 25
            reasons.append("Short-term momentum acceleration confirmed.")
            
        # Analyst 3: Momentum Range Agent
        if 40 <= current_rsi <= 65:
            score += 25
            reasons.append("RSI shows stable buying demand without being overbought.")
        elif current_rsi > 65:
            reasons.append("RSI flags extreme overbought levels. Entry carries near-term distribution risks.")
        else:
            reasons.append("RSI indicates weak relative strength / markdown phase.")
            
        # Analyst 4: Volatility Band Agent
        if current_price < bb_low * 1.05:
            score += 15
            reasons.append("Price is reacting near the lower Bollinger margin (Potential Value Zone).")
            
        # FINAL UNIFIED RATING ROUTER
        if score >= 75:
            decision = "🟢 BUY (STRONG ALGORITHMIC EDGE)"
            explanation = f"Trident Scoring Index: {score}/100. High-confluence matching across standard metrics. " + " ".join(reasons)
        elif 40 <= score < 75:
            decision = "🟡 HOLD / WAIT FOR DIAL-IN"
            explanation = f"Trident Scoring Index: {score}/100. Mixed signals registered. Assets are stabilizing. " + " ".join(reasons)
        else:
            decision = "🔴 AVOID / SELL (HIGH DISTRIBUTION)"
            explanation = f"Trident Scoring Index: {score}/100. Severe technical distribution. High correlation to further weakness. " + " ".join(reasons)
            
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
