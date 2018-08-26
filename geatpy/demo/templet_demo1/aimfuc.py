# -*- coding: utf-8 -*-
"""
函数接口示例

Created on Sun Jul 29 14:42:13 2018

@author: jazzbin
"""

import numpy as np

def aimfuc(Phen):
    x1 = Phen[:, 0]
    x2 = Phen[:, 1]
    ObjV = x1*x1 + x2*x2
    return np.array([ObjV]).T
    
    