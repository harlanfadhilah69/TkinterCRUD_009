import sqlite3
con = sqlite3.connect("DB1.db")
cur = con.cursor()
cur.execute("""

    CREATE TABLE TBL1
            (col1 int, col2 text)

""")

con.commit()