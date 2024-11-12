import discord
import asyncio
import random
import re
waiting = False
running = False
channelids = []
snipechannelids = [1289670814798446713]
deletedmessages = []
client = discord.Client()
admins = []
owners = [992175008493338777]

@client.event
async def on_ready():
    print(f"You're logged in as {client.user}")


@client.event
async def on_message(message: discord.Message):
    global channelids, running, waiting

    # COUNT ING THING
    if message.author in admins or message.author in owners and "!count" in message.content:
        x = re.findall(r"-?\d+", message.content)
        if int(x[0]) > int(x[1]):
            reply = await message.reply(f"{int(x[0])}")
            for i in range(int(x[0]) + abs(int(x[1]))):
                print(f"{int(x[0])-i}")
                await reply.edit(f"{int(x[0])-i}")
                await asyncio.sleep(1)
                i -= 1
            await reply.edit(f"{int(x[1])}")
        else:
            reply = await message.reply(f"{int(x[0])}")
            for i in range(abs(int(x[0]) - int(x[1]))):
                print(f"{int(x[0])+i}")
                await reply.edit(f"{int(x[0])+i}")
                await asyncio.sleep(1)
                i += 1
            await reply.edit(f"{int(x[1])}")

    if (message.author.id in owners) and "!stop" in message.content:
        running = True

    elif (message.author.id in owners) and "!listen" in message.content:
        channelids.append(message.channel.id)
        await message.reply("Listening...")

    elif (message.author.id in admins or message.author.id in owners) and "!snipelisten" in message.content:
        print(message.channel.id)
        snipechannelids.append(message.channel.id)
        await message.reply("Sniping...")

    elif (message.author.id in owners) and "!stoplisten" in message.content:
        channelids.remove(message.channel.id)
        await message.reply("Not Listening...")

    elif (message.author.id in owners) and "!stopsnipelisten" in message.content:
        snipechannelids.remove(message.channel.id)
        await message.reply("Not Sniping...")

    elif (
        message.channel.id in channelids
        and ("how" in message.content or "where" in message.content)
        and ("install" in message.content or "download" in message.content)
        and "xeno" in message.content
        and not waiting
    ):
        if ("virustotal" in message.content or "jerkmate" in message.content):
            waiting = True
            await message.reply("""you can't.""")
            await asyncio.sleep(15)
            waiting = False
        else:
            waiting = True
            await message.reply(
                """
Download to Xeno: <#1289729762310225941>
If the application (Xeno.exe/Xeno [Application]) doesn't open after downloading and extracting: <#1290088055352590347>

Other Additional Solutions (e.g., not attaching or still not opening):
-# Make sure any antivirus is off (Especially for Windows 11)
-# It's an auto attach so it doesn't matter which one opens first
-# Remember to use an alternative account and VPN to prevent any inconvenience!
-# If it says version mismatch, press ok and run it anyways, it should work."""
            )
            await asyncio.sleep(15)
            waiting = False

    if (
        ("fisch" in message.content or "blox fruits" in message.content)
        and "script" in message.content
        and message.channel.id in channelids
        and not waiting
    ):
        
        rickrollbaits = [
            "i have a good one, check [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)",
            "oh yeah for sure, check [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)",
            "actually yeah i think i have one, check [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)",
            "i saw one on youtube but idk if it works, you should [try it](https://www.youtube.com/watch?v=dQw4w9WgXcQ)",
            "uhm i think [this one](https://www.youtube.com/watch?v=dQw4w9WgXcQ) works",
            "you might have to check it but [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ) is the link",
            "im pretty sure this one works, check [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)",
        ]
        waiting = True
        await message.channel.typing()
        await asyncio.sleep(random.randint(1, 3))
        await message.reply(rickrollbaits[random.randint(0, 6)])
        await asyncio.sleep(15)
        waiting = False

    if (message.author.id in admins or message.author.id in owners) and message.channel.id in snipechannelids and "!snipe" in message.content:
        try:
            if re.search(r'\d+', message.content):
                x = re.search(r'\d+', message.content)
                await message.author.send(deletedmessages[-int(x[0])])
            else:
                await message.author.send(deletedmessages[-1])
        except:
            await message.author.send("no messages deleted")
    
    if message.channel.id in channelids and (message.author.id in admins or message.author.id in owners) and "!banana" in message.content:
        await message.channel.send(f"<@{message.mentions[0].id}> , you're being bananaed by <@{message.author.id}> 🍌")
    
    if message.author.id in owners and "!admin" in message.content and message.mentions[0].id not in admins:
        admins.append(message.mentions[0].id)
        await message.reply(f"Added {message.mentions[0].display_name} to admins")

    elif message.author.id not in owners and "!admin" in message.content:
        await message.reply("You don't have permission to use this command")

    elif message.author.id in owners and "!admin" in message.content and message.mentions[0].id in admins:
        await message.reply("they already an admin or sum shit")

    if message.author.id in owners and ("!removeadmin" in message.content or "!unadmin" in message.content) and message.mentions[0].id in admins:
        admins.remove(message.mentions[0].id)
        await message.reply(f"Removed {message.mentions[0].display_name} from admins")

    elif message.author.id not in owners and ("!removeadmin" in message.content or "!unadmin" in message.content):
        await message.reply("You don't have permission to use this command")

    elif message.author.id in owners and ("!removeadmin" in message.content or "!unadmin" in message.content) and message.mentions[0].id not in admins:
        await message.reply("they already not an admin or sum shit")

@client.event
async def on_message_delete(message: discord.Message):
    if message.channel.id in snipechannelids:
        if message.reference:
            deletedmessages.append(f"{message.author.display_name} ({message.author.name}) in <#{message.channel.id}>: {message.content} (replied to {message.reference.resolved.author.display_name})")
        else:
            deletedmessages.append(f"{message.author.display_name} ({message.author.name}) in <#{message.channel.id}>: {message.content}")

client.run("MTI5OTE2NjM1NjQ1Njg2OTkzMA.GqxA4d.75a4iF1j7bFgIwolRlaJ6HUR8OvxYj8L7RRpek")