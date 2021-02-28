# from robotictools.Robot import *
import robotictools as rct
import numpy as np
from math import *
if __name__=="__main__":
    Link1 = rct.Link(alpha=0,a=0,d=0,theta=0,limit=[0,180])
    Link2 = rct.Link(0,5,0,pi/6)
    Link3 = rct.Link(0,5,0,0)

    Robot = rct.Robot(3,[Link1,Link2,Link3])
    Robot.teach()