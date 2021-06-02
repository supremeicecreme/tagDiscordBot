import discordHandler
import dataAccess

if __name__ == "__main__":
    guild_id = "395274402901524480"
    tags = dataAccess.get_tags_by_guild(guild_id)
    print(tags)
    discordHandler.kickstart()
