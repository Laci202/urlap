f = open("fajlok/demofile2.txt", "a")
f.write("Új tartalom!")
f.close()

#open and read the file after the appending:
f = open("fajlok/demofile2.txt", "r")
print(f.read())
