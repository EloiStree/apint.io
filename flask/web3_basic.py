# WITHOUT CERTBOT SSL
# ONLY WORK IN HTTP ON LOCAL COMPUTER OF OUTSIDE OF BROWSER.





# pip install apscheduler --break-system-packages
# pip install flask --break-system-packages
# Note: Steam downloads a game at home at 70Mbps
# 8750000 bits per second
# 8750000/8 = 1093750 bytes per second
# integer command is 4-12 bytes
# You can receive in theory 1093750/4 
# 273437 integer commands per second
# In the best world where you don't have 
# lag, bandwidth limitation, CPU limitation,
# Not counting the heavy REST format in the gate that relays the 12 bytes
# Not counting print execution when forgetting to mute.
# and the header size of UDP.
# All that to say, you need to manage the community spam and game design
# If you do an integer game with this tool.
# -> And, use Webscoket for real time action.<-

# sudo nano /lib/systemd/system/apintio_flask_api.service
"""
[Unit]
Description=Flask API Auth
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /git/apintio/flask/web3_basic.py
Restart=always
User=root
WorkingDirectory=/git/apintio/flask/

[Install]
WantedBy=multi-user.target
"""
#1h
# sudo nano /etc/systemd/system/apintio_flask_api.timer
"""
[Unit]
Description=API Flask Timer

[Timer]
OnBootSec=0min
OnUnitActiveSec=1800s

[Install]
WantedBy=timers.target
"""


# Learn: https://youtu.be/nvx9jJhSELQ?t=368
"""
# cd /lib/systemd/system/
# sudo systemctl daemon-reload
# sudo systemctl enable apintio_flask_api.service
# chmod +x /git/apintio/flask/web3_basic.py
# sudo systemctl enable apintio_flask_api.service
# sudo systemctl start apintio_flask_api.service
# sudo systemctl enable apintio_flask_api.timer
# sudo systemctl start apintio_flask_api.timer
# sudo systemctl status apintio_flask_api.service
# sudo systemctl stop apintio_flask_api.service
# sudo systemctl restart apintio_flask_api.service
# 
sudo systemctl list-timers | grep apintio_flask_api



sudo systemctl stop apintio_flask_api.service
sudo systemctl stop apintio_flask_api.timer

 sudo systemctl restart apintio_flask_api.service
 sudo systemctl restart apintio_flask_api.timer


 sudo systemctl list-timers | grep apintio_flask_api
"""

import socket
import struct
from flask import Flask, jsonify, request
from web3 import Web3
import secrets
from eth_account.messages import encode_defunct
import uuid
from apscheduler.schedulers.background import BackgroundScheduler
from tzlocal import get_localzone

from flask_cors import CORS  # Import the CORS class
from flask import Flask, jsonify


app = Flask(__name__)
# Enable CORS for all routes and all origins (allow access from any domain)
CORS(app)


time_between_authentification_change=10
double_authentification_int_current=""
double_authentification_int_previous=""



# >>>>>>>>>>>>>>>>>>>>>>>> START OF RELAY TO PARSING AND BYTES COUNTER INIT

## Do you want an other app to deal with the message.
## Just the address and the message are sent.
## Thing application is in "trust mode"
bool_use_interpretor_udp=True
# BY SIMPLICITY, LACK OF SECURITY, I SEND THE MESSAGE TO A INTERPRETOR ON THE SAME DEVICE
# GIVE IT IP THAT SHOULD BE THE SAME AS THE DEVICE BUT CAN BE CHANGED
valide_message_interpretor_udp_ipv4= "127.0.0.1"
# GIVE IT PORT.
valide_message_interpretor_udp_port= 7042

# Avoid user to make file transfert or abuse of your generosity.
# Limit the size of the message
authorized_size_of_message=512




# When you can identify a user by it public address.
# You can use a byte counter to count the byte sent by the user.
# If you don't kick or ban user for abusing your service.
# They will do it.
# That an other level of code, so find the code in future github code.
# The idea is simple, an application receive public address and byte count.
# Kicking user or banning them depending of rate per second, minute, hour, day, months, years.
bool_use_byte_counter=True
byte_counter_ipv4="127.0.0.1"
byte_counter_port= 7403 # 403 is status message for forbidden in http.

local_app_counter_byte_ipv4={}
local_app_counter_call_ipv4={}

def append_to_byte_counter(public_address, byte_count):
    if not is_ethereum_public_address(public_address):
        return 

    if not bool_use_byte_counter:
        return
    
    sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = f"{public_address}|{byte_count}"
    byte_t = text.encode()
    sock.sendto(byte_t, (byte_counter_ipv4, byte_counter_port))
    sock.close()
    
    
# <<<<<<<<<<<<<<<<<<<<<<< END OF RELAY TO PARSING AND BYTES COUNTER INIT
    



# >>>>>>>>>>>>>>>>>>>>>>>> START OF DEBUG INIT

