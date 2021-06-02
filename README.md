# tagDiscordBot
A discord.py bot used to store and recall tags.  It has full multi-guild support with the ability add admins (the first has to be added to the guild directly to the database at the moment).

# Setup guide
## Token
The token is stored in a file called `constants.py` in the root.  You must create this with the following variable(s):
- `BOT_TOKEN` and set this to your token as a string, i.e. `BOT_TOKEN = "<paste your token here>"`

## The database
The bot uses a SQLite database.  To start with, you can use this database as it has the correct structure, but it is recommended that you install the [SQLite DB Browser application](https://sqlitebrowser.org/) to easily edit the database, as you need to add the initial admin.

### Adding the first admin
- Open SQLite DB Browser and open the `tags.db` database.
- Go to Browse Data and select the `admins` table.  Clear out the current entries and add a new one.  `AdminID` should be the ID of the user you want to be an admin, and the `GuildID` should be the ID of the server you want them to be an admin in.
- Click Write Changes, then Close Database.

If you wish, you can clear out the entries in the `tags` table as these exist for my testing guild, and so take up some space.  These will not show up in your server(s).

## Running the bot
Make sure you fulfil the prerequisite constants file.

The bot is supplied in a venv, so you should use that as it already contains discord.py.  The entrypoint is `main.py` - run this with Python 3.8 to start the bot.
