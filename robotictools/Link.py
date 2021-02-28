import numpy as np
from math import *
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

class Link():
    def __init__(self,alpha,a,d,theta,limit = [-180,180],offset = 0):
        # D-H Param
        self.alpha = alpha
        self.a     = a
        self.d     = d
        self.theta = theta
        self.limit = limit

    def Transform_Matrix(self):
        self.T  = np.array([[np.cos(self.theta),                    -np.sin(self.theta),                   0,                   self.a],
                            [np.sin(self.theta)*np.cos(self.alpha), np.cos(self.theta)*np.cos(self.alpha), -np.sin(self.alpha), -np.sin(self.alpha)*self.d],
                            [np.sin(self.theta)*np.sin(self.alpha), np.cos(self.theta)*np.sin(self.alpha), np.cos(self.alpha),  np.cos(self.alpha)*self.d],
                            [0,                                     0,                                     0,                   1]])

    def Euler_Angles(self,pose_matrix):
        sy = math.sqrt(pose_matrix[0][0]**2+pose_matrix[1][0]**2)
        singular = sy<1e-6
        if(not singular):
            x = math.atan2(pose_matrix[2][1], pose_matrix[2][2])
            y = math.atan2(-pose_matrix[2][0], sy)
            z = math.atan2(pose_matrix[1][0], pose_matrix[0][0])
        else:
            x = math.atan2(-pose_matrix[1][2], pose_matrix[1][1])
            y = math.atan2(-pose_matrix[2][0], sy)
            z = 0

        return [x,y,z]