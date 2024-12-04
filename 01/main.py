""" Insert Name """
# Izveidoja mainīgo name, kurā ievada savu vārdu
name = input("Whats your name: ")

""" Insert age. Also convert age into an Integer value """
# Izveidoja mainīgo age, kurā ievada savu vecumu. Mainīgo arī pārvērta par int vērtību.
age = int(input("How old are you: "))

""" Do the math """
# Izveidoja mainīgo year, kura vērtība ir tagadējais gads mīnus age mainīgais plus 100
year = str((2018 - age)+100)

""" Print the result """
# Izprintē name mainīgo ar tekstu, kas saka cik vecs tu būsi pēc 100 gadiem, un tad vēl pieliek klāt year mainīgo
print(name + " will be 100 years old in the year " + year)
