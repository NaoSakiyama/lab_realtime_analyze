import cv2
import numpy as np
from matplotlib import pyplot as plt

# カメラの準備
cap = cv2.VideoCapture(0)

while True:
    # フレームの取得
    ret, frame = cap.read()
    
    # グレースケールに変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 2次元フーリエ変換
    f_transform = np.fft.fft2(gray)
    f_transform_shifted = np.fft.fftshift(f_transform)
    
    # 物体光成分の抽出（例: 中心から30x30の領域をゼロにする）
    rows, cols = gray.shape
    crow, ccol = rows // 2 , cols // 2
    f_transform_shifted[crow-15:crow+15, ccol-15:ccol+15] = 0
    
    # 逆フーリエ変換
    f_transform_inverse = np.fft.ifftshift(f_transform_shifted)
    img_back = np.fft.ifft2(f_transform_inverse)
    img_back = np.abs(img_back)
    
    # 結果の表示
    cv2.imshow('Original', frame)
    cv2.imshow('Filtered', np.uint8(img_back))
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# 後処理
cv2.destroyAllWindows()
cap.release()
