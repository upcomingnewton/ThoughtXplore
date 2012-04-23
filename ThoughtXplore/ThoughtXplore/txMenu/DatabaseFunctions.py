from ThoughtXplore.txDatabaseHelper import DBhelper
from ThoughtXplore.txMisc.MiscFunctions import WriteOutput

def DBUpdateMenu(details):
    query = "SELECT * FROM txMenu_menu_edit(" + str(details['mid']) + ",'" + details['name'] + "','" + details['desc'] + "','" + details['murl'] + "'," + str(details['pid']) + ",'" + details['micon'] + "','" + details['maction'] + "','" + details['logsdesc'] + "','" + details['prev'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
    WriteOutput( query )
    result = DBhelper.CallFunction(query)
    #WriteOutput( result )
    print result
    return result[0]


def DBUpdateMultiple(details):
    query = "SELECT * FROM txMenu_menu_statechange('" + details['csv_mid'] + "'," + str(details['mpid']) + ",'" + details['permission'] + "','" + details['logsdesc'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
    WriteOutput( query )
    result = DBhelper.CallFunction(query)
    #WriteOutput( result )
    print result
    return result[0]



def DBInertMenu(details):
    query = "SELECT * FROM txMenu_menu_insert('" + details['name'] + "','" + details['desc'] + "','" + details['murl'] + "'," + str(details['pid']) + ",'" + details['micon'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"    
    WriteOutput( query )
    result = DBhelper.CallFunction(query)
    #WriteOutput( result )
    print result
    return result[0]