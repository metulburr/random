
import sys
import traceback

try:
    1/0
except:
    s = sys.exc_info()
    
    exc_type, exc_value, exc_traceback = sys.exc_info()
    t = traceback.format_exception(exc_type, exc_value, exc_traceback)
    t2 = traceback.format_exc()
    

print('basic: {}\n\n'.format(s)) # show basic
print('line number: {}\n\n'.format(t)) #show line number 
print('exception as string: {}\n\n'.format(t2))
