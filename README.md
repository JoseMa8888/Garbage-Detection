# 🚀 Trash Detection with AI Models

Project implementing two AI models (MobileNet and VisionTransformer) for classifying types of trash through images, with a web interface built using FastAPI.

## 🌟 Main Features

- **Two detection models**:
  - MobileNet model (MN)
  - Vision Transformer model (ViT)
- **REST API** with FastAPI
- **Interactive web interface**
- **Automatic documentation** (Swagger UI)
- **Real-time processing** with timing metrics

## 📸 Examples

<p align="center">
  <img src="images/home.png" width="1200" />
</p>

<p align="center" float="left">
  <img src="images/mn_detection.png" width="500" />
  <img src="images/vit_detection.png" width="500" />
</p>

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green?logo=fastapi)
![ONNX](https://img.shields.io/badge/ONNX-1.10+-orange?logo=onnx)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-red?logo=opencv)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?logo=javascript)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
2. Create and activate a virtual environment
- On Windows
```bash
python -m venv venv
venv\Scripts\activate
```
- On Linux/Mac
```bash
python -m venv venv
source venv/bin/activate
```
3. Install the dependencies
```bash
pip install -r requirements.txt
```
4. 🚀 Launch your server
```bash
uvicorn main:app --reload
```
## 🌐 Access the App

Once the server is running, you can access the following from your browser:

### 🖥️ Web Interface

[http://localhost:8000](http://localhost:8000)

### 📚 API Documentation (Swagger UI)

[http://localhost:8000/docs](http://localhost:8000/docs)

## 🖥️ Usage

### 🌍 Web Interface

1. Select the desired model (MV or ViT).
2. Upload an image.
3. View the classification results and prediction time.

## 📊 Performance

| Model | Parameters (M) | Accuracy | Top 2 Accuracy | 
|-------|----------------|----------|----------------|
| MN    | 5.4            | 80%      | 90%            |
| ViT   | 86             | 84%      | 93%            |
