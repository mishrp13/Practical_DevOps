#!/bin/bash

# Node Health Check Script

LOG_FILE="/var/log/node_health.log"
HOSTNAME=$(hostname)
DATE=$(date "+%Y-%m-%d %H:%M:%S")

echo "========================================" >> $LOG_FILE
echo "Health Check: $DATE" >> $LOG_FILE
echo "Hostname: $HOSTNAME" >> $LOG_FILE

# CPU Usage
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}')

echo "CPU Usage: $CPU_USAGE%" >> $LOG_FILE

if (( $(echo "$CPU_USAGE > 80" | bc -l) )); then
    echo "WARNING: High CPU usage" >> $LOG_FILE
else
    echo "CPU Status: OK" >> $LOG_FILE
fi


# Memory Usage
MEM_USAGE=$(free | awk '/Mem:/ {printf "%.2f", $3/$2 * 100}')

echo "Memory Usage: $MEM_USAGE%" >> $LOG_FILE

if (( $(echo "$MEM_USAGE > 80" | bc -l) )); then
    echo "WARNING: High memory usage" >> $LOG_FILE
else
    echo "Memory Status: OK" >> $LOG_FILE
fi


# Disk Usage
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

echo "Disk Usage: $DISK_USAGE%" >> $LOG_FILE

if [ "$DISK_USAGE" -gt 80 ]; then
    echo "WARNING: High disk usage" >> $LOG_FILE
else
    echo "Disk Status: OK" >> $LOG_FILE
fi


# Check important service
SERVICE="sshd"

if systemctl is-active --quiet $SERVICE; then
    echo "$SERVICE Status: RUNNING" >> $LOG_FILE
else
    echo "WARNING: $SERVICE is NOT running" >> $LOG_FILE
fi