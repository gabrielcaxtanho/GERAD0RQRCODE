from flask import Flask, request, render_template, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color="black", back_color="white")
        buf = BytesIO()
        img_qr.save(buf)
        buf.seek(0)
        return send_file(buf, mimetype='image/png', as_attachment=True, download_name='qrcode.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
