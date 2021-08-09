import sqlite3 as sqlite

# --=== CONSTANTS ===--
DATABASE_FILE = "tags.db"

# Connection
con = sqlite.connect(DATABASE_FILE)


def add_tag(tag_name, guild_id, response_text):
    cur = con.cursor()
    cur.execute("INSERT INTO tags (TagName, GuildID, ResponseText) VALUES (?, ?, ?)",
                (tag_name, guild_id, response_text))
    con.commit()


def get_tags_by_guild(guild_id):
    cur = con.cursor()
    cur.execute("SELECT TagName FROM tags WHERE GuildID = '%s'" % guild_id)
    tags = cur.fetchall()
    tags = list(map(lambda x: x[0], tags))
    return tags


def get_tag_by_name_and_guild(tag_name, guild_id):
    cur = con.cursor()
    cur.execute("SELECT ResponseText FROM tags WHERE TagName = '%s' AND GuildID = '%s'" % (tag_name, guild_id))
    return cur.fetchone()[0]


def remove_tag_by_name_and_guild(tag_name, guild_id):
    cur = con.cursor()
    cur.execute("DELETE FROM tags WHERE TagName = '%s' and GuildID = '%s'" % (tag_name, guild_id))
    con.commit()


def edit_tag_by_name_and_guild(tag_name, guild_id, response_text):
    cur = con.cursor()
    cur.execute("UPDATE tags SET ResponseText = '%s' WHERE TagName = '%s' AND GuildID = '%s'"
                % (response_text, tag_name, guild_id))
    con.commit()


def add_admin(admin_id, guild_id):
    cur = con.cursor()
    cur.execute("INSERT INTO admins (AdminID, GuildID) VALUES(?, ?)", (admin_id, guild_id))
    con.commit()


def get_admins():
    cur = con.cursor()
    cur.execute("SELECT * FROM admins")
    admins = cur.fetchall()
    admins = list(map(lambda x: x[0], admins))
    return admins


def get_admins_by_guild(guild_id):
    cur = con.cursor()
    cur.execute("SELECT AdminID FROM admins WHERE GuildID = %s" % guild_id)
    admins = cur.fetchall()
    admins = list(map(lambda x: x[0], admins))
    return admins


def remove_admin_by_guild_and_id(guild_id, admin_id):
    cur = con.cursor()
    cur.execute("DELETE FROM admins WHERE GuildID = '%s' AND AdminID = '%s'" % (guild_id, admin_id))
    con.commit()


def get_triggers_by_guild(guild_id):
    cur = con.cursor()
    cur.execute("SELECT Triggers FROM quickresponses WHERE GuildID = '%s'" % guild_id)
    triggers = cur.fetchall()
    triggers = list(map(lambda x: x[0], triggers))
    triggers = list(map(lambda x: x.split(", "), triggers))
    return triggers


def get_triggers_and_ids_by_guild(guild_id):
    cur = con.cursor()
    cur.execute("SELECT ID, Triggers FROM quickresponses WHERE GuildID = '%s'" % guild_id)
    triggers = cur.fetchall()
    return triggers


def get_response_by_guild_and_triggers(guild_id, triggers):
    cur = con.cursor()
    cur.execute("SELECT Response FROM quickresponses WHERE GuildID = '%s' AND Triggers = '%s'" %
                (guild_id, triggers))
    response = cur.fetchone()[0]
    return response
