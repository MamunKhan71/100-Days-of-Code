import pyshorteners
print("....................................................")
url = input("Enter Your URL : ")
print("....................................................")
shorts = pyshorteners.Shortener()
a = shorts.tinyurl.short(url)
print("Shortened URL : " + a)
print("....................................................")
