cats = 0
while not cats:
    try:
        cats = int(raw_input("Please enter number of cats in herd: "))
    except ValueError:
        print "Hey, I've told you to enter number of cats!"

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
print "There are %s relations between your cats" % (len(relations))
