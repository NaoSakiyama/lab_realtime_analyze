import cv2

#captureの準備
cap = cv2.VideoCapture(0)

#起動と画面表示まで
while(1):
    #capture frameの作成
    _, frame = cap.read()
    cv2.imshow('Original', frame)

    #originalの反転（鏡状態）
    original = cv2.flip(frame, 1)
    cv2.imshow('Inversion', original)

    #binarization
    gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)
    cv2.imshow('Binarization', gray)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
