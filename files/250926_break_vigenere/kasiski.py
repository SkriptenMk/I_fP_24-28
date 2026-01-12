# kasiski.py

# %%

import string
import pdfplumber
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from collections import defaultdict

# %%

def pdf_reader(path : str, start : int = 0, end : int = None) -> str:
    with pdfplumber.open(path) as pdf:
        pages = pdf.pages
        text = ""
        if end is None:
            end = len(pages)
        for i, pg in enumerate(pages):
            if i >= start and i < end:
                text += pages[i].extract_text() + "\n"
    
    return text
                
# %%

def file_reader(path : str) -> str:

    with open(path, mode='r', encoding='utf-8') as f:
        text = f.read()

    return text

def file_writer(path : str, text : str) -> None:
    i = 0
    grouped_text = ""
    for c in text:
        i += 1
        if i % 50 == 0:
            grouped_text += c + "\n"
        elif i % 5 == 0:
            grouped_text += c + " "
        else:
            grouped_text += c
        
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(grouped_text)
        
def text_cleaning(text : str) -> str:
    clean = text.upper() \
                .replace('Ä', 'AE') \
                .replace('Ö', 'OE') \
                .replace('Ü', 'UE') \
                .replace('ß', 'SS') \
                .replace(' ', '') \

    cleaned_text = ''

    for c in clean:
        if c.isalpha():
            cleaned_text += c
    
    return cleaned_text

# %%

def vigenere(text: str, key: str, mode: str) -> str:
    """Encrypts or decrypts a given text using the Vigenère cipher.

    The function processes a string of uppercase alphabetic characters
    using a provided key for encryption or decryption.

    Args:
        text: The string to be encrypted or decrypted. It should only contain
              uppercase alphabetic characters (A-Z).
        key: The key for the cipher. It should also only contain
             uppercase alphabetic characters (A-Z).
        mode: The operation to perform, must be 'encrypt' or 'decrypt'.

    Returns:
        The resulting ciphertext or plaintext.

    Raises:
        ValueError: If the mode is not 'encrypt' or 'decrypt'.
    """

    # Ensure the mode is valid before proceeding.
    if mode not in ['encrypt', 'decrypt']:
        raise ValueError("Mode must be 'encrypt' or 'decrypt'")
    
    key_length = len(key)
    
    if mode == 'encrypt':
       cipher = ''
       # Iterate through each character of the input text.
       for i, char in enumerate(text):
           # Convert the current text character and the corresponding key 
           # character to a number (0-25).
           # The key character is determined using modulo to cycle through 
           # the key.
           char_num = ord(char) - ord('A')
           key_num = ord(key[i % key_length]) - ord('A')
           
           # Calculate the new character's number using the Vigenère encryption formula.
           # The modulo operator ensures the result stays within the range 0-25.
           cipher_num = (char_num + key_num) % 26
           
           # Convert the resulting number back to an uppercase character and append it.
           cipher += chr(cipher_num + ord('A'))
       return cipher  
    else:  # mode == 'decrypt'
        plain = ''
        # Iterate through each character of the input text.
        for i, char in enumerate(text):
            # Convert the current text character and the corresponding key 
            # character to a number (0-25).
            char_num = ord(char) - ord('A')
            key_num = ord(key[i % key_length]) - ord('A')
            
            # Calculate the new character's number using the Vigenère 
            # decryption formula.
            # The modulo operator handles negative results, ensuring the 
            # result is correct.
            plain_num = (char_num - key_num) % 26
            
            # Convert the resulting number back to an uppercase 
            # character and append it.
            plain += chr(plain_num + ord('A'))
        return plain
    
# %%



def _get_factors(n):
    """
    Hilfsfunktion zur Berechnung aller Teiler einer Zahl n (größer als 2).
    """
    factors = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    if n > 1:
      factors.add(n)
    return list(factors)

def kasiski_test(ciphertext, min_seq_len=3, max_seq_len=5):
    """
    Führt den Kasiski-Test für einen gegebenen Vigenère-verschlüsselten Text durch.

    Der Test identifiziert wiederholte Zeichensequenzen, misst die Abstände zwischen
    ihren Vorkommen und analysiert die Teiler dieser Abstände, um wahrscheinliche
    Schlüssellängen zu finden.

    Args:
        ciphertext (str): Der verschlüsselte Text.
        min_seq_len (int): Die minimale Länge der zu suchenden Zeichensequenzen.
        max_seq_len (int): Die maximale Länge der zu suchenden Zeichensequenzen.

    Returns:
        dict: Ein Dictionary, bei dem die Schlüssel mögliche Schlüssellängen und
              die Werte deren Häufigkeit sind, sortiert nach Häufigkeit absteigend.
    """
    # 1. Finde Positionen von wiederholten Sequenzen
    sequences_positions = defaultdict(list)
    for seq_len in range(min_seq_len, max_seq_len + 1):
        for i in range(len(ciphertext) - seq_len + 1):
            sequence = ciphertext[i:i+seq_len]
            sequences_positions[sequence].append(i)

    # 2. Berechne die Abstände zwischen den Vorkommen
    distances = []
    for sequence, positions in sequences_positions.items():
        if len(positions) > 1:
            for i in range(len(positions) - 1):
                distance = positions[i+1] - positions[i]
                distances.append(distance)

    # 3. Finde die Teiler der Abstände und zähle deren Häufigkeit
    factor_counts = defaultdict(int)
    for dist in distances:
        factors = _get_factors(dist)
        for factor in factors:
            factor_counts[factor] += 1

    # 4. Sortiere die Ergebnisse nach Häufigkeit
    sorted_factor_counts = sorted(
        factor_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return dict(sorted_factor_counts)



# %%
plain = pdf_reader('economist.pdf')

print(plain)
# %%

cipher = vigenere(plain, 'bueli', 'encrypt')

print(cipher)

# %%

file_writer('economist_cipher.txt', cipher)
# %%
plain_clean = text_cleaning(plain)

file_writer('economist_clean.txt', plain_clean)
# %%

result = kasiski_test(cipher, 3, 10)
print(result)

# %%
