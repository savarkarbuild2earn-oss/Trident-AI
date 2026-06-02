import yfinance as yf
import pandas as pd
import ta

def scan_stock(ticker, timeframe="Swing"):
    try:
        ticker_clean = ticker.strip().upper()
        if not ticker_clean.endswith(".NS"):
            ticker_clean = f"{ticker_clean}.NS"
            
        stock = yf.Ticker(ticker_clean)
        
        # CHOOSE DATA DEPLOYMENT STREAM BASED ON TIMEFRAME
        if timeframe == "Intraday":
            df = stock.history(period="15d", interval="5m")
            window_ma = 20
        else:
            df = stock.history(period="6mo", interval="1d")
            window_ma = 50
        
        if df.empty or len(df) < window_ma:
            return None
        
        current_price = df['Close'].iloc[-1]
        avg_volume = df['Volume'].mean()
        
        if avg_volume < 1000:
            return {"status": "BLOCKED", "reason": "Extremely low liquidity detected."}
        
        # ALGORITHMIC MULTI-TIMEFRAME INTERNALS
        df['RSI'] = ta.momentum.rsi(df['Close'], window=14)
        df['TREND_MA'] = df['Close'].rolling(window=window_ma).mean()
        df['EMA_FAST'] = df['Close'].ewm(span=12, adjust=False).mean()
        
        indicator_bb = ta.volatility.BollingerBands(close=df["Close"], window=20, window_dev=2)
        df['BB_Low'] = indicator_bb.bollinger_lband()
        
        current_rsi = df['RSI'].iloc[-1]
        trend_ma = df['TREND_MA'].iloc[-1]
        ema_fast = df['EMA_FAST'].iloc[-1]
        bb_low = df['BB_Low'].iloc[-1]
        
        # MULTI-AGENT SCORE ENGINE MATRIX
        score = 0
        reasons = []
        
        if current_price > trend_ma:
            score += 35
            reasons.append(f"Price holding above the {window_ma}-period baseline.")
        else:
            reasons.append(f"Price under pressure below the {window_ma}-period baseline.")
            
        if current_price > ema_fast:
            score += 25
            reasons.append("Short-term moving velocity tracking positively.")
        else:
            reasons.append("Short-term moving velocity tracking down.")
            
        if 40 <= current_rsi <= 65:
            score += 25
            reasons.append("RSI reflects a healthy consolidation channel.")
        elif current_rsi > 65:
            reasons.append("RSI indicators register overbought levels.")
        else:
            reasons.append("RSI structural decay confirms distribution.")
            
        if current_price < bb_low * 1.05:
            score += 15
            reasons.append("Price action near lower volatility boundaries.")
            
        if score >= 75:
            decision = f"🟢 BUY ({timeframe.upper()} CONFLUENCE EDGE)"
            explanation = f"Trident Engine Score: {score}/100. " + " ".join(reasons)
        elif 40 <= score < 75:
            # FIXED VISUAL TYPO HERE (REMOVED STRANGE TEXT CHARACTERS)
            decision = f"🟡 HOLD / WAIT FOR RALLY ENTRY"
            explanation = f"Trident Engine Score: {score}/100. " + " ".join(reasons)
        else:
            decision = f"🔴 AVOID / SELL ({timeframe.upper()} BREAKDOWN)"
            explanation = f"Trident Engine Score: {score}/100. " + " ".join(reasons)
            
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
