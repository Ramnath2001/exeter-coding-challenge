#importing necessary headers
import os
import time
import csv
import re
import psutil

def main():
    l = {}  #storing the english words as key and a list containing the french word and the freq of english word as value

    with open('french_dictionary.csv', mode ='r')as file:        

            csvFile = csv.reader(file)

            for lines in csvFile:
                  if lines[0] not in l:
                      l[lines[0]] = [lines[1], 0]       #adding all items to dictionary

    with open('t8.shakespeare.txt') as f:     #t8.shakespeare
        contents = f.read()
        wordList = []
        # print(re.split(r'(\W+)', contents))
        for p in re.split(r'(\W+)', contents):
            if p.lower() in l:
                l[p.lower()][1] += 1
                if p.isupper():
                    wordList.append(l[p.lower()][0].upper())
                elif p.istitle():
                    wordList.append(l[p.lower()][0].title())
                else: 
                    wordList.append(l[p.lower()][0].lower())
            else:
                wordList.append(p)
        translatedTxt = ''.join(wordList)
        text_file = open("t8.shakespeare.translated.txt", "w") #creating a new file to store the translated text

        #write string to file
        text_file.write(translatedTxt)

        #close file
        text_file.close()

    fields = ['English Word', 'French Word', 'Frequency']
    with open('frequency.csv', 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        # writing the fields 
        csvwriter.writerow(fields) 
        for i in l:
            if l[i][1] > 0:
                csvwriter.writerow([i, l[i][0], l[i][1]])
    
if __name__ == '__main__':
    start = time.time()  
    main()
    end = time.time()
    print(f"Time to process: {end-start} Seconds")  #time taken to process
    print(f"Memory used: {psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2} MB")  #memory used by the program
