Linked In if you need to contact me:    
https://www.linkedin.com/in/eloistree/  


-------------------

IID & 🍺.io: https://buymeacoffee.com/apintio - https://github.com/EloiStree/IID - https://github.com/EloiStree/apint.io

--------------------------------------


# [https://apint.io](https://apint.io)


I love this name because it reminds me why I created this project:  
_Have an API that takes an integer as input output and operates under a beerware license philosophy._  



**Git**
Code: https://github.com/EloiStree/apint.io    
Page: https://eloistree.github.io/apint.io    

**Support**
Reddit: https://www.reddit.com/r/apint   
Discord: https://discord.gg/ZAUkBUF8ak  

**Server**
Pi Hosting Server: https://193.150.14.47 [https://apint.io](https://apint.io)  
Pi Hosted Server:[https://apint.ddns.net](https://apint.ddns.net)  
Pi Home Server:[https://apint-home.ddns.net](https://apint-home.ddns.net)  

**Chat(s) Bot:**
- Twitch Play on Discord: [Conferance](https://discord.gg/Tr8EvjpVCC) [Chat Only](https://discord.gg/YDYqKKwXAt)
- Twitch Play on Twitch: [Live](https://www.twitch.tv/eloiteaching) [Chat](https://www.twitch.tv/popout/eloiteaching/chat?popout=)

**Support the project**:
You can support the project by making donation and by claiming integer key spot.
- https://buymeacoffee.com/apintio

<a href="https://buymeacoffee.com/apintio" >
  <img style="width: 126px; height: auto;" src="https://github.com/user-attachments/assets/f3a59ae7-78fc-4c48-8985-773352c8b10c" alt="Support me on Buy Me a Coffee"/>
</a>


--------------------

# About 

[![image](https://github.com/user-attachments/assets/7ac2569a-7018-4d98-be9a-2f9eeffdfd9c)](https://github.com/EloiStree/License)  

My name is Éloi Strée, and I’m a Belgian developer working on integer-based tools designed to enable remote control functionality for gaming, QA testing, and "integer massive multiplayer games." Inspired deeply by the Twitch Plays Pokémon phenomenon, creating a game of that nature is a personal dream of mine.

API Integer IO is a landing page showcasing code centered around integers and serving as a gateway to small integer servers used for remote control purposes. For authentication, I use [MetaMask🦊](https://metamask.io) and [Ethereum](https://etherscan.io) as the login system.

Hosting remote control games across multiple computers, especially when they’re not in the same location, can be a real headache. It becomes even more challenging when you're not a tech-savvy person, dealing with fixed IPs and open ports in environments where you often lack admin privileges.

The idea here is to trade off some lag for the sake of simplicity in connectivity.

If you’re a fan of IFTTT, I’d love your help in building what I have in mind. The goal is simple: share integers between devices you own. This foundational concept can enable you to create your own IFTTT-like system. Just grab a Raspberry Pi, connect it to a shared integer server, and you’ve got a computer that can perform actions based on integers sent from any of your devices.

In short: let’s see what I can build!

Have a nice day, may the code be with you.

# Cross-Platform Interaction

APIntIO serves as a cross-platform API, designed with a MetaMask-signed and verified concept. 
Below are examples of bot code designed to run on a Raspberry Pi 5:
- **Twitch Bot**: [GitHub Repository](https://github.com/EloiStree/2024_12_11_HelloMegaMaskTwitchBot)  
- **Discord Bot**: [GitHub Repository](https://github.com/EloiStree/2024_12_07_HelloMegaMaskDiscordBot)

Learn about how to install some of the tools on your Pi:  
[https://github.com/EloiStree/2024_12_05_RaspberryPiGate](https://github.com/EloiStree/2024_12_05_RaspberryPiGate)

 -------------------------------

# Warning Agreement

## I store the authentication information in a public Git repository  

**Warning:** I cannot guarantee the privacy and security of your data.  
I lack the competence and expertise to ensure this.

When you link a MetaMask public address with a platform, it is stored in a public Git repository:  

The data is then placed in a database in this exact format to make it easier to access.  
those MetaMask to social link you give me is the only data related to your identity that I store.

We cannot remove data from a Git project (or prevent leaks of a database).
The server and host are meant to help beginners.

If you want to stay on a private policy system, you can learn to host a Pi server with my code or host a Linux server on AWS/Azure.



## DDoS, Hackers, Trolls, and Stability  

I am just a small game developer, and I don't plan to grow this project to a level where I can guarantee its operability 24/7.  
- It is likely to go down due to DDoS attacks.  
- It may be hacked by people who dislike the project, the use of the tool, or me.  
- It will probably be trolled by the Twitch community 😋.  
- It might crash because I am not great at my job.  
- It is going to be down when we do some stress test with thousands of player

I will do my best, but please do not consider this project to be stable.  

--------------------------


# Stream Game IP

APInt.io is the "stable" shared server part of the project based on integers and hosted on a Raspberry Pi.   
The gaming and development code are on my computer. You can find them with the DDNS.  

Here is an example in Python to recover the IP:
```python
import socket

def get_ip_from_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None

hostname = "apint.ddns.net"
ip_address = get_ip_from_hostname(hostname)
if ip_address is not None:
    print(f"Recovered address: {ip_address}")
else:
    print(f"Failed to get IP for hostname: {hostname}")

```



# Git Page JS HTML API

Small code to have some GET static page unsecure but availaible.

- Create ETH Private key:
  - Code: https://github.com/EloiStree/apint.io/blob/main/js/get/create_metamask_wallet.html
  - Example: http://eloistree.github.io/apint.io/js/get/create_metamask_wallet.html 
- Sign messsage with private key:
  - Code: https://github.com/EloiStree/apint.io/blob/main/js/get/sign_message_with_private_key.html 
  - Example: http://eloistree.github.io/apint.io/js/get/sign_message_with_private_key.html?q=0xf80ce241657b57c495133bde43d281869ab1d08f9e4c28d2c8e17ed1c9283da7|EloiTeaching 
- Verify message
  - Code: https://github.com/EloiStree/apint.io/blob/main/js/get/verifiy_given_message.html 
  - Example: http://eloistree.github.io/apint.io/js/get/verifiy_given_message.html?q=EloiTeaching|0xA3398ad7fB6aE44a542629De9d4426acfb4daE07|0x96f873575cc7a425b44035d0cd09313f092005d9c312b6405d58ad2d29cf398200bd76fdba9da2de86cbad99993292fbc2b1e731a14735f62a6e710149bfdb0b1b 




## DDNS

_When I am going to have the budget for multiple server_
_For now, all redirect to home and a Pi5
- `apint-gaming.ddns.net` Server design for Twitch Play 
- `apint-home.ddns.net` Server at home for testing 
- `apint-iot.ddns.net` Server with high kick restiction for iot remote control
- `apint.ddns.net` Default DDNS
- `apintio.ddns.net` Default DDNS.
- `apint.io` The static website.
