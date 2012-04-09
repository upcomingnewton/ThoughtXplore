from ThoughtXplore.txMisc.DBMessages import db_messages


def decode(result,rescode):
    if result == 1:
            return 'Success, An email has been sent to registration email adress. Please follow the instructions in the email for verification. In case, there is no email, please check spam folder and add "verification@uiet.thoughtexplore.com" as a valid email adress.in case of no-email, feel free to contact system administrators'
    elif result == 2:
            return 'User already exists'
    else: 
        return db_messages[str(rescode)]
    
# insert function messages
db_messages.update({'601':'User registration failed. Please try again later, if problem persists, contact system administrator.',
               '602':'User registration failed. Error adding user to group. Please try again later, if problem persists, contact system administrator.',
               '603':'User registration failed. Error adding entry to logs.Please try again later, if problem persists, contact system administrator.',
               })