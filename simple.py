import tkinter as tk
import tkinter.messagebox as messagebox
import pyperclip

def encode_decode():
    method = method_var.get()
    code = input_entry.get()
    
    if not code:
        messagebox.showerror("Error", "Please enter code.")
        return

    if method == "Encode":
        encoded_code = code[::-1]
        output_label.config(text="Encoded code: " + encoded_code)
    elif method == "Decode":
        decoded_code = code[::-1]
        output_label.config(text="Decoded code: " + decoded_code)

def clear_fields():
    input_entry.delete(0, tk.END)
    output_label.config(text="")

def copy_to_clipboard():
    code = output_label.cget("text").split(": ")[1]
    pyperclip.copy(code)

# Create the main window
root = tk.Tk()
root.title("Code Converter")

# Method selection
method_var = tk.StringVar()
method_var.set("Encode")
method_menu = tk.OptionMenu(root, method_var, "Encode", "Decode")
method_menu.pack(pady=5)

# Input section
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

input_label = tk.Label(input_frame, text="Enter code:")
input_label.pack(side=tk.LEFT)

input_entry = tk.Entry(input_frame, width=50)
input_entry.pack(side=tk.LEFT)

# Button to encode/decode
convert_button = tk.Button(root, text="Convert", command=encode_decode)
convert_button.pack(pady=5)

# Output section
output_frame = tk.Frame(root)
output_frame.pack(pady=5)

output_label = tk.Label(output_frame, text="")
output_label.pack(side=tk.LEFT)

# Buttons for additional actions
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.pack(side=tk.LEFT, padx=5)

copy_button = tk.Button(button_frame, text="Copy", command=copy_to_clipboard)
copy_button.pack(side=tk.LEFT)

# Run the application
root.mainloop()
