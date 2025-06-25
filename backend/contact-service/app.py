from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'contacts.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({'status': 'error', 'message': 'Missing fields'}), 400

    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                       (name, email, message))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success', 'message': 'Contact form submitted successfully'}), 201
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/admin/contacts', methods=['GET'])
def admin_contacts():
    # In a real application, this would be login-protected
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, message FROM contacts")
    contacts = cursor.fetchall()
    conn.close()

    contact_list = []
    for contact in contacts:
        contact_list.append({
            'name': contact[0],
            'email': contact[1],
            'message': contact[2]
        })
    return jsonify({'status': 'success', 'contacts': contact_list}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5001)


