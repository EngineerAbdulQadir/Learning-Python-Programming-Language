import cv2

# Using raw strings to avoid the invalid escape sequence issue
face_cascade = cv2.CascadeClassifier(r'Class 02\Projects\haarcascade_frontalface_default.xml')

# Reading the Input Image with a raw string
image = cv2.imread(r'Class 02\Projects\11.jpg')

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found.")
else:
    # Resizing the Image
    img = cv2.resize(image, None, fx=0.3, fy=0.3)

    # Converting the image into grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecting the Faces
    faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

    # Drawing Rectangles around the Faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Displaying the Output Image
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
