import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib

df = yf.download("BRL=X", period="2y")

df['ret'] = np.log(df['Close']/df['Close'].shift(1))
df['vol'] = df['ret'].rolling(window=252).std() * np.sqrt(252)

df.to_excel("resultado.xlsx")

print(df)