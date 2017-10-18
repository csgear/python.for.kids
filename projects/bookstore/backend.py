
import sqlite3

def connect():
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS book(id integer primary key, title text, author text, year integer, isbn integer)")
	conn.commit()
	conn.close()

def insert(title, author, year, isbn):
	conn = sqlite3.connect("books.db")
	cur = conn.cursor() 
	cur.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?) ", (title, author, year, isbn)) 
	conn.commit() 
	conn.close() 

def view():
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM book")
	rows = cur.fetchall()
	conn.close()
	return rows 

def search(title="", author="", year="", isbn=""):
	conn = sqlite3.connect("books.db")
	cur = conn.cursor() 
	cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
	rows = cur.fetchall()
	conn.close() 
	return rows

def delete(id):
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM book WHERE id = ?", (id))
	conn.commit()
	conn.close() 

if __name__ == "__main__":
	connect() 
	insert("波西杰克逊1", "杨明曦", 2017, 2881201)


