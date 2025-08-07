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
2. Using pyenv for versioning `Python3.9`
- On Windows.
If you don't have python3.9 you can use pyenv. Check this repository: 
[https://github.com/pyenv-win/pyenv-win](https://github.com/pyenv-win/pyenv-win) 
Or just download python3.9 from its webpage: [https://www.python.org/downloads](https://www.python.org/downloads).
Then you must use python3.9 in order to create your environment 

- On Linux/Mac. To install pyenv use:
  ```bash
  brew install pyenv
  ```
  Then in your terminal write:
  ```bash
  nano ~/.zshrc
  ```
  Then copy this lines:
  ```bash
  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
  ```
  Save and refresh with:
  ```bash
  source ~/.zshrc
  ```
Then you have to use pyenv
```bash
pyenv install 3.9
```
Go to your your project route and initialize your python3.9. After closing your terminal, it will return to your original version.
```bash
cd your_project_route
pyenv shell 3.9
```
3. Then you can create your virtual environment

```bash
python -m venv venv
```
On windows
```bash
venv\Scripts\activate
```
On linux/mac
```bash
source venv/bin/activate
```
3. Install the dependencies: You have two requirement files. One for the dependencies that I needed to use only the service and the other one was the one that I used for creating the whole project
- Small requirements (`Recommended for only API users`)
  ```bash
  pip install -r requirements_small.txt
  ```
- Whole requirements
  ```bash
  pip install -r requirements.txt
  ```
4. 🚀 Launch your server
```bash
uvicorn service.main:app --reload
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
