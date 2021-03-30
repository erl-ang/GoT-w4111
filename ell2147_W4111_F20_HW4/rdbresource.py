import pymysql
import copy

conn = pymysql.connect(
    user="dbuser",
    password="dbuserdbuser",
    host="localhost",
    cursorclass=pymysql.cursors.DictCursor,
    # db="W4111GoTHWClean"
    db="gotf20raw"
)


def get_by_by_query(db_name, table_name, args):

    tname = db_name + "." + table_name

    q_string = dict(copy.copy(args))
    terms = []
    vals = []

    for k,v in q_string.items():
        terms.append(str(k) + "=%s")
        vals.append(v)

    if len(terms) > 0:
        wc = " WHERE " + " AND ".join(terms)
    else:
        wc = ""

    q = "SELECT * FROM " + tname + " " + wc;

    cur = conn.cursor()
    print("SQL = ", cur.mogrify(q, vals))
    res = cur.execute(q, args=vals)
    res = cur.fetchall()
    return res