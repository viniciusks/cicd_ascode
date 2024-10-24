from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Service is running"}), 200

@app.route('/base/veracode/', methods=['POST'])
def veracode():
    return jsonify({"message": "Mocked Veracode service"}), 200

@app.route('/base/browserstack/', methods=['POST'])
def browserstack():
    return jsonify({"message": "Mocked BrowserStack service"}), 200

@app.route('/base/cyberark/chave', methods=['GET'])
def cyberark_chave():
    return jsonify({"message": "Mocked CyberArk chave"}), 200

if __name__ == '__main__':
    # Listen on all interfaces (important for containerized environments)
    app.run(debug=True, host='0.0.0.0', port=5000)
