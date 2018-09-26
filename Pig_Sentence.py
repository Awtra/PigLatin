#Ali Mody

#This program converts sentences to pig latin

#Initialize variables
latin = ""
sentence = ''
latin_list = []

#Prints the sentence in pig latin
while sentence != "stop":
    sentence = input("Enter a sentence to translate it to pig latin: ")
    if sentence != 'stop':
        latin_list = sentence.split(" ")
        for i in latin_list:
            latin += i[1:] + i[0] + "ay "
        print(latin)
    elif sentence == "stop":
        print("Job done.")
