import requests

server_ip= "127.0.0.1"
message_to_push = "Hello World !i64 !i65 !i1064 2064"
message_to_push = "Index Integer !ii1.64"

ADDRESS = ""
PRIVATE_KEY = ""
# Fetch a private key for the session

def define_private_key():
    global ADDRESS
    global PRIVATE_KEY
    url = f"http://{server_ip}:80/api/create_metamask_wallet"
    response = requests.get(url)
    if response.status_code == 200:
        print("Response content:")
        print(response.text)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

    response_json = response.json()
    ADDRESS = response_json.get('address')
    PRIVATE_KEY = response_json.get('private_key')

    print(f"Address: {ADDRESS}")
    print(f"Private key: {PRIVATE_KEY}")


bool_fetch_private_key = True
if bool_fetch_private_key:
    define_private_key()
    


def send_message_using_rest_api(message_to_push):

    url_get_server__auth_id = f"http://{server_ip}:80/api/get_server_auth_id"
    response_server_auth_id = requests.get(url_get_server__auth_id)
    if response_server_auth_id.status_code == 200:
        SERVER_AUTH_ID = response_server_auth_id.json().get('auth')
        print("Response content:")
        print(response_server_auth_id.text)
        print ("Auth id:",SERVER_AUTH_ID)
        


    POST_MESSAGE_TO_SIGN = f"{SERVER_AUTH_ID} {message_to_push}"


    url_sign = f"http://{server_ip}:80/api/sign_message_with_private_key"

    #POST_MESSAGE_TO_SIGN = "EloiTeaching"
    data = {
        "private_key": PRIVATE_KEY,
        "message_to_sign": POST_MESSAGE_TO_SIGN
    }

    response_sign = requests.post(url_sign, json=data)
    if response_sign.status_code == 200:
        print("Response content:")
        print(response_sign.text)
    else:
        print(f"Failed to retrieve the page. Status code: {response_sign.status_code}")

    MESSAGE_SIGNED= response_sign.json().get('signed_message')

    #check if the message is signed

    CLIPBOARD_FORMAT = f"{POST_MESSAGE_TO_SIGN}|{ADDRESS}|{MESSAGE_SIGNED}"
    url_verify = f"http://{server_ip}:80/api/verifiy_given_message"
    verifiy_given_message = requests.post(url_verify, json={"message": CLIPBOARD_FORMAT})

    if verifiy_given_message.status_code == 200:
        print("Response content:")
        print(verifiy_given_message.text)
    else:
        print(f"Failed to retrieve the page. Status code: {verifiy_given_message.status_code}")
        
    #print ("Message PUSH:", CLIPBOARD_FORMAT)
    url_push_server_command = f"http://{server_ip}:80/api/push_server_auth_signed_command"
    response_push_server_command = requests.post(url_push_server_command, json={"message": CLIPBOARD_FORMAT})
    if response_push_server_command.status_code == 200:
        print("Response content:")
        print(response_push_server_command.text)
    return True
        
        
        
while True:
    console_input = input("Enter a message to push to the server: ")
    send_message_using_rest_api(console_input)
    print ("Message pushed to the server")