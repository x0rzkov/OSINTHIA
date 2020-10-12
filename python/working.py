import json 
  
# Opening JSON file 
f = open('./sitelist.js',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 
for i in data['children']:
    for x in i['children']:
        for y in x['children']:
            print(y['url']) 

f.close()






import json

with open('./sitelist.js','r') as sitelist:
    sitelist_json = json.load(sitelist)
sitelist_json['children'][0::]