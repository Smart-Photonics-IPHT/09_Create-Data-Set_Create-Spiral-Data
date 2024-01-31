import numpy as np
import matplotlib.pyplot as plt

# Function to generate a spiral

# Glitta was here for the git hub workshop. Checking out the branch "Glitta".
def generate_spiral(theta_max, totalpoints = 300):
    #return a * np.exp(b * t) * np.array([np.cos(t), np.sin(t)])
    t = np.linspace(0, theta_max, totalpoints)
    return t, t * np.array([np.cos(t), np.sin(t)]), -t * np.array([np.cos(t), np.sin(t)])

# # Parameters for the first spiral
# a1, b1 = 1, 0.1
# theta_max1 = 2 * np.pi  # Adjust the angle range as needed
#
# # Parameters for the second spiral
# a2, b2 = -1, 0.1
# theta_max2 = 2 * np.pi  # Adjust the angle range as needed
#
# # Generate points for the first spiral
# t1 = np.linspace(0, theta_max1, 1000)
# spiral1 = generate_spiral(t1, a1, b1, theta_max1)
#
# # Generate points for the second spiral
# t2 = np.linspace(0, theta_max2, 1000)
# spiral2 = generate_spiral(t2, a2, b2, theta_max2)

# test = [[0.478, 1.031], [0.458, 1.075], [0.435, 1.118], [0.063, 0.004]]
# print(test[0])
# theta_max = 2*np.pi
# t, spiral1, spiral2 = generate_spiral(theta_max)
# print(spiral1, spiral2)

save_dir = r'C:\Sobhi\Results\spiral\Spiral_Data_Set'
cnt = 6
#for theta_max in (2*np.pi, 3*np.pi, 4*np.pi, 5*np.pi, 6*np.pi):
#for theta_max in (6*np.pi):
theta_max = 6*np.pi
t, spiral1, spiral2 = generate_spiral(theta_max)

#print(spiral1)

#Plot the spirals
plt.figure(figsize=(16, 16))
plt.scatter(spiral2[0], spiral2[1], s=50, label='Spiral 1', color='blue')
plt.scatter(spiral1[0], spiral1[1], s=50, label='Spiral 2', color='orange')

#Set axis limits and add labels
# plt.xlim([-19, 19])
# plt.ylim([-19, 19])
plt.xlabel('X', fontsize=24)
plt.ylabel('Y', fontsize=24)
pi_symbol = '\u03c0'
#plt.title(f'Theta_max = {cnt}{pi_symbol}', fontsize=36)
plt.gca().set_aspect('equal')

# Add a legend
plt.legend(fontsize=18)
plt.show()

#dffffff
#plt.savefig(f'C:/Sobhi/Results/spiral/Plots/Spiral_theta_max={cnt}pi.png')
plt.close()
# cnt += 1
# Show the plot

combined_array1 = np.column_stack((spiral1[0].flatten(), spiral1[1].flatten()))
combined_array2 = np.column_stack((spiral2[0].flatten(), spiral2[1].flatten()))

# np.savetxt('Spiraldata.txt', np.hstack(combined_array1.flatten(), combined_array2.flatten()), delimiter='\t')

# with open(f'{save_dir}/Spiraldata_theta_max={cnt}pi.txt', 'w') as file:
#     for x in combined_array1:
#         file.write(f'1,{np.round(x[0],3)},{np.round(x[1],3)}\n')
#     for y in combined_array2:
#         file.write(f'0,{np.round(y[0], 3)},{np.round(y[1], 3)}\n')
# cnt += 1



    # print(combined_array1)


