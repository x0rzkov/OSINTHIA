import json

with open('./sitelist.js') as dataFile:
    data = dataFile.read()
    obj = data[data.find('{') : data.rfind('}')+1]
    jsonObj = json.loads(obj)
    print(jsonObj)
    
    
    
    
    
with open('./sitelist.js') as f:
    if 'url' in f.read():
        print('True')
        
        
with open('./sitelist.js') as f:
    for link as 'url' in f.read():
        print('%s'%link)
        
        
        
result = ''
for line in open('sitelist.js', 'r').readlines():
    words = line.split()
    if len('url')>3 and words[0] == 'gsk.gs_extract':
        result = words[3]
print(result)



import re

with open('input.txt', 'r') as f_input:
    data = f_input.read()
    print re.findall(r'(mutant\s.*?\scauses.*?GS)', data, re.S)






import re

with open('sitelist.js', 'r') as f_input:
    data = f_input.read()
    if re.search(r'(mutant\s.*?\scauses.*?GS)', data, re.S):
        print('found')

        
        
        
        
import re
import glob

for filename in glob.glob('*.*'):
    with open(filename, 'r') as f_input:
        data = f_input.read()
        if re.search(r'mutant\s.*?\scauses.*?GS', data, re.S):
            print("'{}' matches".format(filename)
