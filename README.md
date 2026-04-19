# Full‑Stack Pomodoro Timer

A clean, modern Pomodoro Timer built with a Flask backend and a JavaScript/HTML/CSS frontend. 
This app supports Start, Pause, Resume, and Stop, with all timing logic handled on the backend for accuracy and reliability.

This project demonstrates full‑stack engineering fundamentals:
- REST API design
- Backend state management
- Frontend–backend communication
- Asynchronous JavaScript (fetch + async/await)
- UI/UX design with modern styling
- Debugging real-world issues (CORS, async timing, state sync)

---

## Features

### Backend‑driven timer  
The countdown runs on the server, ensuring accurate timing even if the page refreshes.

### Start / Pause / Resume / Stop  
Pause and resume are true backend operations, not just visual freezes.

### Modern, clean UI  
Centered card layout, Google Fonts, and polished button styling.

### Real-time updates  
Frontend polls the backend every second for the latest remaining time.

### Connecting Frontend and Backend
Frontend and backend communicate seamlessly during local development.

---

## Tech Stack

**Frontend:**  
- HTML  
- CSS  
- JavaScript (async/await, fetch API)

**Backend:**  
- Python  
- Flask  
- Flask-CORS  

---

## Project Structure

fullstack-pomodoro-app/
│
├── backend/
│   ├── app.py
│   └── requirements.txt   (optional)
│
└── frontend/
└── index.html


---

## Running the App

### 1. Start the backend using:
```bash
cd backend
python app.py

The backend will start on
http://127.0.0.1:5000

### 2. Open the frontend

Simply open the file below in your browser:
frontend/index.html



### 3. Use the app
- Click **Start** to begin a 25‑minute session  
- Click **Pause** to freeze the timer  
- Click **Resume** to continue  
- Click **Stop** to reset back to 25:00  



## What I Learned

- How to build and structure a full‑stack application

- How to manage backend state (running, paused, resumed)

- How to use fetch()

- How to design a clean, modern UI

- How to debug frontend–backend communication

- How to think like a software engineer, not just write code

Future Improvements

- Adjustable break modes

- Sound alert when timer hits zero

- Dark mode toggle

- Session history + stats dashboar

Contact
Vedhan Basnet
vedhanombasnet@gmail.com
https://www.linkedin.com/in/vedhan-basnet/
Riverview, FL
