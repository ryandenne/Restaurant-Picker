import tkinter as tk
import random
import pandas as pd

def load_restaurants(): # Manage excel list of restaurants
    df = pd.read_excel(r'C:\Users\ryanj\OneDrive\Documents\Python Scripts\Restaurants.xlsx')
    return df['Restaurants'].tolist()

def add_restaurant(): # Add restaurant manually/temporarily
    restaurant = entry.get()
    if restaurant:
        restaurants.append(restaurant)
        entry.delete(0, tk.END)
        update_listbox()

def randomize_restaurant(): #Randomizer FUnction
    if restaurants:
        chosen = random.choice(restaurants)
        result_label.config(text=f"How about {chosen}", font=("Helvitica", 16, "bold"), bg="yellow")
        flash_label(6) # Flash Count

def flash_label(count):
    if count > 0:
        current_color = result_label.cget("bg")
        new_color = "yellow" if current_color == root.cget('bg') else root.cget('bg')
        result_label.config(bg=new_color)
        root.after(500, flash_label, count - 1) # Flash effect

def update_listbox():
    listbox.delete(0, tk.END)
    for restaurant in restaurants:
        listbox.insert(tk.END, restaurant)

# Set up the main window
root = tk.Tk()
root.title("Where to Eat?")
root.geometry("300x500")

# Initialize restaurant list
restaurants = load_restaurants()

# Listbox to display restaurants
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)
update_listbox()

# Entry to add new restaurants
entry = tk.Entry(root)
entry.pack()

# Buttons to add and randomize
add_button = tk.Button(root, text="Add Restaurant", command=add_restaurant)
add_button.pack()

randomize_button = tk.Button(root, text="Pick a Restaurant", command=randomize_restaurant)
randomize_button.pack()

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
