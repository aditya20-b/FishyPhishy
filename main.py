from checks.regex import RegexCheck

regex = RegexCheck()

url = input("Enter a URL: ")

print("This is a scam link" if regex.check_url(url) else "This link is probably safe")
