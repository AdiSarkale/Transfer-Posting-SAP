# 🚚 SAP Material Transfer Posting Automation

An end-to-end SAP GUI automation tool built with **Python**, **Flask**, and **React** to automate Material Transfer Posting transactions in SAP. The application provides a user-friendly web interface for entering transfer details and performs the complete SAP transaction using SAP GUI Scripting.

---

## ✨ Features

- Material Transfer Posting Automation
- SAP GUI Scripting Integration
- Modern React Frontend
- Flask REST API Backend
- Real-time Form Validation
- Loading Indicators
- Error Handling & User-Friendly Messages
- Dynamic Material Entry
- Date Formatting & Validation
- CSV Upload Support (if enabled)
- Automated SAP Navigation
- CORS Enabled API

---

## 🛠 Tech Stack

### Frontend
- React
- Vite
- Tailwind CSS
- Axios

### Backend
- Python
- Flask
- Flask-CORS
- pywin32
- SAP GUI Scripting API

---

## 📂 Project Structure

```
Transfer-Posting-SAP
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── services/
│
├── backend/
│   ├── routes/
│   ├── services/
│   ├── helpers/
│   ├── SAP Scripts/
│   └── app.py
│
└── README.md
```

---

## ⚙️ Prerequisites

Before running the project, ensure you have:

- Python 3.10+
- Node.js 18+
- SAP GUI Installed
- SAP GUI Scripting Enabled
- Valid SAP Credentials

SAP GUI Scripting must be enabled both on the SAP Client and SAP Server.

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/AdiSarkale/Transfer-Posting-SAP.git

cd Transfer-Posting-SAP
```

---

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

Backend runs on

```
http://localhost:8080
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

## 🔄 Workflow

1. Launch SAP GUI and login.
2. Start the Flask backend.
3. Run the React frontend.
4. Enter Transfer Posting details.
5. Submit the transaction.
6. The backend connects to the active SAP session.
7. SAP GUI Scripting executes the transfer posting automatically.
8. Success/Error response is returned to the frontend.

---

## 📸 Application Features

- Material Selection
- Plant Selection
- Storage Location
- Quantity Entry
- Posting Date Validation
- Automated SAP Navigation
- Success & Error Notifications
- Responsive UI

---

## 🧠 Concepts Used

- SAP GUI Automation
- COM Automation (pywin32)
- REST APIs
- React Hooks
- Component-Based Architecture
- Axios API Calls
- Flask Routing
- Error Handling
- Dynamic Forms

---

## 🔒 Disclaimer

This project is intended for educational and internal enterprise automation purposes only.

No SAP proprietary code or confidential business logic is included in this repository.

---

## 👨‍💻 Author

**Aditya Sarkale**

GitHub: https://github.com/AdiSarkale

LinkedIn: www.linkedin.com/in/aditya-sarkale-backend

---

## ⭐ If you found this project useful, consider giving it a Star.
