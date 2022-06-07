def main():
    
    expensive = 0
    cheap = 0
    dead = 0
    alive = 0
    expensivepain = 0
    cheapdeath = 0
    firstclass = 0
    secondclass = 0
    thirdclass = 0
    file_in = open("C:\\Users\\lchandra25\\Desktop\\Titanic.csv")
    frist_name = input("Do you want to begin?:")
    
    file_in.seek(1)
    
    line_counter = 1
    
    for line in file_in: #read a line or copy of csv
    
        if line_counter == 1:
            line_counter = -99
            continue
        list_of_words = line.split(",")
        
        #print("DEBUG: 24: " , list_of_words[1])
        
        if list_of_words[1] == "1":
            #print("They died")
            dead = dead+1
            #print("dead is: ", int(dead))
        if list_of_words[1] == "0":
            #print("They survived")
            alive = alive+1
            #print("alive: ", int(alive))
        #print(list_of_words)
        #print(line)
        
        
        fare = float(list_of_words[10])
        death = list_of_words[1]
        
        if fare < 60 and death == "1":
            #print("and they had a cheap ticket")
            cheapdeath = cheapdeath+1
        if fare > 60 and death == "1":
            #print("and they had a expensive ticket")
            expensivepain = expensivepain+1
        
        
        
        
        
        classy = float(list_of_words[2])
        if classy == 1:
            firstclass = firstclass+1   
        if classy == 2:          
            secondclass = secondclass+1
        if classy == 3:
            thirdclass = thirdclass+1 
    
    
    classm = input("Which class # would you like to see? (1-3)")        
    File = open("C:\\Users\\lchandra25\\Desktop\\Titanic.csv","a")
    choice = input("Would you like to add your name?(Yes/No)")
    if choice == "No":
        pass    
    elif choice == "Yes":
        x=input("What is your name and other info please put commas to go to next collum?")
        File.write("\n"+x)
    File.close()
    if cheapdeath > expensivepain:
        print("More people died with cheap tickets. Should've bought better tickets")
    if expensivepain > cheapdeath:
        print("More people died with expensive tickets. Money didn't save them")
    print('alive: ', str(alive))
    print('dead: ', str(dead))
    print('expensive pain: ', str(expensivepain))
    print('cheap death: ', str(cheapdeath))
    if classm == "1":
        print('in first class: ', str(firstclass))   
    if classm == "2":
        print('in second class: ', str(secondclass)) 
    if classm == "3":
        print('in third class: ', str(thirdclass))  
    file_in.close()
if __name__ == '__main__':
    main()