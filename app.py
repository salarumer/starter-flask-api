from flask import Flask, request, send_file
import os
import cv2
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_image():
    # Check if an image is received
    if 'image' not in request.files:
        return 'No image uploaded', 400
    
    # Get the image file from the POST request
    image_file = request.files['image']
    
    # Read the image using OpenCV
    image_data = image_file.read()
    nparr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Perform some processing on the image (example: convert to grayscale)
    processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert the processed image back to bytes
    _, img_encoded = cv2.imencode('.jpg', processed_img)
    
    # Send the processed image back to the frontend
    return send_file(BytesIO(img_encoded), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
