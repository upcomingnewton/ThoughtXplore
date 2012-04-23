from ThoughtXplore.txMisc.DBMessages import db_messages


def decode(result,rescode,fun):
    if result == 1:
        if fun == 'InsertUserFromSite':
            return 'Success, An email has been sent to registration email adress. Please follow the instructions in the email for verification. In case, there is no email, please check spam folder and add "verification@uiet.thoughtexplore.com" as a valid email adress.in case of no-email, feel free to contact system administrators'
        elif fun == 'AuthenticateUserFromSite':
            return 'Success, User account has been sucessfully verified. You can login now. Please note that you need to complete your profile, which will be verified by your coordinators. After that you will be able to access full functionality'
    elif result == 2:
            return 'User already exists. An email has been sent to registration email adress. Please follow the instructions in the email for verification. In case, there is no email, please check spam folder and add "verification@uiet.thoughtexplore.com" as a valid email adress.in case of no-email, feel free to contact system administrators'
    else: 
        return db_messages[str(rescode)]
    
# insert function messages
db_messages.update({'601':'User registration failed. Please try again later, if problem persists, contact system administrator.',
               '602':'User registration failed. Error adding user to group. Please try again later, if problem persists, contact system administrator.',
               '603':'User registration failed. Error adding entry to logs.Please try again later, if problem persists, contact system administrator.',
               })