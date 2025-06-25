from flask import Flask, request, jsonify, render_template_string, redirect, url_for, session
import requests
import os

app = Flask(__name__)
app.secret_key = os.urandom(24) # Replace with a strong, fixed secret key in production

# ✅ ADD THIS ROUTE
@app.route("/")
def index():
    return "Admin service is up and running."
    
# Mock authentication for admin
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "adminpass"

# Service URLs (replace with actual Kubernetes service names/IPs in a real deployment)
CONTACT_SERVICE_URL = "http://localhost:5001"
CAREERS_SERVICE_URL = "http://localhost:5002"

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("admin_dashboard"))
        else:
            return "Invalid credentials", 401
    return render_template_string("""
        <form method="post">
            <input type="text" name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <input type="submit" value="Login">
        </form>
    """)

@app.route("/admin/logout")
def admin_logout():
    session.pop("logged_in", None)
    return redirect(url_for("admin_login"))

def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("admin_login"))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/admin")
@login_required
def admin_dashboard():
    contacts_data = []
    careers_data = []

    try:
        contacts_response = requests.get(f"{CONTACT_SERVICE_URL}/admin/contacts")
        contacts_response.raise_for_status()
        contacts_data = contacts_response.json().get("contacts", [])
    except requests.exceptions.RequestException as e:
        contacts_data = [{"error": f"Could not fetch contacts: {e}"}]

    try:
        careers_response = requests.get(f"{CAREERS_SERVICE_URL}/admin/applications")
        careers_response.raise_for_status()
        careers_data = careers_response.json().get("applications", [])
    except requests.exceptions.RequestException as e:
        careers_data = [{"error": f"Could not fetch careers: {e}"}]

    return render_template_string("""
        <h1>Admin Dashboard</h1>
        <p><a href="/admin/logout">Logout</a></p>

        <h2>Contact Entries</h2>
        <table border="1">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Message</th>
                </tr>
            </thead>
            <tbody>
                {% for contact in contacts_data %}
                <tr>
                    <td>{{ contact.name }}</td>
                    <td>{{ contact.email }}</td>
                    <td>{{ contact.message }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>

        <h2>Career Applications</h2>
        <table border="1">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Message</th>
                    <th>Resume Path</th>
                </tr>
            </thead>
            <tbody>
                {% for app in careers_data %}
                <tr>
                    <td>{{ app.name }}</td>
                    <td>{{ app.email }}</td>
                    <td>{{ app.message }}</td>
                    <td>{{ app.resume_path }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    """, contacts_data=contacts_data, careers_data=careers_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

