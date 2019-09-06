# This will be our editing script

import sys
import cv2
import numpy

def main():
    print("Welcome to our image editor!\n")
    image_file = ask_for_image_file()
    try:
        image = cv2.imread(image_file)
    except:
        #This is clearly not going to work at the moment because if the image file is some random name, the read isn't throwing an error
        print("The image file you entered was unreadable. Please ensure your image file is in the current directory, the filetype is correct, and the name is spelled properly, then rerun the script.")
        sys.exit()
    
    filter_type = ask_for_filter_type()

    if filter_type == "blur":
        matrix = get_blur_matrix()
    elif filter_type == "sharpen":
        matrix = get_sharpen_matrix()
    else:
        print("Error: Filter Type returned no matrix.")
        sys.exit()
    


def ask_for_filter_type():
    filter_type = ""
    while filter_type != "blur" and filter_type != "sharpen":
        filter_type = input('How would you like to edit your image? Enter "blur" for blur, or "sharpen" for sharpen: ')
        if filter_type != "blur" and filter_type != "sharpen":
            print("Please retry.")
    return filter_type

def ask_for_image_file():
    img_file = ""
    while img_file == "":
        img_file = input('Enter the file name of the image you would like to edit: ')
    return img_file

def get_blur_matrix():
    matrix = ''
    return matrix

def get_sharpen_matrix():
    matrix = ''
    return matrix

if __name__== "__main__":
    main()