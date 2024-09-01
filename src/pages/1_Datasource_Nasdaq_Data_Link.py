import streamlit as st
import nasdaqdatalink as nasdaq

st.title("Nasdaq Data Link")
st.write("Fetching data from the Shardar data source for US equities, via the Nasdaq Data link platform")

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

if st.button("Fetch SHARADAR/SF1"):
    data = fetch_data("SHARADAR/SF1", ticker)
    if data is not None:
        st.write(f"Showing data for {ticker}")
        st.dataframe(data.head(10)) 

if st.button("Fetch SHARADAR/TICKERS"):
    data = fetch_data("SHARADAR/TICKERS", ticker)
    if data is not None:
        st.write(f"Showing data for {ticker}")
        st.dataframe(data.head(10)) 

if st.button("Fetch SHARADAR/METRICS"):
    data = fetch_data("SHARADAR/METRICS", ticker)
    if data is not None:
        st.write(f"Showing data for {ticker}")
        st.dataframe(data.head(10)) 

st.divider()

st.write("The next function pulls the schema for the whole parent data source tables")

if st.button("Fetch SHARADAR/INDICATORS (not ticker specific)"):
    data = fetch_data("SHARADAR/INDICATORS", None)
    if data is not None:
        st.write(f"Showing data for all tables")
        st.dataframe(data.head(10000)) 