import cv2

bcd = cv2.barcode.BarcodeDetector()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Check if a frame was read
    if ret:
        ret_bc, decoded_info, _, points = bcd.detectAndDecode(frame)
        if ret_bc:
            frame = cv2.polylines(frame, points.astype(int), True, (0, 255, 0), 3)
            for s, p in zip(decoded_info, points):
                if s:
                    frame = cv2.putText(frame, s, p[1].astype(int), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('Barcode Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()