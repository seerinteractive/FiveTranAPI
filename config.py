import yaml
import sys
import os


with open(f"{sys.path[0]}/registry.yaml", "r") as stream:

    try:
        request_registry = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
