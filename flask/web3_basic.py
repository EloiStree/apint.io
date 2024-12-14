from flask import Flask, jsonify, request
from web3 import Web3
import secrets
from eth_account.messages import encode_defunct
import uuid


app = Flask(__name__)


def is_message_signed_from_clipboard_text(given_message):
    split_message = given_message.split("|")
    if len(split_message) < 3:
        return False
    message = split_message[0]
    address = split_message[1]
    signature = split_message[2]
    return is_message_signed_from_params(message, address, signature)


def is_message_signed_from_params(message, address, signature):
    w3 = Web3()
    # Encode the message
    encoded_message = encode_defunct(text=message)

    # Recover the address from the signature
    recovered_address = w3.eth.account.recover_message(encoded_message, signature=signature)
    return recovered_address.lower() == address.lower()

# Sample route
@app.route('/')
def home():
    return "Welcome to the Raspberry Pi REST API!"

# Get endpoint
@app.route('/api/create_metamask_wallet', methods=['GET'])
def get_data():
    
    # Generate a new private key
    private_key = "0x" + secrets.token_hex(32)
    w3 = Web3()
    account = w3.eth.account.from_key(private_key)
    sample_data = {
        "address": account.address,
        "private_key": private_key
    }
    return jsonify(sample_data)


@app.route('/api/sign_message_with_private_key', methods=['POST'])
def sign_message():
    data = request.get_json()
    private_key = data.get('private_key')
    message_to_sign = data.get('message_to_sign')
    
    w3 = Web3()
    account = w3.eth.account.from_key(private_key)
    
    message_hash = w3.keccak(text=message_to_sign)
    encoded_message = encode_defunct(text=message_to_sign)
    signed_message = w3.eth.account.sign_message(encoded_message, private_key=private_key)
    
    response_data = {
        "message": message_to_sign,
        "public_address": account.address,
        "signed_message": signed_message.signature.hex(),
        "clipboard_format": f"{message_to_sign}|{account.address}|{signed_message.signature.hex()}"
    }
    return jsonify(response_data)


#Verify the signed message
@app.route('/api/verifiy_given_message', methods=['POST'])
def verify_signed_message():
    data = request.get_json()
    message = data.get('message')
    
    is_signed = is_message_signed_from_clipboard_text(message)
    
    response_data = {
        "is_signed": is_signed
        
    }
    return jsonify(response_data)

# Post endpoint
@app.route('/api/data', methods=['POST'])
def post_data():
    input_data = request.get_json()
    return jsonify({"received": input_data}), 201

if __name__ == '__main__':
    # Run the Flask server on all interfaces (to allow external access)
    app.run(host='0.0.0.0', port=80)



