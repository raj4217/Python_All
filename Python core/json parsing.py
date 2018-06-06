''' JavaScript Object Notation '''
import json

with open('states.json') as f:
    data = json.load(f)

# [print(state['name'],'   ',state['abbreviation']) for state in data['states']]
# [del state['area_codes'] for state in data['states']]
for state in data['states']:
    del state['area_codes']

with open('new_states_json','w') as wfile:
    # dum = json.dumps(data,indent = 2)
    json.dump(data,wfile, indent=2)







#----------------- loading json file
people_string = '''
    {
        "people":[
            {
            "name": "Dave Martin",
			"phone": "615-555-7164",
            "emails": ["davemartin@bogusemail.com","dave-martin@work.com"],
            "has_license": false
			},
			{
			"name": "Charles Harris",
			"phone": "800-555-5669",
			"emails": null,
            "has_license": true
			}
		]
	}
'''

data = json.loads(people_string)
# print(data)
# print((data['people'][1]['name']))
# [print(prsn['name']) for prsn in data['people']]
# for prsn in data['people']:
#     del prsn['phone']
#
# new_string  = json.dumps(data,indent = 2,sort_keys =2)
#
# print(new_string)