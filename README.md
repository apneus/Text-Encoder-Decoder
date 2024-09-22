# Encrypt and Decrypt Text GUI Application

This is a Python-based GUI application that allows users to encrypt and decrypt text using a predefined reversible cipher. The application is built using the `customtkinter` library for the graphical interface. Users can:
- Enter a text string to encrypt it into a random series of symbols and letters.
- Decrypt the previously encrypted message back to the original.
- Copy the encoded message to the clipboard for easy sharing.

## Features
- Encrypt text with a predefined cipher.
- Decrypt the text back to its original form.
- Copy the encrypted message to the clipboard.
- Fixed window size for consistent user experience.

### Disclaimer
- This is a simple text string encrypt and decrypt application. It holds the encryption for the current
session to allow ongoing decryption. This is a learning project only.
- NOT SUITABLE TO USE AS AN ENCRYPTION SOLUTION FOR ANY SENSITIVE INFORMATION

## Using the Application

    Enter Text: Input the text you want to encrypt in the text box.
    Encrypt Button: Click "Encrypt" to transform the input text into a random series of letters and symbols.
    Decrypt Button: Click "Decrypt" to convert the last encrypted message back to its original form.
    Copy to Clipboard: After encrypting the text, click "Copy to Clipboard" to save the encrypted message.
	
## How the Code Works
Main Components:

    Encryption and Decryption:
        Cipher Mapping: The program generates a dictionary that maps each letter and space to a random letter, symbol, or digit using random.sample. This mapping is consistent throughout the session, allowing the program to reverse the encryption process.
        Encrypting: When you press the "Encrypt" button, the input text is encrypted using the predefined encrypt_dict mapping.
        Decrypting: When you press the "Decrypt" button, the last encrypted message is decrypted back to the original text using the decrypt_dict mapping.

    Clipboard Support:
        The application has a "Copy to Clipboard" button that, when clicked, copies the encoded message to the system's clipboard using the clipboard_clear() and clipboard_append() functions from tkinter.

    GUI Layout:
        The GUI is created using the customtkinter library. The window is set to a fixed size of 400x400, meaning users can't resize the window.
        The main window contains:
            A text entry field to input text.
            Buttons to encrypt, decrypt, and copy the text.
            A result label to display the encrypted or decrypted message.
			
## Example Usage

    Encrypt a Message: Enter a message like "Hello World", then click the "Encrypt" button. The message will be transformed into a random string of symbols and letters, e.g., j1kL%Pq2*.
    Decrypt a Message: After encrypting, click "Decrypt" to revert back to the original message.
    Copy to Clipboard: Click "Copy to Clipboard" after encryption to save the encoded message. You can paste it back and click decrypted
	
	This will only work during the current session.