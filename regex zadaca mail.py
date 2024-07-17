import re

email_pattern = "^[a-z]+\.[a-z]+@fpmoz\.sum\.ba$"
eduid_pattern = "^[a-z][a-z]+[0-9]*@sum\.ba$"

while True:
    email = input("unesi email")
    if re.match(email_pattern, email):
        print("email je ispravan.")
        break
    else:
        print("neispravan format emaila. Pokušajte ponovo.")


while True:
    eduid = input("unesi eduID")
    if re.match(eduid_pattern, eduid):
        print("eduID je ispravan.")
        break
    else:
        print("neispravan format eduID-a. Pokušajte ponovo.")

