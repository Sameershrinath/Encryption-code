import tkinter as tk
from cryptography.fernet import Fernet

# Generate a random key for AES encryption
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_decrypt():
    method = method_var.get()
    code = input_entry.get()
    
    if not code:
        messagebox.showerror("Error", "Please enter code.")
        return

    if method == "Encrypt":
        encoded_code = code.encode()
        encrypted_code = cipher.encrypt(encoded_code).decode()
        output_label.config(text="Encrypted code: " + encrypted_code)
    elif method == "Decrypt":
        try:
            decrypted_code = cipher.decrypt(code.encode()).decode()
            output_label.config(text="Decrypted code: " + decrypted_code)
        except:
            messagebox.showerror("Error", "Invalid code or key.")

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
method_var.set("Encrypt")
method_menu = tk.OptionMenu(root, method_var, "Encrypt", "Decrypt")
method_menu.pack(pady=5)

# Input section
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

input_label = tk.Label(input_frame, text="Enter code:")
input_label.pack(side=tk.LEFT)

input_entry = tk.Entry(input_frame, width=50)
input_entry.pack(side=tk.LEFT)

# Button to encrypt/decrypt
convert_button = tk.Button(root, text="Convert", command=encrypt_decrypt)
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