# It convert text !i0099887766 43 1 4564 -45
# To integer value in id format (int, ulong 12 bytes value, date)
# Then send it to the debugger
bool_use_integer_debugger=True
# If you want your local computer to use them
integer_debugger_ipv4="127.0.0.1"
# My anarchy idd debugger port for twtich play
integer_debugger_ipv4="apint.ddns.net"



debugger_port= {}
debugger_port["Windows Home Relay"]=3614 
#debugger_port["RaspberryPi5 Home Relay"]=3613
#debugger_port["Android Home Game Server"]=3612
#debugger_port["MiniPC Home Guide Server"]=3611
debugger_port["Window Workspace"]=3615

# Experiment it on 77073 scratch to warcraft
# https://github.com/EloiStree/2024_08_29_ScratchToWarcraft


# List of the value por tin debugger port set dynamically

debugger_post_list: list = []
for key in debugger_port:
    debugger_post_list.append(debugger_port[key])


def relay_to_anarchy_integer_debugger(integer):
    if not bool_use_integer_debugger:
        return
    
    print(f"""
        > Pushing integer to anarchy integer debugger\n
        Integer: {integer}\n
        """)
    # SEND TO ANARCHY INTEGER DEBUGGER
    # UDP
    # SEND INTEGER TO
    for port in debugger_post_list: 
        byte_integer = struct.pack("<i", integer)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(byte_integer, (integer_debugger_ipv4, port))
        sock.close()
#<<<<<<<<<<<<<<<<<<<<<<< END OF DEBUG INIT

def relay_to_anarchy_index_integer_debugger (index, integer):
    if not bool_use_integer_debugger:
        return
    print(f"""
        > Pushing index integer to anarchy integer debugger\n
        Index Integer: {integer}\n
        """)
    # SEND TO ANARCHY INTEGER DEBUGGER
    # UDP
    # SEND INTEGER TO
    for port in debugger_post_list: 
        byte_integer = struct.pack("<ii", index, integer)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(byte_integer, (integer_debugger_ipv4, port))
        sock.close()



def relay_message_to_interpretor(message, user_public_address):
    if not bool_use_interpretor_udp:
        return
    message.strip()    
    message.replace(str(double_authentification_int_current), "")
    message.replace(str(double_authentification_int_previous), "")
    print(f"""
        > Pushing message to interpretor\n
        Message: {message}
        User Public Address: {user_public_address}\n
        """)
    
    shortcut = message.split(" ")
    for t in shortcut:
        t.strip()
        print(t)
        if len(t) > 3:
            #!ii1.1046 !ii3.65431  index.value
            # Some  anarchic app/game use unauthentify integer format
            # For example when a teach to beginner.
            # Have a look at scratch to warcraft as example
            # https://github.com/EloiStree/2024_08_29_ScratchToWarcraft
            if t[0]=="!" and t[1]=="i" and t.find(".")>0:
                try:
                    t_split = t[2:].split(".")
                    if len(t_split[0])==0:
                        index=0
                    else:
                        index = int(t_split[0])
                    value = int(t_split[1])
                    relay_to_anarchy_index_integer_debugger(index,value)
                    continue
                except:
                    pass
                
           #!i42 !i-654
            elif t[0]=="!" and t[1]=="i":
                try:
                    int_value = int(t[2:])
                    relay_to_anarchy_integer_debugger(int_value)
                    continue
                except:
                    pass
        try:
            int_value = int(t)
            relay_to_anarchy_integer_debugger(int_value)
            continue
        except:
            pass
        
        
    
    
    
    
def is_ethereum_public_address(val):
    if len(val) != 42:
        return False
    if val[0:2] != "0x":
        return False
    return True


# TIMED ACTION
def change_oauth_id():
    global double_authentification_int_current
    global double_authentification_int_previous
    
    if double_authentification_int_current==0:
        print("Set of the first authentification id")
        double_authentification_int_current = uuid.uuid4()
        double_authentification_int_previous = double_authentification_int_current
        print("Oauth2: ", double_authentification_int_current, double_authentification_int_previous)
        return
    print("Change  of the authentification id") 
    double_authentification_int_previous = double_authentification_int_current   
    double_authentification_int_current = uuid.uuid4()
    print("Oauth2: ", double_authentification_int_current, double_authentification_int_previous)
    
# Set the time zone manually
scheduler = BackgroundScheduler(timezone="Europe/London")  # or "Europe/Brussels"
scheduler.add_job(func=change_oauth_id, trigger="interval", seconds=time_between_authentification_change)
scheduler.start()

change_oauth_id()

@app.before_request
def start_scheduler():
    if not scheduler.running:
        scheduler.start()

@app.teardown_appcontext
def shutdown_scheduler(exception=None):
    scheduler.shutdown()



# OFFLINE FUNCTION START

def is_message_signed_from_clipboard_text(given_message):
    """
    This function checks if the given message is signed by the given address.
    The format of the text must be as follows:
    message|address|signature
    """
    split_message = given_message.split("|")
    lenght = len(split_message)
    if not(lenght ==3 or lenght == 5):
        return False
    message = split_message[0]
    address = split_message[1]
    signature = split_message[2]
    return is_message_signed_from_params(message, address, signature)


