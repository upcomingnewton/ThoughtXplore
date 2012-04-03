
import re

class EmailValidate():
    
    def validate(self, email):

        if len(self.email) > 7:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.email) != None:
                return 1
        return 0