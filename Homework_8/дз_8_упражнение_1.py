import re
def email_parse(email_address):
    parse = re.split(r'@', email_address)
    result = {}
    if len(parse) == 2 and '.' in parse[1]:
        result['username'] = parse[0]
        result['domain'] = parse[1]
        return result
    else:
        return ValueError

email = input()
print(email_parse(email))