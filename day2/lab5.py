#lab5.py
import pickle
import json

config = {
          "loc1" : {"city" : "blr", "vals" : [10,20,30]},
          "loc2" : {"city" : "chn", "vals" : [40,50,60]}
         }

with open("config.pkl", "wb") as f:
    pickle.dump(config, f)

rd= open("config.pkl", "rb")
res= pickle.load(rd)
print(res)
rd.close()

print("\n\nJSON file: ", json.dumps(config))