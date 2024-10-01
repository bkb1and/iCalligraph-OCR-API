# PaddleOCR API 项目

## 项目概述

这是一个基于 Python 和 PaddleOCR 库开发的 OCR API 服务。该项目可以通过 HTTP 请求接收图片，并返回识别出的文字内容。

## 功能特点

-   使用 Flask 框架构建 Web API
-   支持中文文字识别
-   能够处理文字旋转的情况
-   通过 ngrok 实现内网穿透，使本地服务可以被外网访问

## 使用方法

1. 运行 `call.py` 启动 Flask 服务器
2. 使用 ngrok 进行内网穿透，将本地主机暴露给外网
3. 客户端可以通过以下方式调用 API：
    - curl 命令行工具
    - Python requests 库
    - Postman 等 API 测试工具

## API 端点

-   **URL**: `/ocr`
-   **方法**: POST
-   **参数**:
    -   `image`: 图片文件（multipart/form-data）
-   **返回**: JSON 格式的识别结果

## 依赖库

-   Flask
-   Pillow (PIL)
-   NumPy
-   PaddleOCR
-   PaddlePaddle

## 安装依赖

```bash
pip install flask pillow numpy paddleocr paddlepaddle
```

## 注意事项

-   确保已正确安装并配置 PaddlePaddle 和 PaddleOCR
-   使用 CPU 进行处理，如需使用 GPU 可修改相关配置
-   项目中设置了环境变量 `KMP_DUPLICATE_LIB_OK="TRUE"` 以解决潜在的库冲突问题
