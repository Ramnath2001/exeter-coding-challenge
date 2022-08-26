import os
import time
import csv
import psutil

meaning = {}

def translate(words):
    global meaning
    for i in range(len(words)):
        for item in meaning:
            start_index = words[i].lower().find(item)  #starting index of the found word
            check1 = False
            check2 = False
            if start_index > 0:
                check1 = words[i][start_index-1].isalpha()  #check if the letter before the starting index is an alphabet
                
            if len(words[i]) > start_index+len(item) and start_index>=0:
                check2 = words[i][start_index+len(item)].isalpha()  ##check if the letter after the starting index + len(found word) is an alphabet

            if(start_index != -1) and (not check1 and not check2):
                temp = meaning[item][0]
                meaning[item][1] += 1
                if words[i].istitle():  #to convert to appropriate casing
                    temp = temp.title()
                elif words[i].isupper():
                    temp = temp.upper()
                words[i] = words[i].replace(words[i][start_index: len(item)+start_index],temp)



def main():
    global meaning
    start = time.time()
    #creating a dictonary with the english words as key and a list as value [french word, frequency]
    with open('french_dictionary.csv', mode ='r')as file:        

        csvFile = csv.reader(file)

        for lines in csvFile:
              if lines[0] not in meaning:
                  meaning[lines[0]] = [lines[1], 0]

    #read the input test file line by line
    translated_text = ""        #variable to hold the translated text
    with open('t8.shakespeare.txt') as f:          #t8.shakespeare
        lines = f.readlines()
        for line in lines:
            words = line.split()
            if len(words) != 0:
                translate(words)
            text = " ".join(words)
            translated_text += text+"\n"
  
    #create a new file to write the translated text
    text_file = open("t8.shakespeare.translated.txt", "w")
    
    #write string to file
    text_file.write(translated_text)
    
    #close file
    text_file.close()

    #create a csv file to store the frequency of occurrence of the english word along with the french word (freq > 0)
    fields = ['English Word', 'French Word', 'Frequency']
    with open('frequency.csv', 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 

        # writing the fields 
        csvwriter.writerow(fields) 

        for i in meaning:
            if meaning[i][1] > 0:
                csvwriter.writerow([i, meaning[i][0], meaning[i][1]])

    end = time.time() 
    print(f"Time to process: {end-start} Seconds")
    print(f"Memory used: {psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2} MB")

if __name__ == "__main__":
    main()