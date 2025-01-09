import re

def is_valid_string(s):
    if len(s) < 6:
        return False
    
    pattern = r"^(?=(.*\d.*\d)(?!.*\d.*\d.*\d))(?=.*\D.*\d)(?!.*\d\d).+$"
    
    return bool(re.match(pattern, s))

print(is_valid_string("a1"))  
print(is_valid_string("123abc")) 
print(is_valid_string("abc123"))
print(is_valid_string("a1b2c")) 