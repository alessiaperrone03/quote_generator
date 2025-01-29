import tkinter as tk
import requests

# Function to fetch a random quote from ZenQuotes API
def generate_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data[0]["q"]
        author = quote_data[0]["a"]
        return f'"{quote}" - {author}'
    else:
        return "Sorry, could not fetch a quote at the moment."

# Function to update the quote on the GUI
def update_quote():
    quote = generate_quote()
    quote_label.config(text=quote)
    save_quote(quote)

# Function to save the quote to a text file
def save_quote(quote):
    with open("quotes.txt", "a") as file:
        file.write(quote + "\n")

# Create the main window
root = tk.Tk()
root.title("Quote Generator")

# Set window size
root.geometry("400x300")

# Create a label to display the quote
quote_label = tk.Label(root, text="Your quote will appear here", wraplength=350, font=("Arial", 14), justify="center")
quote_label.pack(pady=20)

# Create a button to get a new quote
get_quote_button = tk.Button(root, text="Get Quote", command=update_quote, font=("Arial", 12))
get_quote_button.pack(pady=10)

# Create a button to quit the application
quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 12))
quit_button.pack(pady=10)

# Run the main loop
root.mainloop()
