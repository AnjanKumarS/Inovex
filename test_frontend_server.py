from flask import Flask, send_from_directory, redirect
import os

app = Flask(__name__)
BASE = os.path.abspath(os.path.dirname(__file__))

# Map routes to their respective frontend folders and HTML files
ROUTES = {
    '/': ('frontend/home-frontend', 'index.html'),
    '/services': ('frontend/services-frontend', 'services.html'),
    '/industries': ('frontend/industries-frontend', 'industries.html'),
    '/about-us': ('frontend/aboutus-frontend', 'about-us.html'),
    '/careers': ('frontend/careers-frontend', 'careers.html'),
    '/contact': ('frontend/contact-frontend', 'contact.html'),
    '/admin': ('frontend/admin-frontend', 'index.html'),
    '/auth': ('frontend/auth-frontend', 'index.html'),
}

# Serve main pages with unique endpoint names
for route, (folder, html_file) in ROUTES.items():
    def make_view(folder=folder, html_file=html_file):
        def view():
            return send_from_directory(os.path.join(BASE, folder), html_file)
        return view
    endpoint = f"view_{route.strip('/').replace('-', '_') or 'home'}"
    app.add_url_rule(route, view_func=make_view(), endpoint=endpoint)
    # Also support .html extension for direct access
    if not route.endswith('.html'):
        endpoint_html = f"{endpoint}_html"
        app.add_url_rule(route + '.html', view_func=make_view(), endpoint=endpoint_html)

# Serve static files (css/js/images) for each frontend
@app.route('/<section>/<path:filename>')
def serve_section_static(section, filename):
    section_map = {
        'home-frontend': 'frontend/home-frontend',
        'services-frontend': 'frontend/services-frontend',
        'industries-frontend': 'frontend/industries-frontend',
        'aboutus-frontend': 'frontend/aboutus-frontend',
        'careers-frontend': 'frontend/careers-frontend',
        'contact-frontend': 'frontend/contact-frontend',
        'admin-frontend': 'frontend/admin-frontend',
        'auth-frontend': 'frontend/auth-frontend',
    }
    if section in section_map:
        return send_from_directory(os.path.join(BASE, section_map[section]), filename)
    return '', 404

# Serve images from each frontend's Images folder
@app.route('/Images/<path:filename>')
def serve_images(filename):
    # Try to find the image in each frontend's Images folder
    frontend_folders = [
        'frontend/home-frontend',
        'frontend/services-frontend', 
        'frontend/industries-frontend',
        'frontend/aboutus-frontend',
        'frontend/careers-frontend',
        'frontend/contact-frontend',
        'frontend/admin-frontend',
        'frontend/auth-frontend'
    ]
    
    for folder in frontend_folders:
        image_path = os.path.join(BASE, folder, 'Images', filename)
        if os.path.exists(image_path):
            return send_from_directory(os.path.join(BASE, folder, 'Images'), filename)
    
    return '', 404

if __name__ == '__main__':
    app.run(debug=True, port=5000) 