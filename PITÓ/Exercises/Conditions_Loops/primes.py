start = 1
end = 50 + 1
for num in range(start,end):
    if num > 1:
        for i in range(2,num):
            if(num%i) == 0:
                break
        else:
            print(num)  #So you can put the else outside of the for hmm
