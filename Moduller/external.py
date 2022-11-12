from termcolor import colored

"""External = Harici"""

# sonuc = dir(termcolor)
# print(sonuc)

# sonuc = help(termcolor)
# print(sonuc)

sonuc = colored("Merhaba!", color="green", on_color="on_yellow")
print(sonuc)

sonuc = colored("Merhaba!", color="green", on_color="on_yellow", attrs=["bold"])
print(sonuc)
