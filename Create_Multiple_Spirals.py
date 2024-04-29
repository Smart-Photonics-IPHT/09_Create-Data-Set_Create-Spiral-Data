import numpy as np
import matplotlib.pyplot as plt
import os




author = ""
task = ""
description = ""
parameters = ""
# Create main folder and sub folders and generate the readme file inside it
#

def generate_multiple_spirals(theta_max, totalpoints=300, sprials_number=4, max_noise=0):
    #return a * np.exp(b * t) * np.array([np.cos(t), np.sin(t)])
    step = theta_max*np.pi/totalpoints
    t = np.linspace(step, theta_max*np.pi, totalpoints)
    Sprials = []
    for i in range(0, sprials_number):
        Sprials.append(t * np.array([np.cos(t + i*2*np.pi/(sprials_number)), np.sin(t + i*2*np.pi/(sprials_number))])
                       + np.random.uniform(-max_noise, max_noise, totalpoints))
    return t, Sprials[:sprials_number]

Create_date = '040324'
Create_date = 'Template'
Create_date = '260324'
Create_date = '100424'
Create_date = 'Template'
Create_date = '0.5piTemplate'
Create_date = '150424'

main_dir = r'C:\Sobhi\DataSet\Spiral_Data_Set\4_Spirals'
main_dir = f'{main_dir}/{Create_date}'
#for theta_max in (2*np.pi, 3*np.pi, 4*np.pi, 5*np.pi, 6*np.pi):
#for theta_max in (6*np.pi):
theta_max = 0.1 # 10pi
#theta_max = 1
#t, spiral1, spiral2 = generate_spiral(theta_max)

#for theta_max in (2, 4, 6, 8, 10, 12):
# for denom in (0.01, 0.02, 0.05, 0.1, 0.5):
#for denom in (2, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1):
#for denom in (0.5, 1, 2, 4, 8, 16, 32):
#for denom in (0.5, 1, 2, 4, 8, 16, 32):
denom = 2
denom_folder = f'{main_dir}/phase_factor_denom={denom}'
if not os.path.exists(denom_folder):
    os.makedirs(denom_folder)
#new_folder = f'{main_dir}/theta_max={theta_max}'
theta_folder = f'{denom_folder}/theta_max={theta_max}'
theta_folder = f'{main_dir}/theta_max={theta_max}'
if not os.path.exists(theta_folder):
    os.makedirs(theta_folder)
#for max_noise in (0, 0.1, 0.2, 0.4, 0.6, 0.8, 1, 1.2):
for max_noise in (0, 0.1, 0.2):
#for max_noise in (0, 1):
    max_noise_folder = f'{theta_folder}/max_noise={max_noise}'
    if not os.path.exists(max_noise_folder):
        os.makedirs(max_noise_folder)
    t, [spiral1, spiral2, spiral3, spiral4] = generate_multiple_spirals(theta_max, max_noise=max_noise)

    plt.figure(figsize=(16, 16))
    plt.scatter(spiral1[0], spiral1[1], s=50, label='Spiral 1', color='blue')
    plt.scatter(spiral2[0], spiral2[1], s=50, label='Spiral 2', color='green')
    plt.scatter(spiral3[0], spiral3[1], s=50, label='Spiral 3', color='red')
    plt.scatter(spiral4[0], spiral4[1], s=50, label='Spiral 4', color='black')

    #this was used to show two points only that we know they were correctly classified
    # plt.scatter(spiral1[0], spiral1[1], s=50,  color='blue', alpha=0.2)
    # plt.scatter(spiral2[0], spiral2[1], s=50,  color='green', alpha=0.2)
    # plt.scatter(spiral3[0], spiral3[1], s=50,  color='red', alpha=0.2)
    # plt.scatter(spiral4[0], spiral4[1], s=50,  color='black', alpha=0.2)
    #
    # plt.scatter(-9.3, -28.022, s=50, label='Point from Spiral 1', color='blue')
    # plt.scatter(-9.642, -29.568, s=50, label='Point from Spiral 4', color='black')

    #Set axis limits and add labels
    # plt.xlim([-19, 19])
    # plt.ylim([-19, 19])
    plt.xlabel('X', fontsize=24)
    plt.ylabel('Y', fontsize=24)
    pi_symbol = '\u03c0'
    plt.title(f'Theta_max ={theta_max}{pi_symbol} _ Max_noise={max_noise}', fontsize=24)
    plt.gca().set_aspect('equal')

    # Add a legend
    plt.legend(fontsize=14, loc='upper left')
    #plt.show()
    plt.savefig(f'{max_noise_folder}/Multiple_Spirals_theta_max={theta_max}pi_max_noise={max_noise}.png')
    #plt.savefig(f'{max_noise_folder}/two_points_Multiple_Spirals_theta_max={theta_max}pi_max_noise={max_noise}.png')
    plt.close()
    # cnt += 1
    # Show the plot

    combined_array1 = np.column_stack((spiral1[0].flatten(), spiral1[1].flatten()))
    combined_array2 = np.column_stack((spiral2[0].flatten(), spiral2[1].flatten()))
    combined_array3 = np.column_stack((spiral3[0].flatten(), spiral3[1].flatten()))
    combined_array4 = np.column_stack((spiral4[0].flatten(), spiral4[1].flatten()))

    #np.savetxt('Spiraldata.txt', np.hstack(combined_array1.flatten(), combined_array2.flatten()), delimiter='\t')

    with open(f'{max_noise_folder}/4_Spirals_data_theta_max={theta_max}pi_noise={max_noise}.txt', 'w') as file:
        for x in combined_array1:
            file.write(f'1,{np.round(x[0],3)},{np.round(x[1],3)}\n')
        for y in combined_array2:
            file.write(f'2,{np.round(y[0], 3)},{np.round(y[1], 3)}\n')
        for z in combined_array3:
            file.write(f'3,{np.round(z[0], 3)},{np.round(z[1], 3)}\n')
        for t in combined_array4:
            file.write(f'4,{np.round(t[0], 3)},{np.round(t[1], 3)}\n')