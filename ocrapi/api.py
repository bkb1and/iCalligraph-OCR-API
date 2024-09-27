from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
from paddleocr import PaddleOCR
import paddle
import os

paddle.set_device('cpu')
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

app = Flask(__name__)

# 初始化 PaddleOCR
# 支持中文识别，use_angle_cls 处理文字旋转
ocr_model = PaddleOCR(use_angle_cls=True, lang='ch')

@app.route('/ocr', methods=['POST'])
def ocr_process():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file in the request'}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # 打开图片并转换为 numpy 数组
        image_data = Image.open(image_file)
        image_np = np.array(image_data)

        # 使用 PaddleOCR 进行 OCR 识别
        result = ocr_model.ocr(image_np)

        # 提取 OCR 识别的文字内容
        text = '\n'.join([line[1][0] for line in result[0]])

        response = {
            'status': 'success',
            'text': text
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
