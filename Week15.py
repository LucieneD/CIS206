import tkinter as tk

def calculate():
    name = name_entry.get()
    hours = hours_entry.get()

    # Check if hours is a number
    if not hours.isdigit():
        result_label.config(text="Error: Enter a number for hours.")
        return

    pay = int(hours) * 20  # Multiply hours by hourly rate
    result = f"Hi {name}, you earned ${pay}!"
    result_label.config(text=result)

# Create the main window
window = tk.Tk()
window.title("Pay Calculator")
window.geometry("300x200")

# Name input
tk.Label(window, text="Name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Hours input
tk.Label(window, text="Hours Worked:").pack()
hours_entry = tk.Entry(window)
hours_entry.pack()

# Button to calculate
tk.Button(window, text="Calculate Pay", command=calculate).pack()

# Label to show result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the program
window.mainloop()
