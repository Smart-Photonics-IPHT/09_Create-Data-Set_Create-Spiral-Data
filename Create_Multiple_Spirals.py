import numpy as np
import matplotlib.pyplot as plt


def generate_multiple_spirals(theta_max, totalpoints = 200, sprials_number = 4, max_noise=0):
    #return a * np.exp(b * t) * np.array([np.cos(t), np.sin(t)])
    t = np.linspace(0, theta_max, totalpoints)
    Sprials = []
    for i in range(0, sprials_number):
        Sprials.append(t * np.array([np.cos(t + i*2*np.pi/(sprials_number)) , np.sin(t + i*2*np.pi/(sprials_number))])
                       + np.random.uniform(-max_noise, max_noise, totalpoints))
    return t, Sprials[:sprials_number]


save_dir = r'C:\Sobhi\Results\spiral\Spiral_Data_Set'
#for theta_max in (2*np.pi, 3*np.pi, 4*np.pi, 5*np.pi, 6*np.pi):
#for theta_max in (6*np.pi):
theta_max = 10*np.pi
#t, spiral1, spiral2 = generate_spiral(theta_max)
for noise in (0.4, 0.6):
    t, [spiral1, spiral2, spiral3, spiral4] = generate_multiple_spirals(theta_max, max_noise=noise)

    plt.figure(figsize=(16, 16))
    plt.scatter(spiral1[0], spiral1[1], s=50, label='Spiral 1', color='blue')
    plt.scatter(spiral2[0], spiral2[1], s=50, label='Spiral 2', color='orange')
    plt.scatter(spiral3[0], spiral3[1], s=50, label='Spiral 3', color='red')
    plt.scatter(spiral4[0], spiral4[1], s=50, label='Spiral 4', color='purple')

    #Set axis limits and add labels
    # plt.xlim([-19, 19])
    # plt.ylim([-19, 19])
    plt.xlabel('X', fontsize=24)
    plt.ylabel('Y', fontsize=24)
    pi_symbol = '\u03c0'
    plt.title(f'Theta_max =10{pi_symbol} _ Max_noise={noise}', fontsize=36)
    plt.gca().set_aspect('equal')

    # Add a legend
    plt.legend(fontsize=14, loc='upper left')
    #plt.show()
    plt.savefig(f'{save_dir}/Multiple_Spirals_theta_max=10pi_max_noise={noise}.png')
    plt.close()
    # cnt += 1
    # Show the plot

    combined_array1 = np.column_stack((spiral1[0].flatten(), spiral1[1].flatten()))
    combined_array2 = np.column_stack((spiral2[0].flatten(), spiral2[1].flatten()))
    combined_array3 = np.column_stack((spiral3[0].flatten(), spiral3[1].flatten()))
    combined_array4 = np.column_stack((spiral4[0].flatten(), spiral4[1].flatten()))

    #np.savetxt('Spiraldata.txt', np.hstack(combined_array1.flatten(), combined_array2.flatten()), delimiter='\t')

    with open(f'{save_dir}/4_Spirals_data_theta_max=10pi_noise={noise}.txt', 'w') as file:
        for x in combined_array1:
            file.write(f'1,{np.round(x[0],3)},{np.round(x[1],3)}\n')
        for y in combined_array2:
            file.write(f'2,{np.round(y[0], 3)},{np.round(y[1], 3)}\n')
        for z in combined_array3:
            file.write(f'3,{np.round(z[0], 3)},{np.round(z[1], 3)}\n')
        for t in combined_array4:
            file.write(f'4,{np.round(t[0], 3)},{np.round(t[1], 3)}\n')