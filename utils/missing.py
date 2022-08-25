import json

def find_missing(delivery_list, bag):
  f = open('data/items.json',)
  data = json.load(f)
  return data