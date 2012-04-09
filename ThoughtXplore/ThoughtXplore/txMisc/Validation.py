
import re

class EmailValidate():
    
    def __init__(self,email):
        self.email = email
        
    def validate(self):

        if len(self.email) > 7:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.email) != None:
                return 1
        return 0
    
class StringValidate():
    
    def validate_alphastring(self,st):
        if(st.isalpha()):
            return 1
        return 0
    def validate_alphanumstring(self,st):
        if(st.isalnum()):
            return 1
        return 0
    def validate_numeric(self,st):
        if(st.isdigit()):
            return 1
        return 0
    