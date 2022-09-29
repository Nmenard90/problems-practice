#store names and scores in a nested list 
#sort the scores
#get lowest two scores from sorted list
#match up the names with the lowest scores
#print only the lowest score names



mylist = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float( input())
        mylist.append([name,score])
        #print(mylist)
    
    newlist = []
    for i in range(len((mylist))):
        newlist.append(mylist[i][1])
    newlist = sorted( set( newlist))
    secondlowest = (newlist[1])
    #print(secondlowest)
    
    for n in sorted(mylist):
        if n[1] == secondlowest:
            print(n[0])
             
