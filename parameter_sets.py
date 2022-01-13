import json
from jinja2 import Template


def parameter_sets(workflow_version):
    with open('parameter_set.json') as f:
        template = Template(f.read())

    sets = []
    for ssp in [1, 2, 3, 4, 5]:
        s = template.render(year=2050, ssp=ssp, output_name=f'SSP{ssp} Flood', workflow_version=workflow_version)

        sets.append(json.loads(s))
    return sets
