import requests
import json
    
r = requests.get("http://127.0.0.1:8000/")

re = json.dumps(r.json())

with open('apiconsumed.json', 'w') as f:
    f.write(re)
