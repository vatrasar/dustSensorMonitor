def averageFromList(list):
    if(len(list)==0):
        return 0
    return sum(list)/len(list)


def cat_last_part_of_ip_addres(local_addres):
    index:int=1
    while local_addres[(-1)*index]!=".":
        index+=1

    return local_addres[0:(-1)*(index-1)]