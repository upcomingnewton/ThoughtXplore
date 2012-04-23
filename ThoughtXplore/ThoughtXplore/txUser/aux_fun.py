#user has logged in sucessfully
#1. determmine it's group 
#2. check if menu is available for this group in cache or not 

#5. make the menu system for this user
#7. redirect the user to dashboard page
from django.core.cache import cache
import ThoughtXplore.CONFIG as CONFIG
from DatabaseFunctions import GetActiveMenusByGroupid

def MakeGroupMenu(groupid):
    groupkey = CONFIG.GROUP_MENU_PREFIX + str(groupid)
    print groupkey
    if cache.get(groupkey) is None:
        to_cache = MakeGroupMenuCache(groupid)
        cache.set(groupkey,to_cache)
        
def ResetGroupMenu(groupid):
    groupkey = CONFIG.GROUP_MENU_PREFIX + str(groupid)
    to_cache = MakeGroupMenuCache(groupid)
    cache.set(groupkey,to_cache)
        
def ClearGroupMenuCache(groupid):
    groupkey = CONFIG.GROUP_MENU_PREFIX + str(groupid)
    if cache.get(groupkey) is not None:
        cache.delete(groupkey)
        
def MakeGroupMenuCache(groupid):
    #groupkey = CONFIG.GROUP_MENU_PREFIX + str(groupid)
    ClearGroupMenuCache(groupid)
    final_result = []
    temp = []
    #3. fetch menu from database
    menus = GetActiveMenusByGroupid(groupid)
    for menu in menus:
        temp = []
        if menu[4] == -1:
            # add this to our temporary list as first object
            temp.append(menu)
            #traverse through the list and find all children
            for x in menus:
                if x[4] == menu[0]:
                    temp.append(x)
        final_result.append(temp)
    print final_result
    return final_result
    # arrange menu's in 2 lists
    # 
    #4. set the cache