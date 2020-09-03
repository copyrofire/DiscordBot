import sqlite3


sql = ("INSERT INTO reports(text, string, text) VALUES (user,id,reason)")


#return all Records
def show_all():
    
    #connect db and create cursor
    db = sqlite3.connect('reports.db')
    cursor = db.cursor()

    cursor.execute("Select rowid, * FROM reports")
    items = c.fetchall()

    for item in items:
        print(item)

    #Commit our command
    db.commit()
    #Close our connection
    db.close()


def add_one(user, id,reason):
    #connect db and create cursor
    db = sqlite3.connect('reports.db')
    cursor = db.cursor()
    cursor.execute("INSERT INTO reports(?,?,?) VALUES (user,id,reason)")

    #Commit our command
    db.commit()
    #Close our connection
    db.close()
