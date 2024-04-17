from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

def generate_qrcode(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        if url:
            qr_img = generate_qrcode(url)
            img_bytes = BytesIO()
            qr_img.save(img_bytes)
            img_bytes.seek(0)
            return send_file(img_bytes, mimetype='image/png', download_name='qrcode.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
