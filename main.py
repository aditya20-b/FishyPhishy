from back.checks import RegexCheck, JaroWinkler, Levenshtein

import urllib.parse

regex = RegexCheck()
jaro_wink = JaroWinkler()

url_fake = input("Enter fake URL: ")
url_real = input("Enter real URL: ")

parsed_url1 = urllib.parse.urlparse(url_fake)
parsed_url2 = urllib.parse.urlparse(url_real)

url_fake = parsed_url1.netloc + parsed_url1.path
url_real = parsed_url2.netloc + parsed_url2.path

print("Real URL:", url_real)
print("Fake URL:", url_fake)

print("Regex Test says:", regex.check_url(url_fake))
print("Jaro Winkler:", jaro_wink.jaro_winkler(url_fake, url_real))
print("Levenshtein:", Levenshtein().levenshtein_distance(url_fake, url_real))
