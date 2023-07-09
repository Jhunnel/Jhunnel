import tkinter as tk

def secant_method(f, x0, x1, tol, max_iter):

    def update_label():
        nonlocal i, x0, x1, x2
        label.config(text=f"Iteration {i+1}: x0 = {x0}, x1 = {x1}, x2 = {x2}")
        root.update()

    i = 0
    root_prev = x1  # initialize root_prev with x1
    while i < max_iter:
        fx0 = f(x0)
        fx1 = f(x1)
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        label.after(1000, update_label) # update label every second

        if abs(x2 - x1) < tol:
            if abs(x2 - root_prev) < tol:
                return x2
            root_prev = x2
          
        x0, x1 = x1, x2
        i += 1

    raise ValueError(f"Secant method did not converge after {max_iter} iterations")

# Define function f globally
f = lambda x: x**2 - 2

def solve():
    # Get values from Entry widgets
    x0 = float(x0_entry.get())
    x1 = float(x1_entry.get())
    tol = float(tol_entry.get())

    result = secant_method(f, x0, x1, tol, max_iter)
    label.config(text=f"Root: {result}")

# Create GUI
root = tk.Tk()
root.title("Secant Method Solver")

f_label = tk.Label(root, text="f(x) = x^2 - 2")
f_label.pack()

x0_label = tk.Label(root, text="Initial guess (x0):")
x0_label.pack()
x0_var = tk.StringVar()
x0_entry = tk.Entry(root, textvariable=x0_var)
x0_entry.pack()

x1_label = tk.Label(root, text="Initial guess (x1):")
x1_label.pack()
x1_var = tk.StringVar()
x1_entry = tk.Entry(root, textvariable=x1_var)
x1_entry.pack()

tol_label = tk.Label(root, text="Tolerance:")
tol_label.pack()
tol_var = tk.StringVar()
tol_entry = tk.Entry(root, textvariable=tol_var)
tol_entry.pack()

max_iter = 7

button = tk.Button(root, text="Solve", command=solve)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
