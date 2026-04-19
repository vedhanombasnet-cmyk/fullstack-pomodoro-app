from flask import Flask, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

timer_running = False
paused = False
start_time = None
remaining_time = 25 * 60  # 25 minutes in seconds


@app.route("/")
def home():
    return "Pomodoro backend is running!"


@app.route("/start")
def start():
    global timer_running, paused, start_time, remaining_time
    timer_running = True
    paused = False
    remaining_time = 25 * 60
    start_time = time.time()
    return {"status": "started", "duration": remaining_time}


@app.route("/pause")
def pause():
    global paused, remaining_time, start_time, timer_running
    if timer_running and not paused:
        paused = True
        elapsed = int(time.time() - start_time)
        remaining_time -= elapsed
    return {"status": "paused", "remaining": remaining_time}


@app.route("/resume")
def resume():
    global paused, start_time, timer_running
    if timer_running and paused:
        paused = False
        start_time = time.time()
    return {"status": "resumed"}


@app.route("/stop")
def stop():
    global timer_running, paused, remaining_time
    timer_running = False
    paused = False
    remaining_time = 25 * 60
    return {"status": "stopped"}


@app.route("/status")
def status():
    global remaining_time, start_time, paused, timer_running

    if timer_running and not paused:
        elapsed = int(time.time() - start_time)
        current_remaining = remaining_time - elapsed
    else:
        current_remaining = remaining_time

    if current_remaining < 0:
        current_remaining = 0

    return {"remaining": current_remaining}


if __name__ == "__main__":
    app.run(debug=True)
