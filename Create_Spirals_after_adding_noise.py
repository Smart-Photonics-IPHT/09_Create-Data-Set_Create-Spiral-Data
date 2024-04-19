import numpy as np
import matplotlib.pyplot as plt
#import scienceplots
import os

main_dir = r'C:\Sobhi\Results\spiral\Spiral_Data_Set\Two_Spirals'

def generate_spiral(num_points, theta_max=2, noise=0):
    theta = np.linspace(0, theta_max*np.pi, num_points)

    x = theta * np.cos(theta) + np.random.uniform(-noise, noise, num_points)
    y = theta * np.sin(theta) + np.random.uniform(-noise, noise, num_points)
    return x, y

# Number of points in each spiral
num_points = 250
pi_symbol = '\u03c0'
for theta_max in (2, 4, 5, 10, 12):
    new_folder = f'{main_dir}/theta_max={theta_max}'
    os.makedirs(new_folder)
    for max_noise in (0, 0.2, 0.4, 0.6, 0.8, 1, 1.2):
        new_sub_folder = f'{new_folder}/max_noise={max_noise}'
        os.makedirs(new_sub_folder)
        # Generate data for two spirals with noise
        x1, y1 = generate_spiral(num_points, theta_max=theta_max, noise=max_noise)
        # x2, y2 = generate_spiral(num_points, noise=0.1)
        x2, y2 = -x1, -y1
        # Plot the spirals with noise
        plt.figure(figsize=(8, 6))
        # plt.style.reload_library()
        # plt.style.use('science')
        plt.scatter(x1, y1, label='Spiral 1', color='blue')
        plt.scatter(x2, y2, label='Spiral 2', color='red')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'Theta max={theta_max}{pi_symbol} _ Max Noise = {max_noise}')

        plt.xlabel('X', fontsize=24)
        plt.ylabel('Y', fontsize=24)
        plt.gca().set_aspect('equal')

        # Add a legend
        plt.legend(fontsize=14)
        #plt.show()
        #
        #
        # #dffffff
        plt.savefig(f'{new_sub_folder}/Spiral_theta_max={theta_max}pi_max_noise={max_noise}.png')
        plt.close()
        # # cnt += 1
        # # Show the plot

        combined_array1 = np.column_stack((x1.flatten(), y1.flatten()))
        combined_array2 = np.column_stack((x2.flatten(), y2.flatten()))

        # np.savetxt('Spiraldata.txt', np.hstack(combined_array1.flatten(), combined_array2.flatten()), delimiter='\t')

        with open(f'{new_sub_folder}/Spiraldata_theta_max={theta_max}pi_max_noise={max_noise}.txt', 'w') as file:
            for x in combined_array1:
                file.write(f'1,{np.round(x[0],3)},{np.round(x[1],3)}\n')
            for y in combined_array2:
                file.write(f'0,{np.round(y[0], 3)},{np.round(y[1], 3)}\n')