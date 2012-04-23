from ThoughtXplore.txMisc.DBMessages import db_messages


def decode(result,rescode,fun):
    if result == 1:
        if fun == 'CreateMenuFromSite':
            return 'Success, Menu was created sucessfully'
        elif fun == 'UpdateMenuFromSite':
            return 'Success, Menu updated'
        elif fun == 'UpdateMultipleMenuFromSite':
            return 'Success, Menu\'s updated'
    elif result == 2:
            return 'Error, menu already exists'
    else: 
        return db_messages[str(rescode)]
    
# insert function messages
db_messages.update({'601':'User registration failed. Please try again later, if problem persists, contact system administrator.',
               '602':'User registration failed. Error adding user to group. Please try again later, if problem persists, contact system administrator.',
               '603':'User registration failed. Error adding entry to logs.Please try again later, if problem persists, contact system administrator.',
               })