import discord

client = discord.Client()

@client.event
async def on_ready():
    print('ur in bitch, logged in as: {0.user}'.format(client))
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='porn'))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    
@client.event
async def on_message(ctx):
    emoji = '\N{EYES}'
    await ctx.add_reaction(emoji)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith(':'):
        await message.channel.send(':')
    if message.content.startswith('die'):
        await message.channel.send('no u')
    if message.content.startswith('shut up'):
        await message.channel.send('fuck you bitch')
    if message.content.startswith('smh'):
        await message.channel.send('*head has been shaked succesfully!*')
    if message.content.startswith('fuck me'):
        await message.channel.send('oh yes daddy, please fuck me')
    if message.content.startswith('based'):
        await message.channel.send('based indeed')
    if message.content.startswith('based'):
        await message.channel.send('fuck carl saying based, i say it now')
    if message.content.startswith('^^^'):
        await message.channel.send('^^^')
    if message.content.startswith('fuck you'):
        await message.channel.send('go fuck someone else')
    if message.content.startswith('pornhub'):
        await message.channel.send('https://pornhub.com')
    if message.content.startswith('yannis favorite porn'):
        await message.channel.send('https://www.pornhub.com/view_video.php?viewkey=ph5ef6a1d92ae1f')
    if message.content.startswith('stfu'):
        await message.channel.send('no u bitch')
    if message.content.startswith('who made shortbot'):
        await message.channel.send('<@720072050718277654>')
    if message.content.startswith('im back'):
        await message.channel.send('welcome back')
    if message.content.startswith('afk'):
        await message.channel.send('cya!')
    if message.content.startswith('gn guys'):
        await message.channel.send('good night')
    if message.content.startswith('joe'):
        await message.channel.send('whos joe?')
    if message.content.startswith('gus'):
        await message.channel.send('whos gus?')
    if message.content.startswith('amon gus'):
        await message.channel.send('NOOOOOO, u got me')
    if message.content.startswith('joe mama'):
        await message.channel.send('NOOOOOOO')
    if message.content.startswith('Joe'):
        await message.channel.send('whos joe?')
    if message.content.startswith('Gus'):
        await message.channel.send('whos gus?')
    if message.content.startswith('"test"'):
        await message.channel.send('test indeed')
    if message.content.startswith('are you horny?'):
        await message.channel.send('fuck yea man')
    if message.content.startswith('donate'):
        await message.channel.send('dm nitro gifts to gnad#7185, as he needs nitro so bad and he is gonna be so depressed and lonely and sadge and all the sad emotions until he gets nitro, he cant think without nitro, and is slowly dying inside bc he has no nitro. if this hasnt convinced you to gift him niro, idk what will as he rly needs it.')
    if message.content.startswith('code'):
        await message.channel.send('the code is here:')
    if message.content.startswith('straight'):
        await message.channel.send('ur gay')
    if message.content.startswith('i have an idea'):
        await message.channel.send('dm those to <@720072050718277654>')
    if message.content.startswith('light'):
        await message.channel.send(':rotating_light:')
    if message.content.startswith('boobs'):
        await message.channel.send('pls boobies')
    if message.content.startswith(':weary:'):
        await message.channel.send('STOP MOANING')
    if message.content.startswith('no bitch'):
        await message.channel.send('yes bitch')
        
