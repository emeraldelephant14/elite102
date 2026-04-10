
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Banking App")
    label = tk.Label(root, text="Welcome!")
    label.pack()
    btn = tk.Button(root, text="Check Balance")
    btn.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
