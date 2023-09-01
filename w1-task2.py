import cv2 as cv
capture = cv.VideoCapture('/Users/jackiecrickwu/Desktop/USRC workshop/firework.MOV')

while True:
    retval, frame = capture.read()
    if not retval:
        break
    cv.imshow('firework.MOV', frame)

    if cv.waitKey(17) == ord('d'):
        break

capture.release()
cv.destroyAllWindows()