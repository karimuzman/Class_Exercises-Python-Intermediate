import cv2

# Step 1: Prepare the known face(s) and preprocessing

# Step 2: Load and preprocess the known face(s)

# Step 3: Load and preprocess the image to be recognized

# Step 4: Implement face detection

# Step 5: Implement feature extraction

# Step 6: Implement face matching

# Step 7: Display the results

# Load the image
def image():
    image_path = 'a.jpg'
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Implement face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate over the detected faces
    for (x, y, w, h) in faces:
        # Step 4: Extract the bounding box coordinates of the detected face regions

        # Step 5: Implement feature extraction

        # Step 6: Implement face matching

        # Step 7: Display the results
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(image, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting image
    cv2.imshow('Face Recognition', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def camera():
    import cv2
    # Load the pre-trained face detector from OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # Display the resulting frame
        cv2.imshow('Face Recognition', frame)

        # Exit the program if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()


choice = input("Enter 1 to access camera or enter 2 for the image: ")

if choice == '1':
    camera()
elif choice == '2':
    image()