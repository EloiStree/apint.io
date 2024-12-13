# Need help

If any of those topic, you think it is easy and you want to help 😀.  
Ping me on Discord when you have time.  


# Context

I don’t want to create games using ETH, Infura, or other libraries that are unnecessarily heavy. They make the app overly complicated, prone to injection vulnerabilities, and difficult to maintain over time.

In some of my apps, I want to simplify things by adopting a different approach.  

For example, I could create some JavaScript code that processes information via GET parameters and returns results in the body, similar to a RESTful concept.

We need three actions, in MetaMask-compatible format:
1. **Create a New Wallet**  
2. **Sign a Message with a Private Key**  
3. **Verify a Given Message**  

While these actions are risky in terms of potential leaks and could be a hacker’s paradise, my goal here is to provide an easy way to:
- Perform these actions for students who don’t yet have the skills to implement them independently.  
- Serve as a temporary solution while I work on creating lightweight C# code for signing and verifying messages—code that is compatible with MetaMask and can run across all Unity3D platforms.

You can find a human-friendly version in `js/human`, which is designed to guide the user step by step.

Later, I might implement versions of these three actions in:
- **WebSocket** (a simple connection, send params, response, then close the connection with a 4-second timeout)
 
For the website:
- **PHP** (If someone explains how to make it run on old PHP setups without complex installations)
- **RESTful API** (If anyone can help me with this)


What I really need to do is create a static JavaScript page with the three basic actions to ensure I always have a backup solution when my servers are down or under a DDoS attack.
What I need to learn now is how to make a callback from the webpage to the application, so that the static JavaScript results can be returned to the calling Unity application (in Unity3D for Android, Windows, or Quest at a minimum).


