# Stock-Portfolio-Tracker

# Stock Portfolio Tracker

This is a simple Stock Portfolio Tracker built using Python. The application provides an interactive GUI for users to manage their stock portfolio, view real-time stock prices, track portfolio performance, and visualize stock data using plots.

## Features

- **Add and Remove Stocks**: Easily add or remove stocks from your portfolio.
- **Portfolio Summary**: View the total value of your portfolio and track percentage gains/losses.
- **Real-Time Data**: Fetch real-time stock prices using the `yfinance` library.
- **Data Persistence**: Save your portfolio to a CSV file and load it automatically when you start the application.
- **Advanced Charts**: Visualize stock data with both static plots using `matplotlib` and interactive plots using `plotly`.

## Requirements

##To run this project, you'll need to install the following Python libraries:

#- `tkinter`: For building the GUI (included with standard Python distribution)
#- `yfinance`: To fetch stock data
#- `pandas`: For data manipulation
#- `matplotlib`: For static charts
#- `plotly`: For interactive charts

#You can install these libraries using `pip`:

#```bash
#pip install yfinance pandas matplotlib plotly'



#How to Use

#Clone the Repository:

#git clone https://github.com/your-username/stock-portfolio-tracker.git
#cd stock-portfolio-tracker

#Run the Application:

#python stock_portfolio_tracker.py


##Using the Application:

##Add Stocks: Enter the stock symbol (e.g., AAPL, GOOGL, etc.) in the input field and click the "Add Stock" button.
Remove Stocks: Select a stock from the list and click the "Remove Stock" button.
Update Portfolio: Click the "Update Portfolio" button to fetch the latest prices and view the total portfolio value and percentage gain/loss.
Plot Stock Data: Select a stock from the list and click the "Plot Stock" button to visualize the stock's recent performance.

Data Persistence:

Your portfolio is automatically saved to portfolio.csv in the project directory.
The portfolio will be loaded from this file every time you start the application.


File Structure
stock_portfolio_tracker.py: The main Python script containing the application code.
portfolio.csv: The CSV file where your portfolio is saved (automatically created).

Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.##


