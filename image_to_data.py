import cv2
import pytesseract
from pytesseract import Output


def main():
    myconfig = r"--psm 11 --oem 3"

    img = cv2.imread("text.png")
    height, width, _ = img.shape

    data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

    # print(data["text"])
    amount_boxes = len(data['text'])
    for i in range(amount_boxes):
        if float(data['conf'][i]) > 80:
            (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
            img = cv2.putText(img, data['text'][i], (x, y + height + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0),
                              2, cv2.LINE_AA)

    cv2.imshow("img", img)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
