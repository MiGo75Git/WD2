from smartninja_sql.sqlite import SQLiteDatabase

def hw_lesson1():
    # connect database
    db = SQLiteDatabase("Chinook_Sqlite.sqlite")

    # Write an SQL command that will print Name from the table Artist (for all the database entries)
    db.pretty_print("SELECT Name FROM ARTIST")

    # Print all data from the table Invoice where BillingCountry is Germany
    db.pretty_print("SELECT * FROM Invoice WHERE BillingCountry = 'Germany'")

    # Count how many albums are in the database.
    db.pretty_print("SELECT 'All albums ' as info, COUNT(*) AS [Count] FROM Album")

    # How many customers are from France?
    db.pretty_print("SELECT 'France albums ' as info ,COUNT(*) AS [Count] FROM Invoice WHERE BillingCountry = 'France'")

    # Look into the SQL documentation for help. Hint: look for Min&Max and Count, Avg, Sum.
    db.pretty_print("""SELECT 	t.MediaTypeId, m.Name as codec,
                                t.GenreId, g.Name as Genre_name,
                                COUNT(*) AS Num_of_songs, SUM(Milliseconds)/1000/60 as Sum_Time_min, AVG(UnitPrice) as Avg_Price, sum(Bytes) as [Num_of_Bytes] 
                                FROM Track as t 
                                LEFT JOIN MediaType as m on t.MediaTypeId = m.MediaTypeId
                                LEFT JOIN Genre as g on t.GenreId = g.GenreId 
                                group by t.MediaTypeId, t.GenreId 
                    """)

    # Look into the SQL documentation for help. Hint: look for Min&Max and Count, Avg, Sum.

    db.pretty_print("""SELECT 	t.MediaTypeId, m.Name as codec, 		
                                COUNT(*) AS Num_of_songs, SUM(Milliseconds)/1000/60 as Sum_Time_min, AVG(UnitPrice) as Avg_Price, sum(Bytes) as [Bytes] 
                                FROM Track as t 
                                LEFT JOIN MediaType as m on t.MediaTypeId = m.MediaTypeId
                                group by t.MediaTypeId
                    """)

