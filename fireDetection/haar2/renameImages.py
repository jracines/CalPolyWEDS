import os

def main():
    # Renaming all postiive files
    for count, filename in enumerate(os.listdir("positive")):
        # Put a zero before single digit numbers
        if(count < 10):
            dst ="positive" + "00" + str(count) + ".jpg"
            src ='positive/' + filename
            dst ='positive/' + dst
        elif(count < 100):
            dst ="positive" + "0" + str(count) + ".jpg"
            src ='positive/' + filename
            dst ='positive/' + dst
        else:
            dst ="positive" + str(count) + ".jpg"
            src ='positive/' + filename
            dst ='positive/' + dst
          
        # Rename all the files using new name
        os.rename(src, dst)

    # Renaming all negative files
    for count, filename in enumerate(os.listdir("negative")):
        # Put a zero before single digit numbers
        if(count < 10):
            dst ="negative" + "00" + str(count) + ".jpg"
            src ='negative/' + filename
            dst ='negative/' + dst
        elif(count < 100):
            dst ="negative" + "0" + str(count) + ".jpg"
            src ='negative/' + filename
            dst ='negative/' + dst
        else:
            dst ="negative" + str(count) + ".jpg"
            src ='negative/' + filename
            dst ='negative/' + dst
          
        # Rename all the files using new name
        os.rename(src, dst)

if __name__ == "__main__":
    main()