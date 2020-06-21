from smartninja_sql.sqlite import SQLiteDatabase
from HW_Lesson1 import hw_lesson1

db = SQLiteDatabase("testing.sqlite")
# db.execute("""CREATE TABLE IF NOT EXISTS User (
#             id integer PRIMARY KEY AUTOINCREMENT,
#             name text NOT NULL,
#             age integer);""")
#
# db.print_tables(verbose=True)

hw_lesson1()







