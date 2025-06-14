
import streamlit as st
import yfinance as yf
import datetime

st.set_page_config(page_title="SmartStock AI", layout="centered")
st.title("📈 SmartStock AI – Stock Market Assistant")

ticker = st.text_input("Enter Stock Ticker Symbol (e.g. AAPL, TSLA, INFY):")

if ticker:
    try:
        end = datetime.datetime.now()
        start = end - datetime.timedelta(days=365)
        data = yf.download(ticker, start=start, end=end)
        
        st.subheader(f"Last 1 Year Price Chart for {ticker.upper()}")
        st.line_chart(data['Close'])

        st.write("📊 **Recent Data:**")
        st.dataframe(data.tail())

        st.success("✅ Data Fetched Successfully!")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
else:
    st.info("🔍 Please enter a valid stock symbol above.")
