from login import get_headers
import requests
import json
from parameter_sets import parameter_sets

version_message = 'Uploaded from GitHub'
parent_workflow = '4957fd9a-0dff-47ae-9726-30162284b752'

# Login

headers = get_headers()

# Upload the workflow

with open('workflow.json') as f:
    workflow = json.load(f)

r = requests.post(f'https://dafni-nims-api.secure.dafni.rl.ac.uk/workflows/{parent_workflow}/upload/',
                  headers=headers, json={'definition': workflow, 'version_message': version_message})
print(r.text)
r.raise_for_status()
workflow_version = r.json()['workflow_version_id']

# Upload parameter sets

for parameter_set in parameter_sets(workflow_version):
    r = requests.post(f'https://dafni-nims-api.secure.dafni.rl.ac.uk/workflows/parameter-set/upload/',
                      headers=headers, json=parameter_set)
    print(r.text)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Delete the workflow

        r = requests.delete(f'https://dafni-nims-api.secure.dafni.rl.ac.uk/workflows/delete/{workflow_version}/',
                            headers=headers)
        raise e
