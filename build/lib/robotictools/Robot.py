import numpy as np
import math
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

import PySimpleGUI as sg

import threading
import sys
import queue
import time

class Robot():
    def __init__(self,joint_num,Link_list):
        self.joint_num = joint_num
        self.Link_list = Link_list
        self.T         = np.eye(4)
        self.q         = queue.Queue()
    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for Link in self.Link_list:
            past_point = [self.T[0][3],self.T[1][3],self.T[2][3]]
            Link.Transform_Matrix()
            self.T = self.T.dot(Link.T)

            origin_point = [self.T[0][3],self.T[1][3],self.T[2][3]]
            x_axis       = [Link.T[0][0],Link.T[0][1],Link.T[0][2]]
            y_axis       = [Link.T[1][0],Link.T[1][1],Link.T[1][2]]
            z_axis       = [Link.T[2][0],Link.T[2][1],Link.T[2][2]]

            ax.plot3D([origin_point[0],origin_point[0]+z_axis[0]],[origin_point[1],origin_point[1]+z_axis[1]],[origin_point[2],origin_point[2]+z_axis[2]],'blue')

            ax.plot3D([past_point[0],origin_point[0]],[past_point[1],origin_point[1]],[past_point[2],origin_point[2]],'black')
        plt.xlim([-10,10])
        plt.ylim([-10,10])
        plt.show()

    def teach(self):
        def slidebutton():
            layout = [[sg.Text('Robot Joint Position',auto_size_text=True)]]
            for Link in self.Link_list:
                layout.append([sg.Slider(range=(float(Link.limit[0]),float(Link.limit[1])),default_value = 200,orientation ='h')])
            layout.append([sg.OK('确认',auto_size_button=True)])
            window = sg.Window('Robot Joint Position', layout,location=(800, 400))
            try:
                while 1:
                    event, values = window.read()
                    print(values)
                    self.q.put(values)

                    if event == sg.WIN_CLOSED:
                        sys.exit(1)
            except:
                sys.exit(1)

        def teach_plot():
            while 1:
                if not self.q.empty():
                    joint_value = self.q.get()
                    for i in range(self.joint_num):
                        self.Link_list[i].theta = joint_value[i]
                    self.plot()

        button_th = threading.Thread(target=slidebutton)
        button_th.start()
        time.sleep(1)
        plot_th   = threading.Thread(target=teach_plot)
        plot_th.start()
