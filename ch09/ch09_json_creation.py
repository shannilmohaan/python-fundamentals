import json

# create a python dictionary object accounts

accounts_dict = {"accounts":[
                            {"account":100,"name":"Shanil","balance":100.50},
                            {"account":200,"name":"Ramya","balance":200.50},
                            {"account":300,"name":"Aarav","balance":300.50}
                            ]
                }
#print(accounts_dict['accounts'][0]['name'])

# write this to a json file
with open ("accounts.json", mode = 'w') as accounts_json:
    json.dump(accounts_dict,accounts_json)
