from flask import Flask, request, jsonify
import sqlite3
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
DATABASE = 'careers.db'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT,
            resume_path TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/apply', methods=['POST'])
def apply():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    resume = request.files.get('resume')

    if not name or not email or not resume:
        return jsonify({'status': 'error', 'message': 'Missing required fields (name, email, resume)'}), 400

    if resume and resume.filename:
        filename = secure_filename(resume.filename)
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume.save(resume_path)
    else:
        return jsonify({'status': 'error', 'message': 'Resume file not provided or invalid'}), 400

    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO applications (name, email, message, resume_path) VALUES (?, ?, ?, ?)",
                       (name, email, message, resume_path))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success', 'message': 'Application submitted successfully'}), 201
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/admin/applications', methods=['GET'])
def admin_applications():
    # In a real application, this would be login-protected
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, message, resume_path FROM applications")
    applications = cursor.fetchall()
    conn.close()

    application_list = []
    for app_data in applications:
        application_list.append({
            'name': app_data[0],
            'email': app_data[1],
            'message': app_data[2],
            'resume_path': app_data[3]
        })
    return jsonify({'status': 'success', 'applications': application_list}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5002)

