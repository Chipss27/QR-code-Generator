from flask import Flask, render_template, request, send_file
import pyqrcode
from io import BytesIO
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('qrcodeweb.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    link = request.form['link']
    name = request.form['name']

    qr = pyqrcode.create(link)
    # Generate the QR code image in memory
    img_stream = BytesIO()
    qr.png(img_stream, scale=8)

    # Move the BytesIO cursor to the beginning
    img_stream.seek(0)

    # Return the image as a binary response
    return send_file(img_stream, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
