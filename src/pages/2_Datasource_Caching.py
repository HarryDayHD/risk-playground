import streamlit as st
import nasdaqdatalink as nasdaq
import pandas as pd

sample_tickers = pd.DataFrame([
    ("AAPL","APPLE INC"),
    ("AXP","AMER EXPRESS CO"),
    ("BA","BOEING CO"),
    ("CAT","CATERPILLAR INC"),
    ("CSCO","CISCO SYSTEMS"),
    ("CVX","CHEVRON CORP"),
    ("DD","DU PONT (EI) DE"),
    ("DIS","DISNEY WALT"),
    ("GE","GENL ELECTRIC"),
    ("GS","GOLDMAN SACHS"),
    ("HD","HOME DEPOT"),
    ("IBM","INTL BUS MACH"),
    ("INTC","INTEL CORP"),
    ("JNJ","JOHNSON & JOHNS"),
    ("JPM","JPMORGAN CHASE"),
    ("KO","COCA COLA CO"),
    ("MCD","MCDONALDS CORP"),
    ("MMM","3M CO"),
    ("MRK","MERCK & CO INC"),
    ("MSFT","MICROSOFT CORP"),
    ("NKE","NIKE INC-B"),
    ("PFE","PFIZER INC"),
    ("PG","PROCTER & GAMBL"),
    ("TRV","TRAVELERS COS"),
    ("UNH","UNITEDHEALTH GP"),
    ("UTX","UTD TECHS CORP"),
    ("V","VISA INC-A"),
    ("VZ","VERIZON COMM"),
    ("WMT","WALMART INC"),
    ("XOM","EXXON MOBIL CRP"),
], columns=['Ticker', 'Company Name'])

st.write("Sample tickers")
st.dataframe(sample_tickers)

if st.button("Download all data"):
    price_data = nasdaq.get_table("SHARADAR/SEP")
    st.dataframe (price_data)