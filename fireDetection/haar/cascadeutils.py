import os

def generate_negative_description_file():
    # Open output file for writing. Will overwrite existing data
    with open('neg.txt', 'w') as f:
        # Loop over all filenames
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '\n')
