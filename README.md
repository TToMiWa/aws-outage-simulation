# 🛠️ AWS Outage Simulation — Python Resilience Lab

## 📌 Overview  
This mini-project simulates a **chaotic network environment** similar to what happens during a real-world cloud outage (e.g., an AWS region becoming unstable).  
The goal is to demonstrate **resilient client design**, using retry strategies and backoff algorithms to survive intermittent failures.

---

## 🚨 The Problem: Simulating an Unstable Service  

Real systems fail — DNS issues, regional outages, throttling, and partial service degradation.

In this lab, I simulated a failing endpoint where:

- 70% of requests **randomly fail**
- Failures include: timeouts, DNS errors, forced exceptions
- The system becomes unpredictable (“chaos mode”)

This reproduces the effect of the **2024 AWS us-east-1 partial outage**, where high error rates caused cascading failures across clients.

---

## 🧠 The Solution: Decorrelated Jitter Retry Strategy  

Instead of retrying aggressively (which makes outages *worse*), I implemented:

### **✔ Decorrelated Jitter Backoff**
A modern retry algorithm recommended by AWS and Google that:

- spreads retry load  
- prevents “retry storms”  
- avoids synchronized retries  
- increases system resilience during outages  

Formula used:
random.uniform(0, 1)


This ensures retries are:
- **randomized**  
- **non-blocking**  
- **progressively delayed**  

---

## 🧪 Features Implemented

- Simulated chaos mode (random failures)
- Retry wrapper with Decorrelated Jitter
- Terminal logs showing:
  - ❌ failures  
  - ⏳ waiting time  
  - 🔁 retries  
  - ✅ success after N attempts  
- Summary of total attempts made

Example output:
⚠️ Attempt 1 failed: ConnectionTimeout. Retrying in 2.45s...
⚠️ Attempt 2 failed: DNSResolutionError. Retrying in 1.62s...
✅ Success on attempt 3!


---

## 🗂️ Project Structure  
├── chaos_lab.py
├── README.md
└── assets/
└── architecture.png


---

## ▶️ How to Run

### **1. Clone the repo**
```bash
git clone https://github.com/<your-username>/aws-outage-simulation.git
cd aws-outage-simulation

pip install -r requirements.txt
python3 chaos_lab.py



