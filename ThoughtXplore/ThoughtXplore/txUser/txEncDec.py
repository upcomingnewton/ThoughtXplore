from pyDes import des, PAD_PKCS5, CBC

class enc_dec():
    def txDecrypt(self, value):
        td = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        value= self.safe_str(value)
        #unicode_text=value
        #value=unicode_text.encode('utf-8')
        return td.decrypt(value, padmode=PAD_PKCS5)
    
    def txEncrypt(self, value):
        td = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        
        value=self.safe_str(value)
        
        return td.encrypt(value, padmode=PAD_PKCS5)
        
        
        
        
    
    def safe_unicode(self, obj, *args):
        """ return the unicode representation of obj """
        try:
            return unicode(obj, *args)
        except UnicodeDecodeError:
            # obj is byte string
            ascii_text = str(obj).encode('string_escape')
            return unicode(ascii_text)

    def safe_str(self, obj):
        """ return the byte string representation of obj """
        try:
            return str(obj)
        except UnicodeEncodeError:
            # obj is unicode
            return unicode(obj).encode('unicode_escape')