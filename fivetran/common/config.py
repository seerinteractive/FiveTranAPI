import yaml
import sys
import os

path = os.path.dirname(os.path.abspath(__file__))

with open(f"{path}/registry.yaml", "r") as stream:

    try:
        request_registry = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
