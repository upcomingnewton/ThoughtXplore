
from ThoughtXplore.txDatabaseHelper import DBhelper

def DBInsertFolder(folderdetails):
    
    if( folderdetails['cuser'] == 'system'):
        folderdetails['cuser']==''
    
    query = "SELECT txFileSystem_insert_folder('" + folderdetails['cuser'] + "','" + folderdetails['name'] + "','" + folderdetails['desc'] + "','" + folderdetails['folder_type']  +"'); "
    return DBhelper.CallFunction(query)
    
def DBRetrieveFolders():
    
    query= "SELECT * from 'txFileSystem_folder_basics'"
    return DBhelper.CallFunction(query)

def DBInsertFile(file_details):
    
    query = "SELECT txFileSystem_files_basics('" + file_details['name'] + "','" + file_details['desc'] + "','" + file_details['url'] + "','" + file_details['folder_id']+ "','" + file_details['size']+ "','" + file_details['file_type_id']+ "','" + file_details['user_created_id']  +"'); "
    return DBhelper.CallFunction(query)   

    
