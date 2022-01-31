f = open("fajlok/demofile3.txt", "w")
f.write("Új tartalom3!")
f.close()

#open and read the file after the appending:
f = open("fajlok/demofile3.txt", "r")
print(f.read())
