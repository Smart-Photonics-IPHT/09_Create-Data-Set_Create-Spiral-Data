import numpy as np
import matplotlib.pyplot as plt

saving_dir = r'C:\Sobhi\Results\spiral\AccuracyVsBins\theta_max=6pi\scale_factor=pi_over_2'

for bins_number in (2, 4, 5, 10, 25):
    spiral1X = []
    spiral1Y = []
    spiral2X = []
    spiral2Y = []
    with open(f'{saving_dir}/Spiral_theta_max=6pi_scaling_factor=pi_over_2_bins={bins_number}.txt', 'r') as Spirals:
        for line in Spirals:
            values = line.strip().split(',')
            print(values)
            if values[0] == '1':
                spiral1X.append(float(values[1]))
                spiral1Y.append(float(values[2]))
            elif values[0] == '0':
                spiral2X.append(float(values[1]))
                spiral2Y.append(float(values[2]))

    print('spiral1x', len(spiral1X))
    print('spiral2x', len(spiral2X))
    plt.figure(figsize=(16, 16))

    plt.scatter(spiral1X, spiral1Y, label='Spiral 1', s=150,  color='blue')
    plt.scatter(spiral2X, spiral2Y, label='Spiral 2', s=150,  color='orange')

    plt.xlabel('X', fontsize=24)
    plt.ylabel('Y', fontsize=24)
    # pi_symbol = '\u03c0'
    plt.title(f'Classification Results, bins number = {bins_number}', fontsize=40)
    # Add a legend
    plt.legend(fontsize=28)
    plt.gca().set_aspect('equal')

    plt.savefig(f'{saving_dir}/modified_plot_bins={bins_number},classification results.png')
    #plt.show()
    plt.close()