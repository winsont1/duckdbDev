from deltalake import DeltaTable
import duckdb

#1. Read sample delta-table file "delta-table-sample" using delta-lake library into a delta-table object
dt = DeltaTable("delta-table-sample")

#2. Read delta-table file object into pyarrow object (in-memory columnar database)
pyarrow_dataset = dt.to_pyarrow_dataset()

#3. Initiate duckdb OLAP database. Read pyarrow object into duckdb OLAP database for querying.
sample_dataset = duckdb.arrow(pyarrow_dataset)

print(dt.history)
print(dt.schema().json())

print(sample_dataset)

# Note: The name of the duckdb.arrow table variable is the name of the variable it is saved to, sample_dataset

#4. Let's write a query for the sample_dataset
query = '''
  select * from sample_dataset
'''

#5. Run duckdb query and print result
result = duckdb.query(query)
print(result)

#6. Read duckdb query into a dataframe. Print Dataframe
df = duckdb.query(query).to_df()
print(df)
