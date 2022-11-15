import json

fo = open('/home/nilanjan/Desktop/Python For DevOps/PythonScripts/modules/json_module/sample.json', 'r')

# print(fo.read())

print(json.load(fo).get('glossary').get('GlossDiv').get('GlossList'))