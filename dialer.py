import tkinter as tk

def create_keypad():
    # Function to handle button clicks
    def button_click(value):
        current_text = text_area.get()
        text_area.set(current_text + value)
    
    # Function to copy text to clipboard
    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(text_area.get())
        root.update()  # Ensures clipboard is updated
    
    root = tk.Tk()
    root.title("Keypad")

    # Text display area
    text_area = tk.StringVar()
    text_entry = tk.Entry(root, textvariable=text_area, font=("Arial", 14), width=20, justify="center")
    text_entry.grid(row=0, column=0, columnspan=3, pady=10)

    # Copy button
    copy_button = tk.Button(root, text="Copy", font=("Arial", 12), command=copy_to_clipboard, bg="lightblue")
    copy_button.grid(row=1, column=0, columnspan=3, pady=5)

    # Define keypad layout with numbers and letters
    keypad = [
        ("1", ""),
        ("2", "ABC"),
        ("3", "DEF"),
        ("4", "GHI"),
        ("5", "JKL"),
        ("6", "MNO"),
        ("7", "PQRS"),
        ("8", "TUV"),
        ("9", "WXYZ"),
        ("*", ""),
        ("0", "+"),
        ("#", "")
    ]

    # Create buttons for each key in the keypad
    for i, (num, letters) in enumerate(keypad):
        frame = tk.Frame(root, bd=5, relief="flat")
        frame.grid(row=(i // 3) + 2, column=i % 3, padx=5, pady=5)
        
        # Number button
        num_button = tk.Button(frame, text=num, font=("Arial", 16), width=4, height=2, command=lambda n=num: button_click(n))
        num_button.pack()
        
        # Letters label below the number
        letters_label = tk.Label(frame, text=letters, font=("Arial", 10), fg="gray")
        letters_label.pack()
    
    root.mainloop()

if __name__ == "__main__":
    create_keypad()
