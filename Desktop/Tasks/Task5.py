import re

emails = [
    "user@example.com",
     "invalid.email",
    "test_123@domain.co.uk",
    "@nodomain.com"
]

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

for email in emails:
    if re.match(pattern, email):
       print(email, " Is Valid")
    else:
       print(email, " Is Invalid")