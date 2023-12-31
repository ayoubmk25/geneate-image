from io import BytesIO
from flask import Flask, render_template, request, jsonify
import base64
from PIL import Image

app = Flask(__name__)


def generate_image(input_data):
    
    img = Image.new('RGB', (100, 100), color=(255, 0, 0))
    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    input_data = data['input']

    generated_img = generate_image(input_data)

   
    buffered = BytesIO()
    generated_img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return jsonify({'image': img_str})

if __name__ == '__main__':
    app.run(debug=True)
