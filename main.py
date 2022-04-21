import discord 
import os #ahh the joy of free features thx
import requests #allows us to make a http request to get stuff from a api
import json#helps return data
import random
TOKEN = 'ya key'

client = discord.Client() #part of the discord library
sad_words = ["sad","depressed","unhappy","angry","miserable","depressing"]

starter_encouragements = [
  "cheer up",
  "head ups",
  "You are a great person/bot!",
  "you're the smartest entity ive ever met and never forget that :D"
]
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  #going to get us a random quote
  json_data=json.loads(response.text) #from documentation
  quote = json_data[0]['q']+" ~"+ json_data[0]['a']
  return (quote)


@client.event
async def on_ready(): #discord library when bot is ready to go
  print('We have logged in as {0.user}'.format(client))
  #its going to replace user as who ever the client is
  
@client.event
async def on_message(message):# discord library when message is sent 'message' being a varaible
  username =str(message.author).aplit('#')[0] #get username of sender
  user_message = str(message.content) #get the message as string
  channel =str(message.channel.name) #channel name
  print(f'{username}: {user_message} ({channel})') 

  if message.author == client.user:
    return    # if the bot sent something don't send anything back

  if message.channel.name == 'only-random-greetings': # its a channel name you have on discord
    uml = user_message.lower()
    if uml=="hello":
      await message.channel.send(f'Hello {username}!')
      return
    elif uml=="bye":
      await message.channel.send(f"Bye {username}! :D")
      return
    elif uml=='!random':
      reponse=f'Your random number is: {random.randrange(10)}'
      await message.channel.send(response)
      return 
    

  msg = message.content #shorten it I have a feeling its a reoccuring thing to type...
#this is okay this is okay any channel
  if msg.startswith('$inspire'):
    quote = get_quote() #refences function get_quote from above and sends back the quote and author
    await message.channel.send(quote)#sends a quote from api back
  if msg.startswith('$hello'):
      await message.channel.send('hello!')#sends a hello! back
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))  
  
#client.run(TOKEN)  
#client.run(os.getenv('TOKEN'))
client.run(os.environ['popoff'])
#going to use a envornemnt varible to protect key the name is popoff cause this discord bot will pop off somehow on the cloud
