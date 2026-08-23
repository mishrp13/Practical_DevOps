PHASE 1 — Python + Linux
Day 01  Server Health Checker
Day 02  Disk Usage Monitor
Day 03  CPU/Memory Monitor
Day 04  Log Analyzer
Day 05  Automated Backup
Day 06  Log Cleanup
Day 07  Server Inventory

PHASE 2 — Automation + APIs
Day 08  Linux Service Monitor
Day 09  Process Monitor
Day 10  Port Scanner/Checker
Day 11  Website Health Checker
Day 12  REST API Client
Day 13  Git Repository Monitor
Day 14  DevOps Reporting Tool

PHASE 3 — Docker + Kubernetes
Day 15  Docker Container Monitor
Day 16  Docker Image Cleanup
Day 17  YAML Configuration Tool
Day 18  Kubernetes Pod Monitor
Day 19  Kubernetes Deployment Scaler
Day 20  Kubernetes HPA Monitor
Day 21  Kubernetes Health Dashboard

PHASE 4 — Cloud + Remote Automation
Day 22  SSH Automation
Day 23  AWS EC2 Inventory
Day 24  AWS S3 Backup
Day 25  AWS Resource Cleanup
Day 26  CI/CD Automation
Day 27  Professional Python CLI

PHASE 5 — Production Projects
Day 28  Monitoring + Alerting
Day 29  Automated Deployment System
Day 30  Complete DevOps Automation Platform

---------------------------------------------------------------------------------

1. Project Requirement
Problem statement

As a DevOps engineer, I want to automatically check the health of a Linux server and determine whether the server is healthy or unhealthy based on CPU, memory, and disk utilization.

Functional requirements

The script should:

Check CPU utilization.
Check memory utilization.
Check root disk utilization.
Check server uptime.
Compare resource usage against configurable thresholds.
Display the result on the terminal.
Write execution details to a log file.
Return an appropriate Linux exit code.


Default thresholds
Resource	Threshold
CPU	80%
Memory	80%
Disk	80%

For example:

CPU      = 45%
Memory   = 62%
Disk     = 71%


Status = HEALTHY

But:

CPU      = 91%
Memory   = 62%
Disk     = 71%


Status = UNHEALTHY
2. Project Structure

Create this:

server-health-checker/
│
├── health_checker.py
├── requirements.txt
├── README.md
│
└── logs/
    └── health.log

For this version, we don't need any external Python packages, so requirements.txt can be empty.

3. Complete Code

Create:

mkdir server-health-checker
cd server-health-checker


mkdir logs
touch health_checker.py
touch requirements.txt

Put this into health_checker.py: