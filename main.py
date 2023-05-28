import duckdb
import polars as pl
import sqlalchemy

# conn = duckdb.connect()

conn = duckdb.connect(database='db.duckdb', read_only=False)


print(conn.execute("""
CREATE TABLE IF NOT EXISTS new_etf_table(
Date DATE,
Low DOUBLE,
Open DOUBLE,
Close DOUBLE,
High DOUBLE,
AdjClose DOUBLE,
Volume INTEGER);
COPY new_etf_table FROM 'nasdaq_archive/etfs/AAAU.csv' ( HEADER);
SELECT MAX(Low) FROM new_etf_table;
""").fetchall())
