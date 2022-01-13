from login import get_headers
import requests
import json

with open('workflow.json') as f:
    workflow = json.load(f)

r = requests.post(f'https://dafni-nims-api.secure.dafni.rl.ac.uk/workflows/validate/',
                  headers=get_headers(), json={'definition': workflow})
print(r.text)
r.raise_for_status()
