import os #search directory and manage file path
from zipfile import ZipFile



def zip_all( search_dir , extension_list , output_path ):
    with ZipFile(output_path ,'w') as output_zip:
        for root,dir,files in os.walk(search_dir):
            rel_path=os.path.relpath(root,search_dir)#relative path
            for file in files :
                name,ext=os.path.splitext(file)#seperate file name fromp extension
                if ext.lower() in extension_list:
                    output_zip.write(os.path.join(root,file),
                                    arcname=os.path.join(rel_path,file))#(path to original file,ho the file  will be named)

zip_all('C:\\Users\\AMOSA\\Desktop\\hi',['.jpg'] ,'mystaff.zip ')
#search_dir: directory to file  like in the exemple , extension_list .txt .jpg .png .ave ... , output_path : name of thefile.zip/.rar...
