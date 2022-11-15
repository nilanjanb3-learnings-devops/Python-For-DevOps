import json

fo = open('/home/nilanjan/Desktop/Python For DevOps/PythonScripts/modules/json_module/my_skill.json', 'w')

my_skill = {'name':'nilanjan', 'skills':['git', 'python', 'docker', 'kubernetes', 'Azure']}
json.dump(my_skill, fo, indent=4)

fo.close()