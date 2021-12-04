from lib.calculateFK import FK
from core.interfaces import ArmController

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style
import random
import numpy as np

fk = FK()

# the dictionary below contains the data returned by calling arm.joint_limits()
limits = [
    {'lower': -2.8973, 'upper': 2.8973},
    {'lower': -1.7628, 'upper': 1.7628},
    {'lower': -2.8973, 'upper': 2.8973},
    {'lower': -3.0718, 'upper': -0.0698},
    {'lower': -2.8973, 'upper': 2.8973},
    {'lower': -0.0175, 'upper': 3.7525},
    {'lower': -2.8973, 'upper': 2.8973}
 ]

# TODO: create plot(s) which visualize the reachable workspace of the Panda arm,
# accounting for the joint limits.
#
# We've included some very basic plotting commands below, but you can find
# more functionality at https://matplotlib.org/stable/index.html
style.use('ggplot')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

fk = FK()

x = []
y = []
z = []

for i in range(100000):

    q_lst = []

    for j in range(7):

        joint_angle = limits[j]['lower'] + random.uniform(0,1) * (limits[j]['upper'] - limits[j]['lower'])

        q_lst.append(joint_angle)

    q = np.array(q_lst)

    joint_positions, T0e = fk.forward(q)

    x.append(T0e[0][3])
    y.append(T0e[1][3])
    z.append(T0e[2][3])

# TODO: update this with real results
#ax.scatter(1,1,1) # plot the point (1,1,1)

ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()
