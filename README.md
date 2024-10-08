# risk-playground
A toy project using Python, Streamlit, [Toraniko](https://github.com/0xfdf/toraniko) (open source risk model), and the Nasdaq Data Link API.


This app allows you to fetch and display stock data for a specified ticker symbol. Enter a ticker symbol (e.g., AAPL), and the app will display the first 10 rows of data along with a chart of the closing prices.

## Datasource
I'm using the Nasdaq Data Link (formerly Quandl) to fetch stock price data. You can sample a handful of tickers (once you have a free API key).
The aim is to use the full data set to run the risk model.

## Notebooks
There are some exploratory notebooks in the `notebooks` folder. To ensure that sensitive data (from the API) and large outputs (such as tables and plots) are not accidentally committed to the repository, I've added `nbstripout` as a dev package. This tool automatically strips output from notebooks (`*.ipynb` files) before they are committed.

**NB: Enable `nbstripout` locally**: After installing the poetry dependencies, you need to configure `nbstripout` for your local Git repository. Run the following command:
```bash
poetry run nbstripout --install
```
This does the following:
* Setting up a Git filter named `nbstripout` in your local Git configuration.
* Adding or updating a `.gitattributes` file in your repository to associate the `nbstripout` filter with all `.ipynb` files.

## Running the Streamlit App
To run the Streamlit app for this project, follow these steps:

### 1. Install Dependencies
This project is Python with Poetry.
Ensure you have all the necessary dependencies installed via Poetry.

```bash 
poetry install 
```

### 2. Set Up the API Key
This app uses the nasdaq-data-link package to fetch stock data from the Sharadar Equity Prices dataset. 

First, visit https://data.nasdaq.com/sign-up to create an account. This will give you an API key.

Secondly, add the key to your local environment. A few ways to do this, I suggest:

- Windows: Create a file at `C:\Users\<YourUsername>\.nasdaq\data_link_apikey` containing your API key. 
- Unix: Create a file at ~/.nasdaq/data_link_apikey containing your API key.

### 3. Run the Streamlit App
You can run the Streamlit app directly using Python with the following command:

```bash 
poetry run streamlit run src\Homepage.py
```