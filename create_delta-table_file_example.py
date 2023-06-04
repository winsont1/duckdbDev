import deltalake as dl
import pandas as pd
from faker import Faker

#1. Create sample data using Faker
fake = Faker()

#2. Create fake names
name_list = []
for _ in range(1000):
    name_list.append(fake.name())

id_list = []
for i in range(1000):
    id_list.append(i)

#3. Read sample data into pandas dataframe df
df = pd.DataFrame({"id": id_list, "name": name_list})
dl.writer.write_deltalake(f"./tmp/delta-table-example", df)
