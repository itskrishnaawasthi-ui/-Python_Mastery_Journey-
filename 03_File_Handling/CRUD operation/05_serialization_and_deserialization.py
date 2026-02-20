# for reading /writing more complicated data in form of different data types we use module JSON .
#serialization / deserialization a list i.e dump and load 
import json
lisv= [12,334,22,3223,42,3,656,7676,56,545545,4,4,54,44,43,43,43,767,67,4324]
with open("sampledata","w+") as f:
 json.dump(lisv,f)
 f.seek(0)  # move to the begninning of the file
 ist=json.load(f)
 print(ist)
 
 #--serialization / deserialization a tuple
import json
tup=(2,54,55,"ram")
with open("sampledata","w+") as f:
  json.dump(tup,f)
  f.seek(0)     # move to the begninning of the file
  show=json.load(f)
  print(tuple(show))

# we can also add nested list and dictionary likewise----
import json
contact=[12,[21,334,434],["rahul","ram"]]
with open("data","w+") as f :
 json.dump(contact,f)
 f.seek(0)          # move to the begninning of the file
 shown=json.load(f)
 print(shown)
