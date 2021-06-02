# tagDiscordBot
A discord.py bot used to store and recall tags.  It has full multi-guild support with the ability add admins (the first has to be added to the guild directly to the database at the moment).

# Setup guide
## Token
The token is stored in a file called `constants.py` in the root.  You must create this with the following variable(s):
- `BOT_TOKEN` and set this to your token as a string, i.e. `BOT_TOKEN = "<paste your token here>"

## Running the bot
Make sure you fulfil the prerequisite constants file.

The bot is supplied in a venv, so you should use that as it already contains discord.py.  The entrypoint is `main.py` - run this with Python 3.8 to start the bot.
