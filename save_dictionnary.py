import pickle

def save_dic(dict_to_save , file_path):
    with open(file_path , 'wb') as file : #wraiting in binary
        pickle.dump(dict_to_save , file) # serialization of the binary file



def load_dic(file_path):
    with open(file_path , 'rb') as file :
        return pickle.load(file)


dict_to_save={1:'a', 2:'b' ,3:'c'}
file_path='test_dict.pickle'

save_dic(dict_to_save , file_path)


recouvered = load_dic(file_path)
print(recouvered)
