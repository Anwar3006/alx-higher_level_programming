#!/usr/bin/python3

import _mysql
import sys

if __name__ == "__main__":
    db = _mysql.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    print(db)
    # cur = db.cursor()
    # cur.execute("SELECT * FROM `states` ORDER BY `id`")
    # [print(state) for state in cur.fetchall() if state[1][0] == "N"]
