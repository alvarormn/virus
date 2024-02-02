from flask import render_template, request, redirect, url_for
import cv2
import numpy as np
from app import app
import os

@app.route('/')
def index():
    return "¡Hola, Mundo!"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' in request.files:
        file = request.files['image']
        # Convertir el archivo a un array NumPy y luego a una imagen OpenCV
        npimg = np.fromfile(file, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        # Procesamiento de la imagen y obtención de resultados
        # ...

        return jsonify({"message": "Imagen procesada correctamente"})
    return jsonify({"error": "No se proporcionó ninguna imagen"}), 400
