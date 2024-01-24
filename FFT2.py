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
    crow, ccol = 60 ,193
    cropped_width, cropped_height = 50, 50
    mask = np.zeros((rows, cols))
    f_transform_shifted[rows//2-cropped_height:rows//2+cropped_height, cols//2 -cropped_width:cols//2+cropped_width] = f_transform_shifted[crow-cropped_height:crow+cropped_height, ccol-cropped_width:ccol+cropped_height]
    
    f_transform_shifted[:rows//2-cropped_height] = 0
    f_transform_shifted[rows//2+cropped_height:] = 0
    f_transform_shifted[:,:cols//2-cropped_width] = 0
    f_transform_shifted[:,cols//2+cropped_width:] = 0
    
    plt.imshow(np.abs(np.log(1+f_transform_shifted)), cmap = 'gray')
    plt.title('cropped_shift')
    plt.show()
    # 逆フーリエ変換
    f_transform_inverse = np.fft.ifftshift(f_transform_shifted)
    img_back = np.fft.ifft2(f_transform_inverse)
    img_amplitude = np.abs(img_back)
    img_phase = np.angle(img_back)
    
    # 結果の表示
    cv2.imshow('Original', frame)
    cv2.imshow('Reconstruction_amp', np.uint8(img_amplitude))
    cv2.imshow('Reconstruction_phase', np.uint8(img_phase))  
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    plt.imshow(np.abs(np.log(1+f_transform_shifted)))
    plt.title('FI')
    plt.show()
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

# 後処理
cv2.destroyAllWindows()
cap.release()
      
