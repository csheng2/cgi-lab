#!/usr/bin/env python3

import os
import json
from textwrap import indent
import sys

#PRINT OUT ALL ENV VARIABLES AS PLAIN TEXT
# print("Content-Type: text/plain") #let browser know to expect plain text
# print()
# print(os.environ)

#PRINT ENV VARIABLES AS JSON
print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent=2))

#PRINT QUERY PARAMETER DATA IN HTML
# print("Content-Type: text/html")
# print()
# print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

# posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
# print(f"<p>QUERY_STRING={posted_bytes}</p>")
# if posted_bytes:
#     posted = sys.stdin.read(int(posted_bytes))
#     print(f"<p> POSTED: <pre>")
#     for line in posted.splitlines():
#         print(line)
#     print("</pre></p>")