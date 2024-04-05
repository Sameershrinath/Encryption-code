import base64

def encode_text(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text

def decode_text(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text

# Example text
input_text = "This is an example text."

# Encode the text
encoded_text = encode_text(input_text)
print("Encoded text:", encoded_text)

# Decode the text
decoded_text = decode_text(encoded_text)
print("Decoded text:", decoded_text)
