from HadithObj import HadithObj

h = HadithObj(""," ","Book")
print(h.isValid() is not True)

test = "Whats Up"
test2 = "WhatsUp"

num = 0
for char in test:
    num += 1
print(num)
num = 0
for char in test2:
    num += 1
print(num)
