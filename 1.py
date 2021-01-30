import pandas
import sqlite3
def DataToDatabase():
    data = pandas.read_csv("CTA-Ridership-L-Station-Entries-Daily-Totals.csv", names=['station_id','stationname','date','daytype','rides'], skiprows=[0])
    conn = sqlite3.connect("mydatabase.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE rides (station_id int, stationname text, date text, daytype text, rides int)")

    for i in range(len(data)):
        a = int(data['station_id'][i])
        b = data['stationname'][i]
        c = data['date'][i]
        d = data['daytype'][i]
        e = int(data['rides'][i])
        sql = "INSERT INTO rides (station_id, stationname, date, daytype, rides) VALUES (:station_id, :stationname, :date, :daytype, :rides)"
        cur.execute(sql, {"station_id":a, "stationname":b, "date":c, "daytype":d, "rides":e})
    conn.commit()
    conn.close()

def display_all_db_data():
    conn = sqlite3.connect('cta_table.db')
    cur = conn.cursor()
    sql = "SELECT * FROM rides" # * shorthand for all columns of the table
    columns = cur.execute(sql)
    all_entries = columns.fetchall()
    for entry in all_entries:
        print(entry)

display_all_db_data()
