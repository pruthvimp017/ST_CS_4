# 🔐 Controlled Keylogger Simulation

> Application-Level Keystroke Logging Demonstration in Python  
> For Cybersecurity Learning & Defensive Analysis

---

## 📌 Project Overview

This project demonstrates a controlled implementation of a keylogging mechanism within a single Python application.

The program captures keystrokes **only inside the running terminal session** and logs them with timestamps to a local file.

⚠️ This is NOT a system-wide keylogger.  
⚠️ It does NOT monitor other applications.  
⚠️ It does NOT run in background or hidden mode.

The purpose is to understand how keylogging techniques work so they can be analyzed and defended against.

---

## 🎯 Objectives

- Understand character-level input handling
- Implement structured event logging
- Learn how keylogging mechanisms operate conceptually
- Maintain strict ethical and legal boundaries

---

## ⚙️ Technical Stack

- **Language:** Python 3
- **Modules Used:**
  - `msvcrt` (Windows key capture)
  - `datetime` (timestamp logging)

---

## 🚀 How to Run

```bash
python keylogger.py
Type inside the terminal window.

Press ESC to stop logging.

Logs are stored in keystrokes_log.txt.

📝 Log Format
Each keystroke is recorded as:

ruby
Copy code
[YYYY-MM-DD HH:MM:SS] KEY
Example:

css
Copy code
[2026-02-14 14:21:03] H
[2026-02-14 14:21:05] [SPACE]
[2026-02-14 14:21:06] W
🔒 Security Boundaries
This implementation:

✅ Operates only inside the program

✅ Requires active execution

❌ Does NOT hook OS-level keyboard events

❌ Does NOT capture browser or password input

❌ Does NOT bypass security controls

This project is built strictly for educational and defensive cybersecurity study.

📚 Learning Outcomes
Through this project, the following concepts are demonstrated:

Event-driven input capture

File I/O logging mechanisms

Timestamp-based auditing

Ethical limitations of offensive tool simulation

⚠️ Disclaimer
This project is intended for educational purposes only.
Unauthorized use of keylogging techniques may violate privacy laws and cybersecurity regulations.
