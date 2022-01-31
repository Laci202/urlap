import os
if os.path.exists("fajlok/torol.txt"):
  os.remove("fajlok/torol.txt")
else:
  print("A fájl nem létezik")