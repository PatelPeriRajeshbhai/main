def text_file(filename):
  with open(filename,"r") as file:
        text = file.read()

  lines = text.split("\n")
  words = text.split()
  characters = len(text)
  longest_word = max(words, key=len)
    
  print("Total Lines:", len(lines))
  print("Total Words:", len(words))
  print("Total Characters:",characters)
  print("Longest Word:", longest_word)
   

text_file("file19.txt")        