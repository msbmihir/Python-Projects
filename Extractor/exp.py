from zipfile import ZipFile 

file_name = "RECIPE.zip"
  

with ZipFile(file_name, 'r') as zip: 
    
    zip.printdir() 
  
   
    print('Extracting all the files now...') 
    zip.extractall() 
    print('Done!') 

