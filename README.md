# What it is:
Just a bot to see the current stats of COVID 2019 (# cases, # recovered, # deaths)

# Commands
 + !stats - gives the stats
 + !data - view source data (alternatively, it's here: [nCov2019](https://github.com/GuangchuangYu/nCov2019) 
 + !dashboard - view dashboard created from source data (alternatively, it's here: [Coronavirus COVID-19](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)
 + !commands - view available commands from above

# Set up:
(assumes Discord Bot exists and is added to server)

Get your Discord Bot token and create a file "token.txt" in the same directory as "run_bot.py" then:

``` python
pip install requests discord
python run_bot.py
```

Might make this a bit more comprehensive soon - mostly wanted to work on my Python outside of a Spark context and this seemed interesting to me