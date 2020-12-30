import operator
d = {1:2,3:4,4:3,2:1,0:0}
sorted_d = sorted(d.items(), key = operator.itemgetter(1))
sorted_d = dict(sorted(d.items(), key = operator.itemgetter(1),reverse=True)) #idk mate