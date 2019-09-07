# This is an image editing script that uses kernel matrices
# to edit an images rgb values and produce a new image

import sys
import cv2
import numpy as np

def main():
    print("\nWelcome to our image editor!\n")
    image_file = ask_for_image_file()
    image_shape = None
    try:
        image = cv2.imread(image_file)
        image_shape = image.shape
        b,g,r = cv2.split(image)
    except:
        print("The image file you entered was unreadable. Please ensure your image file is in the current directory, the filetype is correct, and the name is spelled properly. Then rerun the script.")
        sys.exit()

    width = image_shape[0]
    height = image_shape[1]
    filter_type = ask_for_filter_type()
    matrix = None

    if filter_type == "blur":
        matrix = get_blur_matrix()
    elif filter_type == "sharpen":
        matrix = get_sharpen_matrix()
    else:
        print("Error: Filter Type returned no matrix.")
        sys.exit()

    new_b = np.zeros((width, height))
    new_g = np.zeros((width, height))
    new_r = np.zeros((width, height))

    for i in range(1, width - 1):
        for j in range(1, height - 1):
            new_b[i, j] = np.sum(b[i-1:i+2, j-1:j+2] * matrix)
            new_g[i, j] = np.sum(g[i-1:i+2, j-1:j+2] * matrix)
            new_r[i, j] = np.sum(r[i-1:i+2, j-1:j+2] * matrix)
    
    new_image = cv2.merge((new_b,new_g,new_r))
    new_name = image_file.split('.')[0] + '-' + filter_type + '.jpg'
    cv2.imwrite(new_name, new_image)
    print("Your " + filter_type + " is complete!")

def ask_for_filter_type():
    filter_type = ""
    while filter_type != "blur" and filter_type != "sharpen":
        filter_type = input('How would you like to edit your image? Enter "o" for options: ')
        if filter_type == "o":
            print('\nEnter:\n    - "blur" to blur your image\n    - "sharpen" to sharpen your image\n')
        elif filter_type != "blur" and filter_type != "sharpen":
            print("Please retry.")
    print("Processing... this may take a second.")
    return filter_type

def ask_for_image_file():
    img_file = ""
    while img_file == "":
        img_file = input('Enter the file name of the image you would like to edit: ')
        print('')
    return img_file

def get_blur_matrix():
    matrix = [[1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9]]
    return matrix

def get_sharpen_matrix():
    matrix = [[0, -1, 0],
              [-1, 5, -1],
              [0, -1, 0]]
    return matrix

if __name__== "__main__":
    main()