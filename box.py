import cv2
import pytesseract


def main():
    myconfig = r"--psm 11 --oem 3"

    img = cv2.imread("text.png")
    height, width, _ = img.shape

    boxes = pytesseract.image_to_boxes(img, config=myconfig)
    for box in boxes.splitlines():
        box = box.split(" ")
        img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255,
                                                                                                            0), 2)

    cv2.imshow("img", img)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
