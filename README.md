# VulnScope

Security platform for offensive simulation, defensive analysis, and vulnerability assessment — built for authorized testing.

## Overview
VulnScope is a unified full-stack cybersecurity platform designed to consolidate multiple security assessment domains into a single, accessible web interface. It eliminates tool fragmentation by bringing together network reconnaissance, web vulnerability scanning, packet analysis, and DoS simulation.

## Key Features
- **Network Scanning:** Multi-profile port scanner with real-time NVD/CVE correlation.
- **Web Security:** Automated SQL injection testing across multiple database engines.
- **Traffic Analysis:** Deep packet inspection and behavioral flow analysis.
- **Network Defense:** Controlled DoS simulation and defense benchmarking.
- **Social Engineering:** Semantic phishing and BEC threat detection.
- **Access Control:** Multi-signal asynchronous credential tester.

## Prerequisites
- **Python 3.10+**
- **Node.js 18+**

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/HebaZakwan/VulnScope.git](https://github.com/HebaZakwan/VulnScope.git)
   cd VulnScope
2. Install Backend Dependencies:
   ```bash
   cd CyberNexus_proj_Backend
   pip install -r requirements.txt
   cd ..
3. Install Frontend Dependencies:
   ```bash
   cd frontend
   npm install
   cd ..
4. How to Run (One-Click Start)
From the root directory of the project, simply run:
   ```bash
   python run.py
