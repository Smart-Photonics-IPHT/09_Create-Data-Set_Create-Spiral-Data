import numpy as np

# Replace 'your_data.npy' with the desired name for the data file
folder = r'C:\Sobhi\Spiral Classification'
data_file_path = f'{folder}/spiral.data'

# Example: Loading data from a text file (replace with your file path)
text_file_path = f'{folder}/spiral.txt'
data_array = np.loadtxt(text_file_path)

# Save the NumPy array as a binary data file (npy format)
np.save(data_file_path, data_array)