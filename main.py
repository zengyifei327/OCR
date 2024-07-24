import pytesseract
import PIL.Image
import cv2


def main():
    myconfig = r"--psm 6 --oem 3"
    text = pytesseract.image_to_string(PIL.Image.open("text.png"), config=myconfig)
    print(text)


if __name__ == "__main__":
    main()
