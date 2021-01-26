#!/usr/bin/env python3
import os
import json
print('Content-Type:text/html')
print()
print("""
<!doctype html>
<html>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

<body>
""")
print("""<h1> Paramters passed</h1>
<br>
<table class="table table-striped mx-5">
  <thead>
    <tr>
      <th scope="col">Query parameter</th>
      <th scope="col">Value</th>
    </tr>
    </thead>
    <tbody>
""")
for parameter in os.environ['QUERY_STRING'].split('&'):
    (name, value) = parameter.split('=')
    print(f"<tr><td>{name}</td> <td>{value}</td></tr>")
print("""</tbody>
</table>
</body>
</html>
""")
