# SAP Material Transfer Posting Automation

> **Copyright & Usage Notice**  
> Copyright © 2026 Aditya Sarkale. All rights reserved **to the extent of rights owned by the author**.  
> No license is granted to copy, modify, redistribute, publish, sublicense, or use this source code or substantial portions of it outside the GitHub platform without prior written permission from the applicable rights holder.  
> **Important:** Any company-owned, client-owned, SAP-proprietary, third-party, or otherwise restricted material remains subject to its applicable ownership, confidentiality, and licensing terms.

## Overview
An end-to-end SAP GUI automation application built with **Python, Flask and React** to automate material transfer-posting workflows through SAP GUI Scripting.

## Workflow
1. Launch SAP GUI and log in.
2. Start the Flask backend.
3. Start the React frontend.
4. Enter material transfer details.
5. Submit the request.
6. The backend connects to the active SAP GUI session.
7. SAP GUI Scripting performs the required transaction steps.
8. Success/error information is returned to the frontend.
9. Validate the posting in SAP.

## Technology
- Python
- Flask / Flask-CORS
- pywin32
- SAP GUI Scripting API
- React / Vite
- Axios
- JavaScript / CSS

## Prerequisites
- Windows
- SAP GUI for Windows
- SAP GUI Scripting enabled
- Python 3.10+
- Node.js 18+
- Appropriate SAP authorization

## Structure
```
frontend/      React/Vite UI
backend/       Flask API and SAP automation
README.md      Project documentation
```

## Installation

### Backend
```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend
```powershell
cd frontend
npm install
npm run dev
```

Use the ports configured in the current source code if they differ from the defaults.

## Troubleshooting
If the application reports **"SAP not logged in or User cancelled the transaction"** while SAP is visibly logged in:
1. Open RZ11.
2. Check the required dynamic SAP GUI scripting parameter.
3. Confirm the parameter is set to **TRUE**.
4. Check the active SAP GUI session and whether the transaction was cancelled.
5. Escalate server-side configuration changes to SAP Basis.

If the web application is inaccessible, follow the organization's internal server/startup procedure. Do not place internal server credentials or confidential infrastructure details in this public repository.

## Security
Never commit SAP passwords, tokens, cookies, confidential exports or company/client data.

## Author
**Aditya Sarkale** — https://github.com/AdiSarkale
