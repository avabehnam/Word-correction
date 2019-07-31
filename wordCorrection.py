def single_insert_or_delete(x,y):
    counter=0
    dif=len(x)-len(y)
    i=0
    j=0
    if dif==-1 :
        while (i < len(x) and counter<2):
            if x[i]==y[j]:
                i=i+1
                j=j+1
            else :
                counter=counter+1
                
                j=j+1
    elif dif==1 :
        while (i < len(y) and counter<2):
            if x[i]==y[j]:
                i=i+1
                j=j+1
            else :
                counter=counter+1
                i=i+1
    return counter




def dis_similarity(s1, s2):
    counter = 0
    for i in range(len(s1)):
        if s1[i].lower() != s2[i].lower():
            counter+=1

    return counter










def spelling_corrector(string,my_list):
    string_list=[]
    word_list=[]
    string_list=string.split(' ')
    word_list=my_list.split(',')
    printWords=[]

    for stringIndex in range(0,len(string_list)):
        printWords.append('')
        if len(string_list[stringIndex])<=2:
                printWords[stringIndex] = string_list[stringIndex]
                continue
        else: 
            wordIndex=0
            while wordIndex<=len(word_list)-1:
                if string_list[stringIndex]==word_list[wordIndex]:
                    printWords[stringIndex] = string_list[stringIndex]
                    break 
                else:
                    wordIndex+=1
                    
        #index=stringIndex
        if printWords[stringIndex]=='':
                wordIndex=0
                diff=len(string_list[stringIndex]);
                while wordIndex<=len(word_list)-1:

                    if abs(len(string_list[stringIndex])-len(word_list[wordIndex]))==1:
                        diff = single_insert_or_delete(string_list[stringIndex],word_list[wordIndex])
                        if diff<2:
                            printWords[stringIndex] = word_list[wordIndex]
                            break      
                    wordIndex+=1
                
                if printWords[stringIndex]=='':  
                    wordIndex = 0  
                    while wordIndex<=len(word_list)-1:
                        if len(string_list[stringIndex])==len(word_list[wordIndex]):
                            diff = dis_similarity(string_list[stringIndex],word_list[wordIndex])
                            if diff<2:
                                printWords[stringIndex] = word_list[wordIndex]
                                break
                        wordIndex+=1
                if printWords[stringIndex]=='':  
                    printWords[stringIndex] = string_list[stringIndex]
            
    for i in printWords:
        print(i + ' ' , end='')



spelling_corrector("","")