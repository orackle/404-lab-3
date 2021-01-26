#!/usr/bin/env python3
import os
import json
print('Content-Type: application/json')
print()
print(json.dumps(dict(os.environ), indent=2))
print("\n\n")
if(os.environ['QUERY_STRING']):
    print(os.environ['QUERY_STRING'])
else:
    print("no query parameters passed")
