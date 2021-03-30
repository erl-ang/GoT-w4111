import process_got_json
import py2neo
import pymysql
import graphs.got.gotdb as db

from graphs.got.got_graph import GotGraph

fg = GotGraph(auth=('neo4j', 'dbuserdbuser'),
              host="127.0.0.1",
              port=7687,
              secure=True)


def t1():
    cid = "b9308108-30c1-4a0b-86a6-fb4cdaf4baa8"
    q = "MATCH (n:Movie) RETURN n LIMIT 25"
    res = fg.run_q(q, None)
    for r in res:
        print("r = ", r)


def t2():
    res = db.get_characters()
    print("Res = ", res)


def t3():
    res = db.get_characters()

    for new_c in res:
        r = fg.create_node("Character", **new_c)


def t4():
    res = db.get_character_relationships()
    print("Res = ", res)


def t5():
    res = db.get_characters()

    for c in res:
        r = fg.get_character(c['character_id'])
        print("r = ", r)


def t6():
    res = db.get_character_relationships()

    for rel in res:
        r2 = fg.create_character_relationship(rel['source_ch_id'],
                                              rel['target_ch_id'], rel['label'])
        print("created " + str(rel))


t6()
