from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>Cloud-Native CI/CD</title>
            <style>
                body { font-family: 'Segoe UI', Arial, sans-serif; text-align: center; margin-top: 80px; background-color: #fafbfc; color: #2c3e50; }
                .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); display: inline-block; max-width: 500px; }
                h1 { color: #1a73e8; margin-bottom: 10px; }
                .status { background-color: #34a853; color: white; padding: 6px 12px; border-radius: 15px; font-weight: bold; font-size: 14px; }
                .footer { margin-top: 30px; font-size: 12px; color: #7f8c8d; border-top: 1px solid #eee; padding-top: 15px; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Cloud-Native CI/CD Pipeline</h1>
                <p>Aplicatie livrata in mod complet automatizat printr-un pipeline de integrare si deployment continuu.</p>
                <p><span class="status">DEPLOYMENT AUTOMAT REUSIT - Test Live Proiect 2.0</span></p>
                <div class="footer">
                    <strong>Masterand:</strong> Sebastian-Marian Barbu <br>
                    <strong>Stiva Tehnologica:</strong> Python / Flask / Docker / Cloud-Native Pipeline
                </div>
            </div>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return jsonify({"status": "UP", "infrastructure": "cloud-native", "verified_by": "sebastian.barbu"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)