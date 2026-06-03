import subprocess
import sys
import os
import signal

def start_servers():
    # Define paths for backend and frontend folders
    root_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.join(root_dir, "CyberNexus_proj_Backend")
    frontend_dir = os.path.join(root_dir, "frontend", "frontend")

    print("[*] Starting VulnScope Platform...")

    # 1. Start Flask Backend
    print("[*] Launching Backend Server...")
    backend_process = subprocess.Popen(
        [sys.executable, "main.py"],
        cwd=backend_dir
    )

    # 2. Start React Frontend (Using shell=True for npm cross-platform execution)
    print("[*] Launching Frontend Development Server...")
    frontend_process = subprocess.Popen(
        "npm run dev",
        cwd=frontend_dir,
        shell=True
    )

    print("\n[+] Both servers are running successfully!")
    print("[*] Press Ctrl+C to stop both servers safely.\n")

    try:
        # Keep the script alive while both processes are running
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        # Handle graceful shutdown when user presses Ctrl+C
        print("\n[-] Shutting down both servers safely...")
        backend_process.terminate()
        frontend_process.terminate()
        print("[+] Done.")

if __name__ == "__main__":
    start_servers()