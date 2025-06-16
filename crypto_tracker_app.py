
# crypto_tracker_app.py

import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("🚀 Cryptocurrency Price Tracker")
st.markdown("Get real-time and historical crypto data using CoinGecko API.")

coin = st.selectbox("Select Cryptocurrency", ["bitcoin", "ethereum", "dogecoin", "solana"])
days = st.selectbox("Select Period", [7, 30])

 # Real-time Price
price_url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
price_data = requests.get(price_url).json()
st.metric(label=f"{coin.title()} Current Price", value=f"${price_data[coin]['usd']}")

 # Historical Chart
hist_url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days={days}"
hist_data = requests.get(hist_url).json()
df = pd.DataFrame(hist_data['prices'], columns=["Timestamp", "Price"])
df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit='ms')

fig = px.line(df, x="Timestamp", y="Price", title=f"{coin.title()} Price in Last {days} Days")
st.plotly_chart(fig)
