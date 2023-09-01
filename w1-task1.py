# Demo
import cv2 as cv

def main():
    kangaroo = cv.imread('/Users/jackiecrickwu/Desktop/kangaroo.jpeg')
    cv.imshow('Kangaroo', kangaroo)
    cv.waitKey(0)




if  __name__ == '__main__':
    main()