from flask import Flask, render_template, request, send_file
import os
from app.model.style_transfer import image_loader, run_style_transfer

app = Flask(__name__)
UPLOAD_FOLDER = 'app/static/uploads'
RESULT_FOLDER = 'app/static/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    content = request.files['content']
    style = request.files['style']

    content_path = os.path.join(UPLOAD_FOLDER, content.filename)
    style_path = os.path.join(UPLOAD_FOLDER, style.filename)

    content.save(content_path)
    style.save(style_path)

    content_img = image_loader(content_path, imsize=512)
    style_img = image_loader(style_path, imsize=512)

    output = run_style_transfer(content_img, style_img, None)

    output_path = os.path.join(RESULT_FOLDER, 'output.jpg')
    output_img = transforms.ToPILImage()(output.squeeze(0))
    output_img.save(output_path)

    return render_template('result.html',
                           content_image=content.filename,
                           style_image=style.filename,
                           output_image='output.jpg')

if __name__ == '__main__':
    app.run(debug=True)
