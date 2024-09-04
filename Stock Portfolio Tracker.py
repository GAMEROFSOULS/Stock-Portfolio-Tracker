import tkinter as tk
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

portfolio = []

# Load portfolio from CSV
def load_portfolio():
    try:
        df = pd.read_csv('portfolio.csv')
        for index, row in df.iterrows():
            portfolio.append(row['Stock'])
            stock_listbox.insert(tk.END, row['Stock'])
    except FileNotFoundError:
        pass

# Save portfolio to CSV
def save_portfolio():
    df = pd.DataFrame(portfolio, columns=['Stock'])
    df.to_csv('portfolio.csv', index=False)

# Add stock to portfolio
def add_stock():
    stock = stock_entry.get()
    if stock:
        portfolio.append(stock)
        stock_listbox.insert(tk.END, stock)
        stock_entry.delete(0, tk.END)
        save_portfolio()

# Remove stock from portfolio
def remove_stock():
    selected_stock = stock_listbox.curselection()
    if selected_stock:
        stock = stock_listbox.get(selected_stock)
        portfolio.remove(stock)
        stock_listbox.delete(selected_stock)
        save_portfolio()

# Update portfolio and show stock prices
def update_portfolio():
    total_value = 0
    initial_value = 0
    prices = []

    for stock in portfolio:
        data = yf.download(stock, period="1d")
        price = data['Close'].iloc[-1]
        prices.append(f"{stock}: ${price:.2f}")
        
        # Assume initial value is the price at some historical point (e.g., 1 year ago)
        historical_data = yf.download(stock, period="1y")
        initial_price = historical_data['Close'].iloc[0]
        initial_value += initial_price
        total_value += price
    
    prices_label.config(text="\n".join(prices))
    
    # Calculate and display portfolio summary
    total_label.config(text=f"Total Value: ${total_value:.2f}")
    gain_loss = (total_value - initial_value) / initial_value * 100
    gain_loss_label.config(text=f"Portfolio Gain/Loss: {gain_loss:.2f}%")

# Plot stock data
def plot_stock():
    selected_stock = stock_listbox.curselection()
    if selected_stock:
        stock = stock_listbox.get(selected_stock)
        data = yf.download(stock, period="1mo")
        
        # Matplotlib Plot
        plt.figure(figsize=(10, 6))
        plt.plot(data['Close'], label=f'{stock} Price')
        plt.title(f"{stock} - Last 1 Month")
        plt.xlabel("Date")
        plt.ylabel("Close Price")
        plt.legend()
        plt.grid(True)
        plt.show()
        
        # Plotly Plot (interactive)
        fig = go.Figure(data=[go.Scatter(x=data.index, y=data['Close'], mode='lines', name=stock)])
        fig.update_layout(title=f"{stock} - Last 1 Month", xaxis_title="Date", yaxis_title="Close Price")
        fig.show()

# GUI Setup
root = tk.Tk()
root.title("Stock Portfolio Tracker")
root.geometry("600x600")

stock_entry = tk.Entry(root)
stock_entry.pack()

stock_listbox = tk.Listbox(root)
stock_listbox.pack()

add_button = tk.Button(root, text="Add Stock", command=add_stock)
add_button.pack()

remove_button = tk.Button(root, text="Remove Stock", command=remove_stock)
remove_button.pack()

update_button = tk.Button(root, text="Update Portfolio", command=update_portfolio)
update_button.pack()

plot_button = tk.Button(root, text="Plot Stock", command=plot_stock)
plot_button.pack()

prices_label = tk.Label(root, text="")
prices_label.pack()

total_label = tk.Label(root, text="Total Value: $0.00")
total_label.pack()

gain_loss_label = tk.Label(root, text="Portfolio Gain/Loss: 0.00%")
gain_loss_label.pack()

# Load portfolio when starting the app
load_portfolio()

root.mainloop()