def is_message_signed_from_params(message, address, signature):
    """
    This function checks if the given message is signed by the given public address.
    """
    w3 = Web3()
    encoded_message = encode_defunct(text=message)
    recovered_address = w3.eth.account.recover_message(encoded_message, signature=signature)
    return recovered_address.lower() == address.lower()

def is_message_start_with_current_previous_server_auth_id( message):
    """
    If someone stole signed message of user he can sotre and use them later
    To make sure the message is design for this server,
    we check if the message start with the current or previous authentification id
    If meaning that a message use by a hacker is by sniffing is valide only for N seconds
    """    
    print(f"M: {message} C: {double_authentification_int_current} P: {double_authentification_int_previous}")
    return message.startswith(str(double_authentification_int_current)) or message.startswith(str(double_authentification_int_previous))

# OFFLINE FUNCTION END

# API START

# Sample route
@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>API Int 🍺.io</title>
    <style>
        body {
            background-color: black;
            color: #00FF00;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        a {
            color: #00AA00;
            text-decoration: none;
        }
        a:hover {
            color: #00CC00;
            text-decoration: underline;
        }
        
    </style>
</head>
<body>
    <h1>API Int 🍺.io</h1>
    <p>Welcome to the Raspberry Pi REST API </p>
    <p>Documentation here: <a href="https://github.com/EloiStree/apint.io/tree/main/flask">https://github.com/EloiStree/apint.io/tree/main/flask</a></p>
    
    
</body>
</html>
"""

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
@app.route('/api/echo', methods=['POST'])
def post_echo():
    data = request.get_json()
    return jsonify(data)


# PUSH MESSAGE WITH AUTHORITY

@app.route('/api/get_server_auth_id', methods=['GET'])
def get_server_auth_id():
    """
    RETURN THE CURRENT AUTH ID
    THIS ID IS A BIT LIKE A AUTH2.
    IT CHANGE EVERY N SECONDS
    IT ALLOWS TO BE SURE THE SIGNED MESSAGE IS RECENT AND TARGETING THIS SERVER
    """
    response_data = {
        "auth": double_authentification_int_current
    }
    return jsonify(response_data)

@app.route('/api/push_server_auth_signed_command', methods=['POST'])
def push_server_auth_signed_command():
    """ IF YOU READ THIS.
    REST IS HEAVY TO JUST SEND SMALL MESSAGE AND INTEGER
    USER SHOULD BE USING THE WEBSOCKET VERSION.
    BUT WHEN YOUR JUST WANT TO TURN ON AND OF LIGHTS
    THEN WEBSOCKET COULD BE THE WORST SOLUTION.
    IF YOU NEED REAL TIME ACTION <1-10 MS, 
    YOU WONT REACH IT FROM HERE.
    """
    data = request.get_json()
    message = data.get('message')
    print (f"Message: {message}")
    
    if  len(message) > authorized_size_of_message:
        response_data = {
            "error": """
            The server is not a file transfert server.
            Your message must be less that 256 characters long.
            """
        }
        return jsonify(response_data)
    
    if not is_message_start_with_current_previous_server_auth_id(message):
        response_data = {
            "error": """
            Your message must start with the current or previous auth id\n.
            See /api/get_server_auth_id in documentation.
            """ 
        }
        return jsonify(response_data)
    is_signed = is_message_signed_from_clipboard_text(message)
    if not is_signed:
        response_data = {
            "error": """
            Please sign your message before sending it.
            If you don't have the coding level to sign a message, you can use the following API:
            Use /api/sign_message_with_private_key 
            Required: private_key, auth_id
            """
        }
        return jsonify(response_data)
    
    split_message = message.split("|")
    split_message_length = len(split_message)
    address= split_message[1]
    to_interpret = split_message[0]
    to_interpret = to_interpret.replace(str(double_authentification_int_current), "")
    to_interpret = to_interpret.replace(str(double_authentification_int_previous), "")
    
    if split_message_length == 3:
        relay_message_to_interpretor(to_interpret, address)
        response_data = {
            "ok": "Message relayed"
        }
        return jsonify(response_data)
    if split_message_length == 5:    
        master_address = split_message[3]
        is_coaster_signed = is_message_signed_from_params(split_message[1], split_message[3], split_message[4])
        if not is_coaster_signed:
            response_data = {
                "error": """
                The coaster message must be signed by the coaster public address.
                """
            }
            return jsonify(response_data)
        
        relay_message_to_interpretor(to_interpret, master_address)
        response_data = {
            "ok": "Coasted message relayed"
        }
        return jsonify(response_data)

# API END
if __name__ == '__main__':
    
    if bool_use_integer_debugger:
        ip_of_ddns = socket.gethostbyname(integer_debugger_ipv4)
        #integer_debugger_ipv4 = ip_of_ddns
        print(f"Integer debugger ip: {integer_debugger_ipv4}")
    
    app.run(host='0.0.0.0', port=8081)
    
    
