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
browser_info = os.environ['HTTP_USER_AGENT']
print(f"""<h1> User browser</h1> <p class="px-5">{browser_info}</p>""")
print("""
<br>
<hr>
<b>Question 3</b>: What environment variable contains information about the user's browser?
<p class="px-5 py-2">'HTTP_USER_AGENT'</p>
</body>
</html>
""")
