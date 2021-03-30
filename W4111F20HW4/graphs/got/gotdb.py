import pymysql

conn = pymysql.connect(
    user="dbuser",
    password="dbuserdbuser",
    host="localhost",
    cursorclass=pymysql.cursors.DictCursor,
    db="W4111GoTHWClean"
)


def get_characters():

    q = "SELECT character_id, characterName FROM gotf20raw.characters;"
    cur = conn.cursor()
    res = cur.execute(q)
    res = cur.fetchall()
    return res


def get_character_relationships():

    q = """
    SELECT
	a.character_id as source_ch_id, label, b.character_id as target_ch_id
    from character_relationships as a left join characters as b
    on value=b.characterName
    where b.character_id is not NULL;"""

    cur = conn.cursor()
    res = cur.execute(q)
    res = cur.fetchall()
    return res

