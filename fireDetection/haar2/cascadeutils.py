import os

def generate_negative_description_file():
    # Open output file for writing. Will overwrite existing data
    with open('neg.txt', 'w') as f:
        # Loop over all filenames
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '\n')

# Generate negative description file
#   In terminal
#       python
#       from cascadeutils import generate_negative_description_file
#       generate_negative_description_file()
#       quit()
#
# Generate positive description file:
#   C:/Users/Jayare/Downloads/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=positive/
#   Don't forget to go into pos.txt and change '\' to '/'
#
# Generate vector file
#   C:/Users/Jayare/Downloads/opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec
#
# Train cascade classifier
#   Create a folder called cascade
#   C:/Users/Jayare/Downloads/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 45 -numNeg 100 -numStages 10
#   numPos must be less than number of sample (rectangles drawn)
#   numNeg can be any number, some say it must be 1/2 or 2x the positive samples
#   numStages beware of overtraining... 10 stages is good for 200 samples
#   HR: hit rate, FA: false alarm, N: weak layer number... detail increases with each layer
#       Layer 1, 2, ... are the outermost layers 
#       Want the final layer to have the smallest FA rate possible without over training
#   Overtraining: if NEG count : acceptanceRatio 100 : 0.0000... more than 4 zeros
#
#   Other parameters
#       -precalcValBufSize:     gives more memory to help model train faster
#       -maxFalseAlarmRate:     keeps adding more layers until this value is reached
#       -minHitRate:            keeps adding more layers until this value is reached    
#
#   C:/Users/Jayare/Downloads/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 24 -h 24 -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos 45 -numNeg 500 -numStages 12 -maxFalseAlarmRate 0.3 -minHitRate 0.999