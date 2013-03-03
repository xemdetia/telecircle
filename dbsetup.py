
import os
import sqlite3

def sql_file_filter(x):
    if x[-3:] == "sql":
        return x
    else:
        return False

def sqlite_setup(filepath):

    # connect to the selected filepath
    conn = sqlite3.connect(filepath)

    # get scripts from the directory
    for i in filter( sql_file_filter, os.listdir('setup/db/sqlite')):
        with open('setup/db/sqlite/'+i, 'r') as f:
            print "[SQLite] running "+i+"..."
            c = conn.cursor()
            c.executescript(f.read())

    return conn # give us a reference to this database

if __name__ == "__main__":
    print "Setting up database:"
    dbchoice = raw_input( "Do you want to use SQLi(t)e or (P)ostgres? (t/p):" )

    if dbchoice == "t" or dbchoice == "T":
        filepath = raw_input( "Where do you want the sqlite database to be stored? (Default=./telecircled.sqlite): ")
        if filepath == "":
            print "Default of ./telecircled.sqlite was chosen."
            filepath = "./telecircled.sqlite"
        else:
            print "Using "+filepath+" as the file for the database."
    
        sqlite_setup(filepath)
    

