import tkinter as tk

# Won't work in the Codespace web UI, but you can run this on VS Code on your machine.
# Go to GitHub repoo > Code > Open with Codespaces > click three dots > Open in Visual Studio Code
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
