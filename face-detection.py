import cv2
import mediapipe as mp

# img = cv2.imread(r"C:\Users\Abdullah Usama\Desktop\DL\computer-vision\media\dawwg.png")
# img = cv2.resize(img, (400, 500))


def process_img(img, face_detection, h, w):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output = face_detection.process(img_rgb)
    if output.detections is None:
        print("NO FACE DETECTED")
        exit
    if output.detections is not None:
        for detect in output.detections:
            loc_data = detect.location_data
            bbox = loc_data.relative_bounding_box
            x1, y1, b_w, b_h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            x1 = int(x1 * w)
            y1 = int(y1 * h)
            b_w = int(b_w * w)
            b_h = int(b_h * h)

            x1 = max(0, min(x1, w - 1))
            y1 = max(0, min(y1, h - 1))
            x2 = min(x1 + b_w, w)
            y2 = min(y1 + b_h, h)

            if x1 < x2 and y1 < y2:
                face_region = img[y1:y2, x1:x2]
                if face_region.size > 0:
                    # for blur effect
                    img[y1:y2, x1:x2] = cv2.blur(face_region, (80, 80))
                    # for rectangle on face
                    img = cv2.rectangle(
                        img, (x1, y1), (x1 + b_w, y1 + b_h), (0, 255, 0), 2
                    )
            # print(img.shape)
    return img


detect_object = mp.solutions.face_detection

vid = cv2.VideoCapture(0)

while True:
    ret, img = vid.read()
    with detect_object.FaceDetection(
        model_selection=0, min_detection_confidence=0.3
    ) as face_detection:
        h, w, _ = img.shape
        img = process_img(img, face_detection, h, w)
        img = cv2.flip(img, 1)
        img = cv2.resize(img, (int(640 * 1.3), int(480 * 1.3)))
        cv2.imshow("res", img)
        if cv2.waitKey(1) == ord("q"):
            break

cv2.destroyAllWindows()
