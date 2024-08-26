import streamlit as st
import nasdaqdatalink as nasdaq

def fetch_data(ticker: str):
    try:
        data = nasdaq.get_table('SHARADAR/SEP', ticker={ticker})
        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None
    
def main():
    st.title("Risk Playground")
    st.write("Currently: NASDAQ-Data-Link -> [Sharadar Equity Prices] Fetching App")

    ticker = st.text_input("Enter ticker symbol (e.g., AAPL):", value="AAPL")
    
    if st.button("Fetch Data"):
        data = fetch_data(ticker)
        if data is not None:
            st.write(f"Showing data for {ticker}")
            st.dataframe(data.head(10)) 
            st.line_chart(data['close'])

if __name__ == "__main__":
    main()