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

To run this project, you'll need to install the following Python libraries:

- `tkinter`: For building the GUI (included with standard Python distribution)
- `yfinance`: To fetch stock data
- `pandas`: For data manipulation
- `matplotlib`: For static charts
- `plotly`: For interactive charts

You can install these libraries using `pip`:

```bash
pip install yfinance pandas matplotlib plotly
