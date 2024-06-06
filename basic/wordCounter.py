sentence = input("Writte a sentence: ")
sentence = sentence.strip()
counter = 0
position = 0
position = sentence.find(" ", position)
if sentence == "":
    counter = 0
else: 
    counter += 1
    while position != -1:
        counter += 1
        while sentence[position + 1] == " ":
            position += 1
        position = sentence.find(" ", position +1)

print("Number of words:", counter)