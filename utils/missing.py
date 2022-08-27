import json

def find_missing(delivery_list, bag):
  f = open('data/items.json',)
  data = json.load(f)
  lstmissingval = []
  for missval in delivery_list:
    if missval not in bag:
      lstmissingval.append(missval)
  
  lstval = []
  for i in lstmissingval:
    for j in data:
      if j['id'] == i: 
        lstval.append(j)      
  return lstval
      
      

