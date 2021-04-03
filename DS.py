import time
import random
import hashlib
import math

def generate_random_str(randomlength=16):
  """
  生成一个指定长度的随机字符串
  """
  random_str = ''
  base_str = 'abcdefghigklmnopqrstuvwxyz0123456789'
  length = len(base_str) - 1
  for i in range(randomlength):
    random_str += base_str[random.randint(0, length)]
  return random_str

def AManager_k2():
    """2.6.0 算法更新 2021-04-03"""
    arrayList = []
    iArr = [168, 162, -106, -108, -106, -4782969, -114, 210, 186, -118, -98, -106, -14348907, -177147, 192, -6561, -4782969, -59049, -177147, 192, -116, 156, -112, -14348907, -122, 156, -100, -110, -116, 198, -100, -729]
    for i2 in iArr:
        if(i2<0):
            d2 = float(6)
            i = math.log(-float(i2))/math.log(3) - d2 + 48 if(-float(i2) >= pow(3, d2)) else ~int(i2)
        else:
            i = (i2 / 3) + 48
        arrayList.append(int(i))
    strs = str(bytes(arrayList), encoding="utf-8")
    return strs


def getds():
    """
    获取DS参数 2020-12-10 V2.3.0
    """
    salt = AManager_k2()
    r = generate_random_str(6)
    t = round(time.time())
    objhash = hashlib.md5()
    objhash.update("salt={}&t={}&r={}".format(salt, t, r).encode("utf-8"))
    o = objhash.hexdigest()
    objhash.update(str(t).encode("utf-8"))
    ret = "{},{},{}".format(str(t), r, o)
    return ret
