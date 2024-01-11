def play_demo(camera=0, play_time=5):
    # IPythonディスプレイ準備
    notebook_display = IPython.display.display("", display_id=1)

    # カメラキャプチャ設定
    cap = cv.VideoCapture(camera)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 360)

    start_time = time.time()

    while cap.isOpened():
        # カメラ画像取得
        ret, frame = cap.read()
        if ret is False:
            break
        
        ##################
        # その他処理
        ##################
                
        # ディスプレイ表示
        _, frame = cv.imencode('.jpg', frame, [int(cv.IMWRITE_JPEG_QUALITY), 100])
        frame_buffer = BytesIO(frame)
        notebook_display.update(IPython.display.Image(data=frame_buffer.getvalue()))

        if (time.time() - start_time) > play_time:
            break
    cap.release()
