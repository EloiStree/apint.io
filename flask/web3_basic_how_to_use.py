<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Socket.IO Client</title>
    <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/web3/dist/web3.min.js"></script>
    <script>
    

    document.addEventListener('DOMContentLoaded', (event) => {
        async function signMessage(privateKey, message_to_sign) {
        try {
            if (!privateKey || !message_to_sign) {
                document.getElementById('error').textContent = "Invalid format. Expected format is: ?q=<privateKey>|<MessageToSign>";
                return;
            }
            const web3 = new Web3();
            const account = web3.eth.accounts.privateKeyToAccount(privateKey);
            const public_key = account.address;
            // Sign the message with the private key
            const signature = await web3.eth.accounts.sign(message_to_sign, privateKey);
            return message_to_sign + "|" + public_key + "|" + signature.signature;
        } catch (error) {
            console.error('Error signing message:', error);
            return "";
        }
    }
        const serverIp = 'http://193.150.14.47';
        //refresh page
        


        function validateOrGeneratePrivateKey() {
        let privateKeyInput = document.getElementById('PRIVATE_KEY').value;
        if (privateKeyInput) {
            // Validate the private key
            try {
                const web3 = new Web3();
                const account = web3.eth.accounts.privateKeyToAccount(privateKeyInput);
                document.getElementById('PRIVATE_KEY').value = privateKeyInput;
                document.getElementById('ADDRESS').value = account.address;
                document.getElementById('error').textContent = '';
            } catch (error) {
                document.getElementById('error').textContent = 'Invalid private key.';
            }
        } else {
            // Generate a new private key using web3
            const web3 = new Web3();
            const account = web3.eth.accounts.create();
            privateKeyInput = account.privateKey;
            document.getElementById('PRIVATE_KEY').value = privateKeyInput;
            document.getElementById('ADDRESS').value = account.address;
            document.getElementById('error').textContent = '';
        }

      
    }

    validateOrGeneratePrivateKey()
    async function pushInteger(value) {
        const serverIp = 'http://193.150.14.47';
        let request = serverIp + "/api/push_server_auth_signed_command";
        const coaster= document.getElementById('COASTER').value;

        let payloadValue ="";
       
        
        /// IF YOU DONT USE A COASTER THE USER IS EXPOSING IT PRIVATE KEY
        /// BUT IT MAKE IT EASY 
        const serverAuthId = document.getElementById('SERVER_AUTH').value;
        const privateKey = document.getElementById('PRIVATE_KEY').value;
        const currentServerAuthGUID= document.getElementById('SERVER_AUTH').value;
        const authPlusValueToSign=  currentServerAuthGUID+":"+value.toString();
        payloadValue = await signMessage(privateKey, authPlusValueToSign);
        if (coaster) 
        splitLetter = coaster.split("|");
            const coasterGuarantSigned= splitLetter[0];
            const metamaskPublicAddress= splitLetter[1];
            const guarantSignedBytMetaMask= splitLetter[2];
            payloadValue+="|"+metamaskPublicAddress+"|"+guarantSignedBytMetaMask;
        
      

        const payload = {
            message: payloadValue
        };

        fetch(request, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Response from server:', data);
        })
        .catch(error => console.error('Error pushing integer:', error));
    }

    async function pushRandomIID(min = 0, max = 100) {
        pushInteger(Math.floor(min + Math.random() * (max - min)));
    }


    function createCoaster() {

        //PRIAVTE_KEY: 0xcd88085df283a97c19ed050a60e6bc2d919b283270ee74bf2f05f857d818cd85
        //ADDRESS TO TRUST: 0x6ebB578a62E7a30961FF8272c3a06575F2072480
        //META_MASK PUBLIC ACCOUNT: 0x6CdD12C4CaaF4bcE5669f7f386d73a55ec7D1129
        //COASTER: 0x6ebB578a62E7a30961FF8272c3a06575F2072480|0x6CdD12C4CaaF4bcE5669f7f386d73a55ec7D1129|0x9d67549ef1a6e77f3519c2f679808dd4d46163d75e50c1e3bacc978cbcb97e1654ea1c4d5e1cc3467756c28170726eafc345daabe1e2d68cafa4759fa314cb881b
        const address = document.getElementById('ADDRESS').value;
        // open new tab to https://eloistree.github.io/SignMetaMaskTextHere/index.html?q= + address
        window.open('https://eloistree.github.io/SignMetaMaskTextHere/index.html?q=' + address, '_blank');
    }

    function fetchServerAuthId() {
        fetch(serverIp + '/api/get_server_auth_id')
            .then(response => response.json())
            .then(data => {
                document.getElementById('SERVER_AUTH').value = data.auth;
            })
            .catch(error => console.error('Error fetching server auth ID:', error));
    }



        function feelWithDebugValue(){

//PRIAVTE_KEY: 0xcd88085df283a97c19ed050a60e6bc2d919b283270ee74bf2f05f857d818cd85
//ADDRESS TO TRUST: 0x6ebB578a62E7a30961FF8272c3a06575F2072480
//META_MASK PUBLIC ACCOUNT: 0x6CdD12C4CaaF4bcE5669f7f386d73a55ec7D1129
//COASTER: 0x6ebB578a62E7a30961FF8272c3a06575F2072480|0x6CdD12C4CaaF4bcE5669f7f386d73a55ec7D1129|0x9d67549ef1a6e77f3519c2f679808dd4d46163d75e50c1e3bacc978cbcb97e1654ea1c4d5e1cc3467756c28170726eafc345daabe1e2d68cafa4759fa314cb881b

document.getElementById('PRIVATE_KEY').value = "0xcd88085df283a97c19ed050a60e6bc2d919b283270ee74bf2f05f857d818cd85";
document.getElementById('COASTER').value = "0x6ebB578a62E7a30961FF8272c3a06575F2072480|0x6CdD12C4CaaF4bcE5669f7f386d73a55ec7D1129|0x9d67549ef1a6e77f3519c2f679808dd4d46163d75e50c1e3bacc978cbcb97e1654ea1c4d5e1cc3467756c28170726eafc345daabe1e2d68cafa4759fa314cb881b";
document.getElementById('ADDRESS').value = "0x6ebB578a62E7a30961FF8272c3a06575F2072480"



}
    fetchServerAuthId();
    setInterval(fetchServerAuthId, 10000);
//feelWithDebugValue();

    function loadPrivateAndCoaster() {
        const privateKey = getCookie('privateKey');
        const coaster = getCookie('coaster');
        if (privateKey) {
            document.getElementById('PRIVATE_KEY').value = privateKey;
        }
        if (coaster) {
            document.getElementById('COASTER').value = coaster;
        }
    }

    function savePrivateAndCoaster() {
        const privateKey = document.getElementById('PRIVATE_KEY').value;
        const coaster = document.getElementById('COASTER').value;
        setCookie('privateKey', privateKey, 7);
        setCookie('coaster', coaster, 7);
    }

    function setCookie(name, value, days) {
        const d = new Date();
        d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = "expires=" + d.toUTCString();
        document.cookie = name + "=" + value + ";" + expires + ";path=/";
    }

    function getCookie(name) {
        const cname = name + "=";
        const decodedCookie = decodeURIComponent(document.cookie);
        const ca = decodedCookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(cname) == 0) {
                return c.substring(cname.length, c.length);
            }
        }
        return "";
    }

    document.getElementById('GENERATEPRIVATE').addEventListener('click', validateOrGeneratePrivateKey);
    document.getElementById('PUSHRANDOM').addEventListener('click', pushRandomIID);
    document.getElementById('CREATECOASTER').addEventListener('click', createCoaster);
     
    document.getElementById('SAVE').addEventListener('click', savePrivateAndCoaster);
    document.getElementById('LOAD').addEventListener('click', loadPrivateAndCoaster);


    });

   
    </script>
</head>
<body>
    <h1>Socket.IO Client</h1>

    
    <p><label for="PRIVATE_KEY">Private Key:</label>
    <input type="text" id="PRIVATE_KEY" >
    <button id="GENERATEPRIVATE" >Validate/Generate Private Key</button>
        <button id="SAVE">Save</button>
        <button id="LOAD">Load</button>
</p>


    <p><input type="text" id="COASTER" placeholder="Copy the signed message here">
    <button id="CREATECOASTER" >Create Coaster</button></p>
    <p><label for="SERVER_AUTH">Server Auth:</label>
    <input type="text" id="SERVER_AUTH" readonly></p>
    <p><label for="ADDRESS">Address:</label>
    <input type="text" id="ADDRESS" readonly></p>

    <p id="error"></p>
    <button id="PUSHRANDOM">Push Random</button>
</body>
</html>
