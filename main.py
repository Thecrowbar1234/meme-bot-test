import discord
import keep_alive
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>random'):
      if message.content.endswith(' meme'):
        meme = random.randint(1,6)
        if meme == 1 :
          await message.channel.send('https://tenor.com/view/flamingelmomeme-flaming-flamingelmo-elmo-memes-gif-10674657')
        elif meme == 2 :
          await message.channel.send('https://tenor.com/view/sanesss-sans-undertale-unitale-gif-5478072')
        elif meme == 3 :
          await message.channel.send('https://www.youtube.com/watch?v=MAlSjtxy5ak')
        elif meme == 4 :
          await message.channel.send('https://media3.giphy.com/media/AQz3wCDgDX3HO/giphy.gif')
        elif meme == 5 :
          await message.channel.send('https://media.giphy.com/media/XDAY1NNG2VvobAp9o0/giphy.gif')
        elif meme == 6 :
          await message.channel.send('https://media.giphy.com/media/YWf50NNii3r4k/giphy.gif')
        elif meme == 7 :
          await message.channel.send('https://www.youtube.com/watch?v=cPJUBQd-PNM')
      else:
        await message.channel.send('⚠️cannot recognize meme type⚠️')
    elif message.content.startswith('>search'):
      if message.content.endswith(' nuclear elmo'):
        await message.channel.send('https://tenor.com/view/flamingelmomeme-flaming-flamingelmo-elmo-memes-gif-10674657')
      elif message.content.endswith(' Sans the meme skeleton'):
        await message.channel.send('https://tenor.com/view/sanesss-sans-undertale-unitale-gif-5478072')
      elif message.content.endswith(' Every programming tutorial'):
        await message.channel.send('https://www.youtube.com/watch?v=MAlSjtxy5ak')
      elif message.content.endswith(' Patricks wierd butt'):
        await message.channel.send('https://media3.giphy.com/media/AQz3wCDgDX3HO/giphy.gif')
      elif message.content.endswith(' STONKS'):
        await message.channel.send('https://media.giphy.com/media/XDAY1NNG2VvobAp9o0/giphy.gif')
      elif message.content.endswith(' MAKE DANK MEMES'):
        await message.channel.send('https://media.giphy.com/media/YWf50NNii3r4k/giphy.gif')
      elif message.content.endswith(' creeper aw man'):
        await message.channel.send('https://www.youtube.com/watch?v=cPJUBQd-PNM')
      else :
        if message.content.endswith('search'):
          await message.channel.send('⚠️You don\'t have a search term⚠️')
        else :
          await message.channel.send('⚠️cannot find your dank meme⚠️')
    elif message.content.startswith('>')  :
      await message.channel.send('⚠️command not recognized⚠️')
keep_alive.keep_alive()
client.run('Token that might have been used for malicious puroses.')
