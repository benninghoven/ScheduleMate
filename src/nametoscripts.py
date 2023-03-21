import json
from getparentdir import GetParentDir

def NameToScripts(name: str) -> str:

    name = name.upper()

    parentDir = GetParentDir()
    with open(f'{parentDir}/data/tasks.json', 'r') as f:
        data = json.load(f)

    for task, scripts in data.items():
        if name == task:
            return scripts

    return ["echo NOTHING FOUND!"]
