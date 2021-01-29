#!/usr/bin/env python3
import templates
import os
import json
import secret
import http.cookies as Cookie
import cgi
print("Content-Type: text/html\n")
# Q1
# -------------------------------------------
# print('Content-Type: application/json')
# print()
# print(json.dumps(dict(os.environ), indent=2))
# -----------------------------------------

# Q2
# -----------------------------------------
# print('Content-Type: application/json')
# print()
# print(json.dumps(dict(os.environ), indent=2))
# print("\n\n")
# if(os.environ['QUERY_STRING']):
#     print(os.environ['QUERY_STRING'])
# else:
#     print("no query parameters passed")
# -----------------------------------------

# Q3
# -----------------------------------------
#print(os.environ["HTTP_USER_AGENT"])
# -----------------------------------------

# Q4
# how to fetch values stored in cgi module
# from Bharel on stackoverflow https://stackoverflow.com/users/1658617/bharel
# https://stackoverflow.com/questions/36508304/how-do-i-properly-get-formdata-using-pythons-cgi-module
# -----------------------------------------
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")
form_validate = False
if username == secret.username and password == secret.password:
    form_validate = True


# Q5
# # -----------------------------------------
# if cookie sent via http headers
# instantiate a SimpleCookie object and store cookie sent
# check against form values
#
# setting a cookie from: http://cgi.tutorial.codepoint.net/set-the-cookie
# instantiate and retrieve cookie from: http://cgi.tutorial.codepoint.net/retrieve-the-cookie
# -----------------------------------------
cookie = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))
cookie_username = None
cookie_password = None
validated = False
# print(cookie)

if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

if cookie_username == secret.username and cookie_password == secret.password:
    validated = True


if validated:
    username = cookie_username
    password = cookie_password

if form_validate:                                     # setting a cookie
    print("Set-Cookie: username=", username)          # send to HTTP headers
    print("Set-Cookie: password=", password)

# print(cookie_username, username)
# print(cookie_password, password)

if not username and not password:
    print(templates.login_page())
elif username == secret.username and password == secret.password:
    print(templates.secret_page(username, password))
else:
    print(templates.after_login_incorrect())
