import tkinter as tk
import math

def click(event):
    current = entry.get()
    button_text = event.widget.cget("text")

    try:
        if button_text == "=":
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))

        elif button_text == "C":
            entry.delete(0, tk.END)

        elif button_text == "√":
            result = math.sqrt(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))

        elif button_text == "^":
            entry.insert(tk.END, "**")

        elif button_text == "π":
            entry.insert(tk.END, str(math.pi))

        elif button_text == "e":
            entry.insert(tk.END, str(math.e))

        elif button_text == "sin":
            result = math.sin(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))

        elif button_text == "cos":
            result = math.cos(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))

        elif button_text == "tan":
            result = math.tan(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))

        elif button_text == "log":
            result = math.log10(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))

        elif button_text == "ln":
            result = math.log(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))

        else:
            entry.insert(tk.END, button_text)

    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# GUI setup
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x550")

entry = tk.Entry(root, font="Arial 24")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

# Buttons grid
buttons = [
    ['7', '8', '9', '/', '√'],
    ['4', '5', '6', '*', '^'],
    ['1', '2', '3', '-', 'π'],
    ['0', '.', '=', '+', 'e'],
    ['sin', 'cos', 'tan', 'log', 'ln'],
    ['C']
]

for row in buttons:
    frame = tk.Frame(root)
    for label in row:
        btn = tk.Button(frame, text=label, font="Arial 18", width=6, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)
    frame.pack()

root.mainloop()
