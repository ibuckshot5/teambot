import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='I add teams! Type !help in #helpdesk.'))

@client.event
async def on_message(message):
    if message.content == "!help":
        await client.send_message(message.channel, "Use `!team (blue | red | yellow)` or `!team (mystic | valor | instinct)` to choose a team.\n\n**Remember to show the moderators a picture of your character, else you might get kicked.**")
    if message.content.startswith("!team"):
        team_list = ["team-mystic", "team-instinct", "team-valor"]
        entered_team = message.content.lower()
        role = discord.utils.get(message.server.roles, name=entered_team)
        roles = [
            # IDs of the roles for the teams
            "306376567624302592",
            "306376804279648260",
            "306376717788905473",
        ]
        for r in message.author.roles:
            if r.id in roles:
                # If a role in the user's list of roles matches one of those we're checking
                await client.send_message(message.channel,
                                          "You already have a team role. If you want to switch, message a moderator.")
                return
        if message.content == "!team red" or message.content == "!team valor":
            role = discord.utils.get(message.server.roles, name="team-valor")
            try:
                await client.add_roles(message.author, role)
                await client.send_message(message.channel, "Successfully added role {0}.\n\n**Remember to show the moderators a picture of your character, else you might get kicked.**".format(role.name))
            except discord.Forbidden:
                await client.send_message(message.channel, "I don't have perms to add roles.")
        elif message.content == "!team yellow" or message.content == "!team instinct":
            role = discord.utils.get(message.server.roles, name="team-instinct")
            try:
                await client.add_roles(message.author, role)
                await client.send_message(message.channel, "Successfully added role {0}.\n\n**Remember to show the moderators a picture of your character, else you might get kicked.**".format(role.name))
            except discord.Forbidden:
                await client.send_message(message.channel, "I don't have perms to add roles.")
        elif message.content == "!team blue" or message.content == "!team mystic":
            role = discord.utils.get(message.server.roles, name="team-mystic")
            try:
                await client.add_roles(message.author, role)
                await client.send_message(message.channel, "Successfully added role {0}.\n\n**Remember to show the moderators a picture of your character, else you might get kicked.**".format(role.name))
            except discord.Forbidden:
                await client.send_message(message.channel, "I don't have perms to add roles.")
        else:
            # If the role wasn't found by discord.utils.get() or is a role that we don't want to add:
            await client.send_message(message.channel,
                                      "Team doesn't exist. Teams that do are `blue`, `red`, and `yellow`.\nBlue is Mystic, red is Valor, and yellow is Instinct.")
            return

client.run('MzI3OTg5MDE0MzI3OTg0MTI4.DC9XHw.n-69vI_fMin_-SSkjMYIUextH3U')