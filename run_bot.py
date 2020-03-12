# Feel free to PR and fix attrocious string code, still learning python
import discord
import requests
from datetime import datetime

client = discord.Client()

# This is where your discord token should go
TOKEN_FILE = "token.txt"
TOKEN = ""
with open(TOKEN_FILE) as f:
	TOKEN = f.readline()

# There is a more comprehensive API available at https://coronavirus.john-coene.com/#/ but this works just fine for what I am trying to do.
API_URL = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/query?f=json&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Confirmed%22%2C%22outStatisticFieldName%22%3A%22confirmed%22%7D%2C%20%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Deaths%22%2C%22outStatisticFieldName%22%3A%22deaths%22%7D%2C%20%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Recovered%22%2C%22outStatisticFieldName%22%3A%22recovered%22%7D%5D'

# Sources
DASHBOARD_LINK = 'https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6'
DATA_LINK = 'https://github.com/GuangchuangYu/nCov2019'

# Symbols - any symbol will work here as long as the bot has access to it
NEUTRAL_SYMBOL = ':biohazard:'
BAD_SYMBOL = ':skull_crossbones:'
GOOD_SYMBOL = ':smile_cat:'

SPACING = "".rjust(50, " ")

STATS_STRING = """
,%s Total Cases: %s %s \n
,%s Total Recovered: %s %s\n
,%s Total Deaths: %s %s"""

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('!stats'):
		log("USER %s requested !stats" % message.author)
		await message.channel.send('Hold on - I\'m checking.')
		response = requests.get(API_URL)
		if response.status_code != 200:
			await message.channel.send('There was an error getting the status')
			await message.channel.send('Response Status: %s' % response.status_code)
			await message.channel.send(response.json())
			return
		data = response.json()['features']
		data = data[0]['attributes']

		to_send = "COVID-2019 Stats as of %s UTC\n" % datetime.utcnow() + STATS_STRING.replace(",", SPACING) % (
						NEUTRAL_SYMBOL, data['confirmed'], NEUTRAL_SYMBOL, 
						GOOD_SYMBOL, data['recovered'], GOOD_SYMBOL,
						BAD_SYMBOL, data['deaths'], BAD_SYMBOL)
						
		await message.channel.send(to_send)

	if message.content.startswith('!dashboard'):
		log("USER %s requested !dashboard" % message.author)
		await message.channel.send('A more comprehensive dashboard is located at %s' % DASHBOARD_LINK)

	if message.content.startswith('!data'):
		log("USER %s requested !data" % message.author)
		await message.channel.send('The raw data can be found at %s' % DATA_LINK)

	if message.content.startswith('!commands'):
		log("USER %s requested !commands" % message.author)
		await message.channel.send('The available commands are !stats, !dashboard, !data')
		
async def check_stats(message):
	await message.channel.send('In the stats method')
	
def log(message):
	print("[%s] %s" % (datetime.utcnow(), message))

client.run(TOKEN)