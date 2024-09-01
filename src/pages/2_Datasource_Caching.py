import streamlit as st
import nasdaqdatalink as nasdaq


def fetch_data(table: str, ticker: str):
    try:
        data = nasdaq.get_table(table, ticker={ticker})
        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

ticker = st.text_input("Enter ticker symbol (e.g., AAPL):", value="AAPL")

if st.button("Fetch SHARADAR/SEP"):
    data = fetch_data("SHARADAR/SEP", ticker)
    if data is not None:
        st.write(f"Showing data for {ticker}")
        st.dataframe(data.head(10)) 
        st.line_chart(data['close'])
