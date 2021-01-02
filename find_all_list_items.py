def index_all(search_list , item):
    indices =list()
    for i in range( len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i],list):
            for index in index_all(search_list[i],item):
                indices.append([i]+index)
    
    return indices
exmple = [[1,2,3],2,[1,3],[2,3,1]]
a=index_all(exmple  ,2)
print (a)
        
