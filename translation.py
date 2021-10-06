import csv,time,math,psutil
import os
def french():
    with open('french_dictionary.csv','r') as frenc_file:
            french_file=csv.reader(frenc_file)
            for data in french_file:
                Dict_french[data[0]]=[data[1],0]
def translate(inputFile):
    french_text=open('t8.shakespeare.translate.txt','w')
    check=Dict_french.keys()
    with open(inputFile,'r') as text_file:
        while True:
            line=text_file.readline()
            if not line:
                break
            text=''
            for words in line.split():
                word_filter=filter(str.isalpha,words)
                text_word=''.join(word_filter)
                if text_word in check:
                    Dict_french[text_word][1]+=1
                    french_word=Dict_french[text_word][0]
                    words=words.replace(text_word,french_word)
                text+=words+' '
            text=text.strip()
            french_text.write(text+'\n')
    print('Translation is completed.calculating time....')
    return True
def frequency():
    key=Dict_french.keys()
    with open('frequency.csv','w') as frequecy_file:
        fields=['English word','French word','frequency']
        writer=csv.DictWriter(frequecy_file,fieldnames=fields)
        writer.writeheader()
        for data in key:
            writer.writerow({'English word':data,'French word':Dict_french[data][0],'frequency':Dict_french[data][1]})
    return True 
if __name__ == '__main__':
    start_time=time.time()   
    inputFile='t8.shakespeare.txt' 
    Dict_french={}   
    french()
    translate(inputFile)
    frequency()
    complete_time=time.time()
    process_time=complete_time-start_time
    mins=math.floor(process_time)
    sec=round(process_time-mins,2)
    memory_used =psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
    memory=round(memory_used,2)
    with open('performance.txt','w') as performance_text:
        performance_text.write(f'Time taken:{mins}mins{sec}sec'+'\n')
        performance_text.write(f'Memory used:{memory}MB')
    print('Task completed....')



        
    

        