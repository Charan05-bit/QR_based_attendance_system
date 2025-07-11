
# QR Code Attendance System
A modern, lightweight attendance tracking system that uses QR codes and local network verification to record student attendance without requiring logins or cloud services.

## Features

### Core Functionality
- 🖥️ **Teacher Interface**: Generates QR codes with embedded attendance links
- 📱 **Student Interface**: Mobile-friendly form for submitting attendance
- 🌐 **Local Network Verification**: Ensures students are physically present by checking IP subnet
- 📊 **Simple Data Storage**: Records attendance to CSV file (can be exported to Excel)

### Technical Highlights
- 💻 Single Python script backend (Flask)
- 🔗 No database required (uses CSV files)
- 📶 Works on local WiFi network
- 🛡️ No student login required
- 📱 Mobile-first design for student interface

## How It Works

### Teacher Setup
1. Teacher runs the Python script on a classroom computer
2. System generates a QR code containing the local server URL
3. Teacher displays the QR code to students (projector or screen)

### Student Process
1. Student scans QR code with smartphone camera
2. Mobile browser opens attendance form
3. System verifies student is on same local network
4. Student submits ID and name
5. Attendance recorded with timestamp

## Technology Stack

| Component       | Technology Used |
|----------------|----------------|
| Backend        | Python Flask   |
| Frontend       | HTML5, Bootstrap 5 |
| QR Generation  | Python qrcode library |
| Data Storage   | CSV (can upgrade to SQLite) |
| Styling        | Custom CSS with Bootstrap |

## Installation

### Requirements
- Python 3.6+
- Flask
- qrcode library

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/qr-attendance-system.git

# Navigate to project directory
cd qr-attendance-system

# Install requirements
pip install -r requirements.txt

# Run the application
python server.py
```

## Usage

1. **Start the server**:
   ```bash
   python server.py
   ```

2. **Access teacher interface**:
   - Open `http://localhost:5000` in browser
   - Display the generated QR code to students

3. **Student attendance**:
   - Students scan QR code with smartphone
   - Submit their details through the form

4. **View attendance records**:
   - Check generated `attendance.csv` file
   - File format: `class_attendance,student_id,student_name,timestamp`

## Customization Options

1. **Change class name**:
   - Modify `class_attendance` variable in `server.py`

2. **Upgrade to database**:
   - Replace CSV storage with SQLite for better scalability

3. **Add authentication**:
   - Implement simple teacher login if needed

4. **Custom styling**:
   - Edit CSS in the template files

## Project Structure

```
qr-attendance-system/
├── server.py            # Main Flask application
├── templates/
│   ├── teacher.html     # Teacher interface
│   └── student.html     # Student attendance form
├── static/
│   └── qr.png           # Generated QR code
├── attendance.csv       # Attendance records
└── README.md            # This documentation
```

## Screenshots

**Teacher Interface**  
![image alt](https://github.com/Charan05-bit/QR_based_attendance_system/blob/be59c71773f0e8b8bc998dc0aa882dc27260d39c/Screenshot%20(39).png)

**Student Mobile View**  
![Student View](https://i.imgur.com/example2.jpg)

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/yourfeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/yourfeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions or issues, please [open an issue](https://github.com/charan05-bit/qr-attendance-system/issues) on GitHub.
