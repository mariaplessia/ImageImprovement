import numpy as np
import cv2
import os
import argparse


def main(args):
    
    dir = "unedited-images/"
    blurry_image = cv2.imread(dir+args.input)


    # Display the input image in the first window
    window_name1 = 'Original Blurry Image'

    cv2.namedWindow(window_name1, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name1, blurry_image)
    cv2.waitKey(5000)

    # Smoothing & Sharpening Filters for image improvement

    if args.input == 'img1.png':
        kernel = np.array([[-1,-1,-1],
                            [-1,9,-1],
                            [-1,-1,-1]])

        smooth = cv2.GaussianBlur(blurry_image, (5,5), 0)
        smoother = cv2.medianBlur(smooth, 3)
        sharp = cv2.filter2D(smoother, -1, kernel)
        improved = cv2.medianBlur(sharp, 3)
        improved = cv2.bilateralFilter(improved, 15, 85, 85)

    if args.input == 'img2.png':
        kernel = np.array([[-1,-1,-1],
                            [-1,9,-1],
                            [-1,-1,-1]])
        
        smooth = cv2.medianBlur(blurry_image, 5)
        sharp = cv2.filter2D(smooth, -1, kernel)
        improved = cv2.medianBlur(sharp, 3)

    if args.input == 'img3.png':
        kernel = np.array([[-1,-1,-1],
                            [-1,9,-1],
                            [-1,-1,-1]])

        smooth = cv2.medianBlur(blurry_image, 3)
        sharp = cv2.filter2D(smooth, -1, kernel)
        improved = cv2.bilateralFilter(sharp, 5, 65, 65)

    if args.input == 'img4.png':
        kernel = np.array([[-1,-1,-1],
                            [-1,9,-1],
                            [-1,-1,-1]])
        
        sharp = cv2.filter2D(blurry_image, -1, kernel)
        improved = cv2.bilateralFilter(sharp, 5, 45, 45)
        
    # Save and display edited image
    cv2.imwrite(os.path.splitext(args.input)[0]+"-edited.png", improved)
    cv2.imshow("Sharp ", improved)
    cv2.waitKey(5000)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image improvement via area-to-pixel filters')
    parser.add_argument('-i', default='img1.png')
    args = parser.parse_args()

    main(args)
