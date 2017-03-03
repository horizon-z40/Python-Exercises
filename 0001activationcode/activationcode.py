#!/usr /bin/env python
# -*- coding: utf-8 -*-
"""
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
Note:string.ascii_letters+string.digits生成一个数组，在这里面选择
"""
import random
import string

#List，每次组随机在这里面取一个数
x=string.ascii_letters+string.digits

def generate(num,length):
  def func(n=length):
    code=''
    for i in xrange(length):
      code+=random.choice(x)
    return code
  
  codes=[func() for i in xrange(num)]
  return codes
  
if __name__=='__main__':
  codes=generate(200,12)
  
  
