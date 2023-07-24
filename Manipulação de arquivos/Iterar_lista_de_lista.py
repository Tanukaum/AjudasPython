list = [(3,6), (3,5), (2,2), (4,5), (4,1)]

def check_list():
    for item in range(len(list)):
        for subitem in range(len(list[item])):
            if subitem == 0:
                if list[item][subitem]:
                    print('Won %d games from %d' % (list[item][subitem],list[item][subitem+1]))
            

check_list()