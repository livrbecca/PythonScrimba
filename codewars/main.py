def solution(a, b):
    if len(a) < len(b):
        print(a+b+a)
    else:
        print(b+a+b)


solution("1", "22")


def name_shuffler(str_):
    name = str_.split(" ")
    print(name[1], name[0])


name_shuffler("Olivia Walker")



def between(a,b):
    
    current_int = a
    results = []
    
    while current_int <= b:
        results.append(current_int)
        current_int = current_int + 1 # 2
        
        
    return results 
    


    def unusual_five():
        return len("apple")


def name_shuffler(str_):
    name = str_.split(" ")
    return f"{name[1]} {name[0]}"