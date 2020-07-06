import time
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def call_with_monitor_2(func, arg0, arg1):
    begin = time.time()
    ret = func(arg0, arg1)
    end = time.time()
    print(" {:.3f} s".format(end - begin))
    return ret
    
def call_with_monitor_1(func, arg0):
    begin = time.time()
    ret = func(arg0)
    end = time.time()
    print(" {:.3f} s".format(end - begin))
    return ret
    
def call_with_monitor_0(func):
    begin = time.time()
    ret = func()
    end = time.time()
    print(" {:.3f} s".format(end - begin))
    return ret
    
