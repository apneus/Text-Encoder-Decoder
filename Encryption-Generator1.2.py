import customtkinter as ctk
import random
import string
import tkinter as tk  # Required for clipboard functionality

# Variable to store the last encrypted message
last_encrypted_message = ""

# Generate a mapping for encryption
def create_cipher_mapping():
    # Include letters and space for encryption
    letters_and_space = string.ascii_letters + ' '  
    symbols = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>/?"
    # Randomly sample without replacement
    random_symbols = random.sample(symbols, len(letters_and_space))  
    encrypt_dict = dict(zip(letters_and_space, random_symbols))
    decrypt_dict = {v: k for k, v in encrypt_dict.items()}
    return encrypt_dict, decrypt_dict

# Create encryption and decryption mappings
encrypt_dict, decrypt_dict = create_cipher_mapping()

# Function to encrypt the message using the predefined mapping
def encrypt_message(message):
    encrypted_message = ""
    for char in message:
        # Encrypt letters and spaces
        encrypted_message += encrypt_dict.get(char, char)  
    return encrypted_message

# Function to decrypt the message using the predefined mapping
def decrypt_message(message):
    decrypted_message = ""
    for char in message:
        # Decrypt letters and spaces
        decrypted_message += decrypt_dict.get(char, char)  
    return decrypted_message

# Function to handle encryption
def on_encrypt_button_click():
    # Store the encrypted message
    global last_encrypted_message  
    input_text = input_entry.get()
    encrypted_text = encrypt_message(input_text)
    # Save the encrypted message for later decryption
    last_encrypted_message = encrypted_text  
    result_label.configure(text=f"Encoded Message: {encrypted_text}")

# Function to handle decryption
def on_decrypt_button_click():
    global last_encrypted_message
    # Decrypt the last encrypted message
    decrypted_text = decrypt_message(last_encrypted_message)  
    result_label.configure(text=f"Decoded Message: {decrypted_text}")

# Function to copy the encrypted message to clipboard
def copy_to_clipboard():
    if last_encrypted_message:
        # Clear the clipboard
        app.clipboard_clear()  
        # Append the encrypted message to the clipboard
        app.clipboard_append(last_encrypted_message)  
        # Update the label to show success
        result_label.configure(text="Encoded Message Copied to Clipboard!")  

# Create the main window
app = ctk.CTk()
app.geometry("400x400")
app.title("Encrypt and Decrypt Text")

# Set the minimum and maximum window size
app.minsize(400, 400)
app.maxsize(400, 400)

# Set appearance mode to 'dark'
ctk.set_appearance_mode("dark")
# You can choose other color themes as well
ctk.set_default_color_theme("dark-blue")  

# Input Label
input_label = ctk.CTkLabel(app, text="Enter Text", font=("Arial", 14))
input_label.pack(pady=10)

# Input Entry
input_entry = ctk.CTkEntry(app, width=300, font=("Arial", 14))
input_entry.pack(pady=10)

# Encrypt Button
encrypt_button = ctk.CTkButton(app, text="Encrypt", command=on_encrypt_button_click)
encrypt_button.pack(pady=10)

# Decrypt Button
decrypt_button = ctk.CTkButton(app, text="Decrypt", command=on_decrypt_button_click)
decrypt_button.pack(pady=10)

# Copy to Clipboard Button
copy_button = ctk.CTkButton(app, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Result Label
result_label = ctk.CTkLabel(app, text="Output: ", font=("Arial", 14))
result_label.pack(pady=20)

# Start the main loop
app.mainloop()
