cats = 3
relations = []
for cat in range(1,cats + 1):
    # print cat
    for cat2 in range(1, cats + 1):
        if cat != cat2:
            relation = [cat, cat2]
            relation.sort()
            #to check print relation
            #to check print relations
            if not relation in relations:
                # print "cat %s likes cat %s" % (cat , cat2)
                relations.append(relation)
print len(relations)
