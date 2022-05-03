import pandas as pd
import json

df = pd.read_csv('Data_API.csv',nrows=10000,low_memory=False)
df = df.reset_index()

j = {"nodes": [], "links": []}
ids = set()

for index, row in df.iterrows():
    x = str(row['Seller_address'])
    y = str(row['Buyer_address'])
    z = str(row['Category'])
    if x not in ids:
        ids.add(x)
        j["nodes"].append({
          "id": x,
          "name": x,
          "category" : z,
          "val": 1
        })

    if y not in ids:
        ids.add(y)
        j["nodes"].append({
          "id": y,
          "name": y,
          "category" : z,
          "val": 1
        })
        
    j["links"].append({
            "source": x,
            "target": y
        })

#print(json.dumps(j))
with open('bestseller.json', 'w') as f:
    json.dump(j, f)
