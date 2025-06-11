from flask import Flask, request, render_template, jsonify
import qrcode
import qrcode.image.svg
from io import BytesIO
import socket
import csv
from datetime import datetime

app = Flask(__name__, static_folder='static')

# Get local IP address
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

# Store attendance in CSV
def record_attendance(class_attendance, student_id, student_name):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('attendance.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([class_attendance, student_id, student_name, timestamp])

@app.route('/')
def home():
    class_attendance = "MATH101"  # Could be made dynamic
    local_ip = get_local_ip()
    port = 5000
    url = f"http://{local_ip}:{port}/attendance?class_attendance={class_attendance}"
    
    # Generate QR code
    img = qrcode.make(url)
    img.save("static/qr.png")
    
    return render_template('teacher.html', qr_url=url)

@app.route('/attendance')
def attendance():
    class_attendance = request.args.get('class_attendance')
    return render_template('student.html', class_attendance=class_attendance)

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    data = request.json
    class_attendance = data['class_attendance']
    student_id = data['student_id']
    student_name = data['student_name']
    
    # Verify student IP is in same subnet (basic check)
    student_ip = request.remote_addr
    server_ip = get_local_ip()
    
    if server_ip.rsplit('.', 1)[0] == student_ip.rsplit('.', 1)[0]:
        record_attendance(class_attendance, student_id, student_name)
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "message": "Not on local network"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)