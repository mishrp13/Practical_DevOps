PYTHON DATA STRUCTURES — 50 QUESTIONS FOR DEVOPS
SECTION 1 — LISTS (Q1-Q15)

Q1: What is a List and how is it used in DevOps?

python
# List = ordered, mutable, allows duplicates
# Most used data structure in DevOps

# DevOps use cases:
servers = ['web-01', 'web-02', 'db-01', 'cache-01']
failed_services = ['nginx', 'mysql', 'redis']
port_numbers = [80, 443, 3306, 6379, 22]

# Key properties:
# ✅ Ordered (maintains insertion order)
# ✅ Mutable (can change after creation)
# ✅ Allows duplicates
# ✅ Indexed (start from 0)

print(servers[0])      # web-01 (first)
print(servers[-1])     # cache-01 (last)
print(servers[1:3])    # ['web-02', 'db-01'] (slice)
print(len(servers))    # 4

Q2: How do you add and remove elements from a list?

python
# Adding elements
servers = ['web-01', 'web-02']

# append() - add to end
servers.append('web-03')
print(servers)  # ['web-01', 'web-02', 'web-03']

# insert() - add at specific position
servers.insert(0, 'load-balancer')
print(servers)  # ['load-balancer', 'web-01', 'web-02', 'web-03']

# extend() - add multiple items
new_servers = ['db-01', 'db-02']
servers.extend(new_servers)
print(servers)  # all 6 servers

# Removing elements
servers.remove('web-03')    # Remove by value
popped = servers.pop()      # Remove last, returns it
popped_idx = servers.pop(0) # Remove at index 0
del servers[0]              # Delete at index

# DevOps scenario:
# Monitor server list and remove failed ones
active_servers = ['web-01', 'web-02', 'web-03', 'db-01']
failed = 'web-02'

if failed in active_servers:
    active_servers.remove(failed)
    print(f"Removed {failed}. Active: {active_servers}")

Q3: How do you sort a list of servers by name and by number?

python
# Sorting server lists
servers = ['web-03', 'web-01', 'db-02', 'web-02', 'db-01']

# Sort alphabetically (in place)
servers.sort()
print(servers)
# ['db-01', 'db-02', 'web-01', 'web-02', 'web-03']

# Sort - new list (original unchanged)
sorted_servers = sorted(servers)

# Sort reverse
servers.sort(reverse=True)

# Sort by custom key
server_data = [
    {'name': 'web-03', 'cpu': 85},
    {'name': 'web-01', 'cpu': 45},
    {'name': 'db-01', 'cpu': 92},
]

# Sort by CPU usage (highest first)
sorted_by_cpu = sorted(
    server_data,
    key=lambda x: x['cpu'],
    reverse=True
)

for server in sorted_by_cpu:
    print(f"{server['name']}: {server['cpu']}%")
# db-01: 92%
# web-03: 85%
# web-01: 45%

# Sort by multiple keys
deployments = [
    ('prod', 'web-01', 3),
    ('dev', 'web-02', 1),
    ('prod', 'db-01', 5),
    ('dev', 'web-01', 2),
]

# Sort by environment then by priority
sorted_deps = sorted(
    deployments,
    key=lambda x: (x[0], x[2])
)
print(sorted_deps)

Q4: Write a DevOps script to find servers with high CPU usage from a list

python
# Real DevOps scenario: Find high CPU servers

server_metrics = [
    ('web-01', 45.2),
    ('web-02', 87.5),
    ('db-01', 92.1),
    ('cache-01', 23.4),
    ('web-03', 78.9),
    ('db-02', 95.3),
]

# Method 1: Traditional loop
def find_high_cpu_servers(metrics, threshold=80):
    high_cpu = []
    for server, cpu in metrics:
        if cpu > threshold:
            high_cpu.append(server)
    return high_cpu

# Method 2: List comprehension (Pythonic)
threshold = 80
high_cpu_servers = [
    server
    for server, cpu in server_metrics
    if cpu > threshold
]

print(f"High CPU servers: {high_cpu_servers}")
# High CPU servers: ['web-02', 'db-01', 'db-02']

# Method 3: With details
critical_servers = [
    {'server': server, 'cpu': cpu, 'status': 'CRITICAL'}
    for server, cpu in server_metrics
    if cpu > threshold
]

for s in critical_servers:
    print(f"🔴 {s['server']}: {s['cpu']}% CPU")

# Method 4: Filter function
high_cpu = list(filter(
    lambda x: x[1] > threshold,
    server_metrics
))
print(high_cpu)

Q5: How do you remove duplicates from a list while maintaining order?

python
# DevOps scenario: Remove duplicate log entries
# or duplicate server names

log_events = [
    'ERROR: disk full',
    'INFO: service started',
    'ERROR: disk full',      # duplicate
    'WARNING: high CPU',
    'INFO: service started', # duplicate
    'ERROR: connection lost',
]

# Method 1: Using dict.fromkeys (maintains order)
unique_events = list(dict.fromkeys(log_events))
print("Unique events:")
for event in unique_events:
    print(f"  {event}")

# Method 2: Using set (does NOT maintain order)
unique_unordered = list(set(log_events))

# Method 3: Manual with seen set (maintains order)
def remove_duplicates_ordered(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

servers = ['web-01', 'db-01', 'web-01', 'web-02', 'db-01']
unique_servers = remove_duplicates_ordered(servers)
print(unique_servers)
# ['web-01', 'db-01', 'web-02']

# Count duplicates too
from collections import Counter
event_counts = Counter(log_events)
for event, count in event_counts.most_common():
    if count > 1:
        print(f"Duplicate ({count}x): {event}")

Q6: How do you flatten a nested list of server groups?

python
# DevOps scenario: Flatten grouped server lists

server_groups = [
    ['web-01', 'web-02', 'web-03'],
    ['db-01', 'db-02'],
    ['cache-01'],
    ['lb-01', 'lb-02'],
]

# Method 1: List comprehension
all_servers = [
    server
    for group in server_groups
    for server in group
]
print(all_servers)
# ['web-01', 'web-02', 'web-03', 'db-01', ...]

# Method 2: itertools.chain
import itertools
all_servers = list(itertools.chain.from_iterable(server_groups))

# Method 3: sum() trick
all_servers = sum(server_groups, [])

# Real scenario: Flatten multi-region server groups
regions = {
    'us-east': ['web-01', 'web-02'],
    'us-west': ['web-03', 'web-04'],
    'eu-west': ['web-05', 'web-06'],
}

all_regional_servers = [
    server
    for region_servers in regions.values()
    for server in region_servers
]
print(f"Total servers: {len(all_regional_servers)}")
print(all_regional_servers)

# Deep flatten (multiple levels)
def deep_flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

nested = ['web-01', ['db-01', ['cache-01', 'cache-02']], 'lb-01']
print(deep_flatten(nested))
# ['web-01', 'db-01', 'cache-01', 'cache-02', 'lb-01']

Q7: Write a script to chunk a list for batch processing

python
# DevOps scenario: Process 1000 servers in batches of 50
# Deploy to servers in controlled batches

def chunk_list(lst, chunk_size):
    """Split list into chunks of specified size"""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

# Generate test server list
all_servers = [f'server-{i:03d}' for i in range(1, 101)]

# Process in batches of 10
batch_size = 10
for batch_num, batch in enumerate(chunk_list(all_servers, batch_size), 1):
    print(f"Batch {batch_num}: {batch}")
    # Simulate deployment
    # deploy_to_servers(batch)

# Real deployment scenario
def rolling_deploy(servers, patch_version, batch_size=5):
    """Deploy patch to servers in rolling batches"""
    total_batches = (len(servers) + batch_size - 1) // batch_size
    failed_servers = []

    for batch_num, batch in enumerate(chunk_list(servers, batch_size), 1):
        print(f"\n[Batch {batch_num}/{total_batches}] Deploying {patch_version}")
        print(f"  Servers: {batch}")

        for server in batch:
            # Simulate deployment
            success = True  # Replace with actual deploy logic
            if success:
                print(f"  ✅ {server}: Deployed successfully")
            else:
                print(f"  ❌ {server}: Deployment failed")
                failed_servers.append(server)

    if failed_servers:
        print(f"\n⚠️ Failed servers: {failed_servers}")
    else:
        print(f"\n✅ All servers updated to {patch_version}")

    return failed_servers

# Run
servers = [f'web-{i:02d}' for i in range(1, 21)]
rolling_deploy(servers, 'v2.4.1', batch_size=5)

Q8: How do you use list comprehensions for log processing?

python
# List comprehensions - most Pythonic way
# Critical for DevOps log processing

# Sample log file content
logs = [
    "2024-01-15 ERROR web-01 Disk full: 98% used",
    "2024-01-15 INFO web-02 Service started successfully",
    "2024-01-15 ERROR db-01 Connection timeout after 30s",
    "2024-01-15 WARNING web-03 CPU usage 85%",
    "2024-01-15 ERROR cache-01 Out of memory",
    "2024-01-15 INFO lb-01 Health check passed",
    "2024-01-15 CRITICAL db-02 Database crashed",
]

# 1. Extract only ERROR logs
error_logs = [log for log in logs if 'ERROR' in log]
print("ERROR logs:", error_logs)

# 2. Extract server names from error logs
error_servers = [
    log.split()[2]
    for log in logs
    if 'ERROR' in log or 'CRITICAL' in log
]
print("Servers with issues:", error_servers)

# 3. Convert logs to dictionaries
def parse_log(log_line):
    parts = log_line.split(maxsplit=4)
    return {
        'date': parts[0],
        'time': parts[1] if len(parts) > 1 else '',
        'level': parts[2] if len(parts) > 2 else '',
        'server': parts[3] if len(parts) > 3 else '',
        'message': parts[4] if len(parts) > 4 else ''
    }

# Wait - our log format is different, let's fix:
logs_v2 = [
    "ERROR web-01 Disk full: 98% used",
    "INFO web-02 Service started",
    "ERROR db-01 Connection timeout",
]

parsed_logs = [
    {
        'level': log.split()[0],
        'server': log.split()[1],
        'message': ' '.join(log.split()[2:])
    }
    for log in logs_v2
]

# 4. Nested list comprehension - get all IPs
ip_ranges = ['192.168.1', '10.0.0', '172.16.0']
all_ips = [
    f'{range}.{host}'
    for range in ip_ranges
    for host in range(1, 5)
]
print(all_ips[:6])

# 5. Conditional expression in comprehension
server_status = [
    f"{server}: {'🔴 HIGH' if cpu > 80 else '🟡 MEDIUM' if cpu > 60 else '🟢 NORMAL'}"
    for server, cpu in [('web-01', 45), ('web-02', 87), ('db-01', 65)]
]
for status in server_status:
    print(status)

Q9: How do you search and filter a list of dictionaries?

python
# Very common in DevOps — list of server configs, 
# deployment records, monitoring data

server_inventory = [
    {'name': 'web-01', 'env': 'prod', 'cpu': 45, 'region': 'us-east', 'os': 'ubuntu'},
    {'name': 'web-02', 'env': 'prod', 'cpu': 87, 'region': 'us-east', 'os': 'ubuntu'},
    {'name': 'db-01',  'env': 'prod', 'cpu': 92, 'region': 'us-west', 'os': 'rhel'},
    {'name': 'web-03', 'env': 'dev',  'cpu': 23, 'region': 'us-east', 'os': 'ubuntu'},
    {'name': 'cache-01','env':'prod', 'cpu': 34, 'region': 'eu-west', 'os': 'ubuntu'},
    {'name': 'db-02',  'env': 'dev',  'cpu': 56, 'region': 'us-west', 'os': 'rhel'},
]

# 1. Filter prod servers
prod_servers = [s for s in server_inventory if s['env'] == 'prod']
print(f"Prod servers: {[s['name'] for s in prod_servers]}")

# 2. Filter high CPU prod servers
critical_prod = [
    s for s in server_inventory
    if s['env'] == 'prod' and s['cpu'] > 80
]
print(f"Critical prod: {[s['name'] for s in critical_prod]}")

# 3. Find server by name
def find_server(inventory, name):
    return next(
        (s for s in inventory if s['name'] == name),
        None  # default if not found
    )

server = find_server(server_inventory, 'db-01')
print(f"Found: {server}")

# 4. Filter with multiple conditions
def filter_servers(inventory, **criteria):
    """Filter servers by any combination of criteria"""
    result = inventory
    for key, value in criteria.items():
        result = [s for s in result if s.get(key) == value]
    return result

ubuntu_prod = filter_servers(
    server_inventory,
    env='prod',
    os='ubuntu'
)
print(f"Ubuntu prod: {[s['name'] for s in ubuntu_prod]}")

# 5. Group by environment
from collections import defaultdict

by_env = defaultdict(list)
for server in server_inventory:
    by_env[server['env']].append(server['name'])

for env, servers in by_env.items():
    print(f"{env}: {servers}")

Q10: Write a script to compare two server lists (diff, intersection, new servers)

python
# DevOps scenario: Compare expected vs actual servers
# Find new servers, removed servers, unchanged

expected_servers = [
    'web-01', 'web-02', 'web-03',
    'db-01', 'db-02',
    'cache-01', 'lb-01'
]

actual_servers = [
    'web-01', 'web-02', 'web-04',  # web-03 gone, web-04 new
    'db-01',                        # db-02 gone
    'cache-01', 'cache-02',         # cache-02 new
    'lb-01', 'lb-02'               # lb-02 new
]

# Convert to sets for comparison
expected_set = set(expected_servers)
actual_set = set(actual_servers)

# New servers (in actual but not expected)
new_servers = list(actual_set - expected_set)

# Removed servers (in expected but not actual)
removed_servers = list(expected_set - actual_set)

# Unchanged servers
unchanged = list(expected_set & actual_set)

# All servers (union)
all_servers = list(expected_set | actual_set)

print("=" * 40)
print("SERVER INVENTORY COMPARISON")
print("=" * 40)
print(f"✅ Unchanged ({len(unchanged)}): {sorted(unchanged)}")
print(f"🆕 New servers ({len(new_servers)}): {sorted(new_servers)}")
print(f"❌ Removed ({len(removed_servers)}): {sorted(removed_servers)}")
print(f"📊 Total expected: {len(expected_servers)}")
print(f"📊 Total actual: {len(actual_servers)}")

# Generate change report
def generate_change_report(expected, actual):
    exp_set = set(expected)
    act_set = set(actual)
    
    return {
        'added': sorted(act_set - exp_set),
        'removed': sorted(exp_set - act_set),
        'unchanged': sorted(exp_set & act_set),
        'change_count': len(act_set - exp_set) + len(exp_set - act_set)
    }

report = generate_change_report(expected_servers, actual_servers)
print(f"\nTotal changes: {report['change_count']}")

Q11: How do you use map(), filter(), reduce() with lists?

python
from functools import reduce

# Server data for examples
servers = ['web-01', 'web-02', 'db-01', 'cache-01']
cpu_usage = [45.2, 87.5, 92.1, 23.4]

# MAP - Apply function to every element
# Convert all server names to uppercase
upper_servers = list(map(str.upper, servers))
print(upper_servers)
# ['WEB-01', 'WEB-02', 'DB-01', 'CACHE-01']

# Add domain suffix to servers
with_domain = list(map(
    lambda s: f"{s}.company.com",
    servers
))
print(with_domain)
# ['web-01.company.com', ...]

# Round CPU values
rounded_cpu = list(map(lambda x: round(x), cpu_usage))
print(rounded_cpu)  # [45, 88, 92, 23]

# FILTER - Keep elements matching condition
high_cpu_vals = list(filter(lambda x: x > 80, cpu_usage))
print(f"High CPU values: {high_cpu_vals}")

prod_servers = list(filter(
    lambda s: s.startswith('web'),
    servers
))
print(f"Web servers: {prod_servers}")

# REDUCE - Combine all elements into one
total_cpu = reduce(lambda acc, x: acc + x, cpu_usage)
print(f"Total CPU: {total_cpu:.1f}%")

max_cpu = reduce(lambda a, b: a if a > b else b, cpu_usage)
print(f"Max CPU: {max_cpu}%")

# Combine: Find average CPU of web servers
server_cpu = list(zip(servers, cpu_usage))

web_cpu = list(filter(
    lambda x: x[0].startswith('web'),
    server_cpu
))

web_cpu_values = list(map(lambda x: x[1], web_cpu))
avg_web_cpu = reduce(lambda a, b: a + b, web_cpu_values) / len(web_cpu_values)

print(f"Average web server CPU: {avg_web_cpu:.1f}%")

Q12: How do you zip and enumerate lists in DevOps scripts?

python
# zip() and enumerate() - essential DevOps tools

servers = ['web-01', 'web-02', 'db-01', 'cache-01']
ip_addresses = ['10.0.1.10', '10.0.1.11', '10.0.2.10', '10.0.3.10']
cpu_usage = [45.2, 87.5, 92.1, 23.4]
memory_gb = [8, 16, 32, 8]

# ENUMERATE - index + value
print("Server inventory:")
for idx, server in enumerate(servers, start=1):
    print(f"  {idx}. {server}")

# ZIP - pair multiple lists
server_ips = list(zip(servers, ip_addresses))
print("\nServer → IP mapping:")
for server, ip in server_ips:
    print(f"  {server}: {ip}")

# ZIP three lists
for server, cpu, mem in zip(servers, cpu_usage, memory_gb):
    status = "🔴" if cpu > 80 else "🟢"
    print(f"{status} {server}: CPU={cpu}%, RAM={mem}GB")

# Create dict from two lists
server_ip_dict = dict(zip(servers, ip_addresses))
print(server_ip_dict)

# Enumerate + zip together
for i, (server, ip, cpu) in enumerate(
    zip(servers, ip_addresses, cpu_usage), 1
):
    print(f"{i}. {server} ({ip}): {cpu}% CPU")

# zip_longest - when lists have different lengths
from itertools import zip_longest

servers_ext = ['web-01', 'web-02', 'web-03']
ips_short = ['10.0.1.10', '10.0.1.11']

for server, ip in zip_longest(
    servers_ext, ips_short,
    fillvalue='TBD'
):
    print(f"{server}: {ip}")

Q13: How do you use list as a stack and queue?

python
# Stacks and Queues — used in deployment pipelines,
# job queues, undo operations

# LIST AS STACK (LIFO — Last In First Out)
# Use for: Undo operations, DFS traversal, 
#          parsing configs

deployment_stack = []

# Push operations (append)
deployment_stack.append('Deploy v1.0')
deployment_stack.append('Deploy v1.1')
deployment_stack.append('Deploy v1.2')

print("Deployment history:", deployment_stack)

# Pop - undo last deployment
last_deployment = deployment_stack.pop()
print(f"Rolled back: {last_deployment}")
print("Current state:", deployment_stack)

# Peek - see last without removing
top = deployment_stack[-1] if deployment_stack else None
print(f"Latest deployment: {top}")

# LIST AS QUEUE (FIFO — First In First Out)
# NOT efficient with regular list (use deque)
# Use deque for proper queue

from collections import deque

# Job queue for deployment pipeline
job_queue = deque()

# Enqueue jobs
job_queue.append('Build Docker image')
job_queue.append('Run unit tests')
job_queue.append('Push to registry')
job_queue.append('Deploy to staging')
job_queue.append('Run integration tests')
job_queue.append('Deploy to production')

print(f"\nJob queue ({len(job_queue)} jobs):")
while job_queue:
    job = job_queue.popleft()  # dequeue from left
    print(f"  Processing: {job}")

# Priority queue for critical deployments
import heapq

# (priority, job_name) — lower number = higher priority
job_heap = []
heapq.heappush(job_heap, (3, 'Deploy feature-X'))
heapq.heappush(job_heap, (1, 'HOTFIX: Critical bug'))
heapq.heappush(job_heap, (2, 'Deploy feature-Y'))

print("\nPriority job queue:")
while job_heap:
    priority, job = heapq.heappop(job_heap)
    print(f"  Priority {priority}: {job}")

Q14: Write a script to monitor and update a list of running processes

python
import subprocess
import time

def get_running_processes_mock():
    """Mock process list (use subprocess in real world)"""
    return [
        {'pid': 1234, 'name': 'nginx', 'cpu': 2.1, 'mem': 1.5},
        {'pid': 5678, 'name': 'mysql', 'cpu': 45.2, 'mem': 23.4},
        {'pid': 9012, 'name': 'redis', 'cpu': 1.2, 'mem': 2.1},
        {'pid': 3456, 'name': 'python', 'cpu': 87.5, 'mem': 15.3},
        {'pid': 7890, 'name': 'java', 'cpu': 92.1, 'mem': 45.6},
    ]

# Process list operations
processes = get_running_processes_mock()

# 1. Find high CPU processes
high_cpu = [p for p in processes if p['cpu'] > 80]
print("High CPU processes:")
for p in high_cpu:
    print(f"  PID {p['pid']}: {p['name']} - {p['cpu']}% CPU")

# 2. Sort by CPU usage
sorted_by_cpu = sorted(
    processes,
    key=lambda p: p['cpu'],
    reverse=True
)
print("\nTop 3 CPU consumers:")
for p in sorted_by_cpu[:3]:
    print(f"  {p['name']}: {p['cpu']}%")

# 3. Get process names list
process_names = [p['name'] for p in processes]
print(f"\nRunning: {process_names}")

# 4. Check if critical service is running
critical_services = ['nginx', 'mysql', 'redis']
running_names = set(process_names)

for service in critical_services:
    status = "✅ Running" if service in running_names else "❌ DOWN!"
    print(f"{service}: {status}")

# 5. Remove process from list (simulate kill)
def remove_process(proc_list, pid):
    return [p for p in proc_list if p['pid'] != pid]

processes = remove_process(processes, 7890)
print(f"\nAfter killing PID 7890: {len(processes)} processes")

# 6. Update process CPU (simulate monitoring update)
def update_cpu(proc_list, pid, new_cpu):
    return [
        {**p, 'cpu': new_cpu} if p['pid'] == pid else p
        for p in proc_list
    ]

processes = update_cpu(processes, 5678, 12.3)
mysql = next(p for p in processes if p['name'] == 'mysql')
print(f"MySQL CPU after update: {mysql['cpu']}%")

Q15: How do you use list slicing for log rotation?

python
# Log rotation, recent logs, sliding window

# Simulate a growing log list
def add_log(logs, message, max_size=10):
    """Add log entry and maintain max size (log rotation)"""
    logs.append(message)
    if len(logs) > max_size:
        logs = logs[-max_size:]  # Keep only last N logs
    return logs

# Slicing operations for logs
all_logs = [
    f"Log entry {i:03d}" for i in range(1, 51)
]

# Last 10 logs
recent_logs = all_logs[-10:]
print("Recent logs:", recent_logs)

# First 5 logs (oldest)
oldest_logs = all_logs[:5]

# Every other log
every_other = all_logs[::2]

# Reverse order (newest first)
newest_first = all_logs[::-1]

# Sliding window for anomaly detection
def check_error_spike(logs, window_size=5, threshold=3):
    """Check if errors spiked in recent window"""
    recent_window = logs[-window_size:]
    error_count = sum(1 for log in recent_window if 'ERROR' in log)

    if error_count >= threshold:
        print(f"⚠️ ALERT: {error_count} errors in last {window_size} logs!")
        return True
    return False

# Test logs with errors
test_logs = [
    'INFO: Started',
    'ERROR: Disk full',
    'ERROR: Connection lost',
    'ERROR: Service crash',
    'ERROR: Memory exceeded',
    'INFO: Recovered',
]

check_error_spike(test_logs, window_size=5, threshold=3)

# Split logs by time window
def split_by_batch(logs, batch_size):
    """Get logs in time windows"""
    return [logs[i:i+batch_size] for i in range(0, len(logs), batch_size)]

hourly_logs = split_by_batch(all_logs, 10)
print(f"\n{len(hourly_logs)} hourly batches")
for i, batch in enumerate(hourly_logs, 1):
    print(f"Hour {i}: {len(batch)} logs")
SECTION 2 — TUPLES (Q16-Q25)

Q16: What is a Tuple and how is it used in DevOps?

python
# Tuple = ordered, IMMUTABLE, allows duplicates
# Use when data should NOT change

# DevOps use cases:
SERVER_PORTS = (22, 80, 443, 3306, 6379)  # Constants
DB_CREDENTIALS = ('admin', 'pass123', 'mydb')  # Config
SERVER_CONFIG = ('web-01', '10.0.1.10', 'prod')

# Key properties:
# ✅ Ordered
# ✅ Immutable (cannot change after creation)  
# ✅ Faster than lists
# ✅ Can be used as dictionary key
# ✅ Good for fixed configuration

# Accessing
server, ip, env = SERVER_CONFIG  # Unpacking
print(f"Server: {server}, IP: {ip}, Env: {env}")

# Named tuples - better readability
from collections import namedtuple

Server = namedtuple('Server', ['name', 'ip', 'env', 'port'])

web01 = Server('web-01', '10.0.1.10', 'prod', 80)
print(f"Server: {web01.name}")
print(f"IP: {web01.ip}")
print(f"Port: {web01.port}")

# List of named tuples
servers = [
    Server('web-01', '10.0.1.10', 'prod', 80),
    Server('web-02', '10.0.1.11', 'prod', 80),
    Server('db-01', '10.0.2.10', 'prod', 3306),
]

prod_web = [s for s in servers if s.env == 'prod' and s.port == 80]
print(f"Prod web servers: {[s.name for s in prod_web]}")

Q17: How do you use tuples as dictionary keys for server configuration?

python
# Tuples as dict keys - powerful for composite keys
# Lists CANNOT be dict keys (mutable)
# Tuples CAN be dict keys (immutable)

# Server performance tracking by (server, date)
performance_data = {
    ('web-01', '2024-01-15'): {'avg_cpu': 45.2, 'avg_mem': 67.3},
    ('web-01', '2024-01-16'): {'avg_cpu': 87.5, 'avg_mem': 72.1},
    ('db-01',  '2024-01-15'): {'avg_cpu': 92.1, 'avg_mem': 89.4},
    ('db-01',  '2024-01-16'): {'avg_cpu': 45.3, 'avg_mem': 78.2},
}

# Query specific server+date
key = ('web-01', '2024-01-16')
data = performance_data.get(key, {})
print(f"web-01 on 2024-01-16: {data}")

# Find high CPU days for web-01
web01_high_cpu = {
    date: metrics
    for (server, date), metrics in performance_data.items()
    if server == 'web-01' and metrics['avg_cpu'] > 80
}
print(f"web-01 high CPU days: {web01_high_cpu}")

# Network route mapping
# (source_region, dest_region) -> route info
routes = {
    ('us-east', 'us-west'): {'latency_ms': 45, 'bandwidth': '10Gbps'},
    ('us-east', 'eu-west'): {'latency_ms': 120, 'bandwidth': '5Gbps'},
    ('us-west', 'ap-east'): {'latency_ms': 150, 'bandwidth': '5Gbps'},
}

# Find route
def get_route(src, dst):
    return routes.get((src, dst)) or routes.get((dst, src))

route = get_route('us-east', 'eu-west')
print(f"Route latency: {route['latency_ms']}ms")

Q18: What is tuple unpacking and how is it useful in DevOps?

python
# Tuple unpacking - very Pythonic, widely used

# Basic unpacking
server_info = ('web-01', '10.0.1.10', 8080, 'prod')
name, ip, port, env = server_info

print(f"Deploying to {name} ({ip}:{port}) in {env}")

# Swap values without temp variable
primary_db = 'db-01'
secondary_db = 'db-02'
primary_db, secondary_db = secondary_db, primary_db
print(f"After failover: Primary={primary_db}, Secondary={secondary_db}")

# Extended unpacking with *
first_server, *middle_servers, last_server = [
    'web-01', 'web-02', 'web-03', 'web-04', 'web-05'
]
print(f"First: {first_server}")
print(f"Middle: {middle_servers}")
print(f"Last: {last_server}")

# Ignore values with _
server_name, _, _, environment = server_info
print(f"Name: {server_name}, Env: {environment}")

# Function returning multiple values (returns tuple)
def get_server_stats(server_name):
    # Simulate getting stats
    return server_name, 45.2, 67.3, 'healthy'

name, cpu, mem, status = get_server_stats('web-01')
print(f"{name}: CPU={cpu}%, Mem={mem}%, Status={status}")

# Unpacking in loops
server_data = [
    ('web-01', '10.0.1.10', 80),
    ('web-02', '10.0.1.11', 80),
    ('db-01',  '10.0.2.10', 3306),
]

for name, ip, port in server_data:
    print(f"Checking {name} at {ip}:{port}")

Q19: Write a DevOps script using tuples for immutable configuration

python
# Using tuples for configuration constants
# Prevents accidental modification

from collections import namedtuple
from typing import Tuple

# Environment configurations as tuples
EnvConfig = namedtuple('EnvConfig', [
    'name', 'db_host', 'db_port',
    'redis_host', 'replicas', 'debug'
])

ENVIRONMENTS = {
    'dev': EnvConfig(
        name='development',
        db_host='localhost',
        db_port=5432,
        redis_host='localhost',
        replicas=1,
        debug=True
    ),
    'staging': EnvConfig(
        name='staging',
        db_host='staging-db.internal',
        db_port=5432,
        redis_host='staging-redis.internal',
        replicas=2,
        debug=True
    ),
    'prod': EnvConfig(
        name='production',
        db_host='prod-db.internal',
        db_port=5432,
        redis_host='prod-redis.internal',
        replicas=5,
        debug=False
    ),
}

# Immutable port definitions
ALLOWED_PORTS: Tuple[int, ...] = (22, 80, 443, 8080, 8443)
CRITICAL_PORTS: Tuple[int, ...] = (22, 443)
DB_PORTS: Tuple[int, ...] = (3306, 5432, 1521, 27017)

def validate_port(port: int) -> bool:
    return port in ALLOWED_PORTS

def deploy_to_env(environment: str):
    config = ENVIRONMENTS.get(environment)
    if not config:
        raise ValueError(f"Unknown environment: {environment}")

    print(f"Deploying to {config.name}")
    print(f"  DB: {config.db_host}:{config.db_port}")
    print(f"  Redis: {config.redis_host}")
    print(f"  Replicas: {config.replicas}")
    print(f"  Debug mode: {config.debug}")

    return config

config = deploy_to_env('prod')
print(f"\nReplicas to spin up: {config.replicas}")

# Tuple for version info
VERSION = (2, 4, 1, 'stable')
MAJOR, MINOR, PATCH, STAGE = VERSION
print(f"\nApp version: {MAJOR}.{MINOR}.{PATCH}-{STAGE}")

Q20: How do you convert between lists and tuples?

python
# Conversion between list and tuple
# Important when you need to switch mutability

# List to Tuple (make immutable)
server_list = ['web-01', 'web-02', 'db-01']
server_tuple = tuple(server_list)
print(f"Tuple: {server_tuple}")

# Tuple to List (make mutable)
ALLOWED_PORTS = (22, 80, 443)
ports_list = list(ALLOWED_PORTS)
ports_list.append(8080)  # Can now modify
ALLOWED_PORTS = tuple(ports_list)  # Convert back
print(f"Updated ports: {ALLOWED_PORTS}")

# Real scenario: Config loaded from file (tuple for safety)
def load_server_config():
    """Load config - return as tuple for immutability"""
    raw_config = ['web-01', 'web-02', 'db-01']  # From file
    return tuple(raw_config)  # Return immutable

# When you need to modify config
config = load_server_config()
# config.append('web-03')  # Would ERROR - tuple is immutable

# Correct way - convert, modify, convert back
config_list = list(config)
config_list.append('web-03')
config = tuple(config_list)
print(f"Updated config: {config}")

# Tuple of lists (mixed)
server_groups = (
    ['web-01', 'web-02'],  # Web tier (list - can modify)
    ['db-01', 'db-02'],    # DB tier
    ['cache-01'],          # Cache tier
)

# Can modify the lists inside
server_groups[0].append('web-03')
print(f"Web tier: {server_groups[0]}")
# But cannot reassign the tuple elements
# server_groups[0] = ['new-list']  # ERROR

Q21-Q25: Tuple Quick Practice Questions

python
# Q21: Zip two lists into list of tuples
servers = ['web-01', 'web-02', 'db-01']
ips = ['10.0.1.10', '10.0.1.11', '10.0.2.10']
server_ip_pairs = list(zip(servers, ips))
print(server_ip_pairs)
# [('web-01', '10.0.1.10'), ('web-02', '10.0.1.11'), ...]

# Q22: Unzip list of tuples back to lists
servers_back, ips_back = zip(*server_ip_pairs)
print(list(servers_back))
print(list(ips_back))

# Q23: Find max/min from tuple
response_times = (120, 45, 890, 23, 456, 67)
print(f"Max response: {max(response_times)}ms")
print(f"Min response: {min(response_times)}ms")
print(f"Avg response: {sum(response_times)/len(response_times):.1f}ms")

# Q24: Count occurrences in tuple
statuses = ('UP', 'DOWN', 'UP', 'UP', 'DOWN', 'UP')
up_count = statuses.count('UP')
down_count = statuses.count('DOWN')
print(f"UP: {up_count}, DOWN: {down_count}")
uptime_pct = (up_count / len(statuses)) * 100
print(f"Uptime: {uptime_pct:.1f}%")

# Q25: Tuple as function arguments (*args)
def deploy_servers(*servers, environment='prod'):
    """Deploy to multiple servers using tuple unpacking"""
    print(f"Deploying to {environment}:")
    for server in servers:
        print(f"  ✅ {server}")

deploy_servers('web-01', 'web-02', 'web-03', environment='prod')

# Unpack tuple as function arguments
server_list = ('db-01', 'db-02')
deploy_servers(*server_list, environment='staging')
SECTION 3 — SETS (Q26-Q35)

Q26: What is a Set and how is it used in DevOps?

python
# Set = unordered, mutable, NO duplicates
# Use for: unique items, membership testing,
#          set operations (union, intersection, difference)

# DevOps use cases
running_servers = {'web-01', 'web-02', 'db-01', 'cache-01'}
expected_servers = {'web-01', 'web-02', 'web-03', 'db-01', 'db-02'}

# Key properties:
# ✅ No duplicates automatically
# ✅ Fast membership testing O(1)
# ✅ Set operations (union, intersection)
# ❌ Unordered (no indexing)
# ❌ Elements must be hashable

# Create set from list (removes duplicates)
server_list = ['web-01', 'web-01', 'web-02', 'db-01', 'web-02']
unique_servers = set(server_list)
print(f"Unique servers: {unique_servers}")

# Fast membership check
if 'web-01' in running_servers:
    print("web-01 is running")

# Much faster than list for large datasets
import time
large_set = set(range(1000000))
large_list = list(range(1000000))

# Set lookup: O(1) - constant time
start = time.time()
_ = 999999 in large_set
set_time = time.time() - start

# List lookup: O(n) - linear time
start = time.time()
_ = 999999 in large_list
list_time = time.time() - start

print(f"Set lookup: {set_time:.6f}s")
print(f"List lookup: {list_time:.6f}s")

Q27: How do you use set operations for server management?

python
# Set operations — most powerful feature of sets

expected = {'web-01', 'web-02', 'web-03', 'db-01', 'db-02', 'cache-01'}
running = {'web-01', 'web-02', 'db-01', 'cache-01', 'web-04'}

# UNION - all servers from both sets (|)
all_known = expected | running
# Or: expected.union(running)
print(f"All known servers: {all_known}")

# INTERSECTION - servers in BOTH sets (&)
working_as_expected = expected & running
# Or: expected.intersection(running)
print(f"Running as expected: {working_as_expected}")

# DIFFERENCE - in expected but NOT in running (-)
down_servers = expected - running
# Or: expected.difference(running)
print(f"🔴 DOWN servers: {down_servers}")

# Unexpected running servers
unexpected_running = running - expected
print(f"⚠️ Unexpected servers: {unexpected_running}")

# SYMMETRIC DIFFERENCE - in either but not both (^)
discrepancies = expected ^ running
print(f"All discrepancies: {discrepancies}")

# Real DevOps monitoring
def check_server_health(expected_servers, actual_servers):
    exp = set(expected_servers)
    act = set(actual_servers)

    report = {
        'healthy': exp & act,          # Running as expected
        'down': exp - act,             # Expected but not running
        'unexpected': act - exp,       # Running but not expected
        'total_expected': len(exp),
        'total_running': len(act),
    }

    health_pct = len(report['healthy']) / len(exp) * 100

    print(f"\nCluster Health Report")
    print(f"{'='*40}")
    print(f"Health: {health_pct:.1f}%")
    print(f"✅ Healthy: {sorted(report['healthy'])}")
    print(f"❌ Down: {sorted(report['down'])}")
    print(f"⚠️ Unexpected: {sorted(report['unexpected'])}")

    return report

check_server_health(expected, running)

Q28: Write a script to find common packages across multiple servers

python
# Real DevOps scenario: Package audit across servers

server_packages = {
    'web-01': {'nginx', 'python3', 'curl', 'git', 'vim', 'htop'},
    'web-02': {'nginx', 'python3', 'curl', 'git', 'nmap'},
    'db-01':  {'mysql', 'python3', 'curl', 'git', 'vim', 'percona-toolkit'},
    'db-02':  {'mysql', 'python3', 'curl', 'vim', 'percona-toolkit'},
    'cache-01': {'redis', 'python3', 'curl', 'git'},
}

# Packages on ALL servers (intersection of all)
all_package_sets = list(server_packages.values())
common_all = all_package_sets[0]
for packages in all_package_sets[1:]:
    common_all = common_all & packages

print(f"Packages on ALL servers: {common_all}")

# Packages on ANY server (union)
all_packages = set()
for packages in server_packages.values():
    all_packages |= packages
print(f"Total unique packages: {len(all_packages)}")
print(f"All packages: {sorted(all_packages)}")

# Packages only on specific server (unique to that server)
for server, packages in server_packages.items():
    other_packages = set()
    for other_server, other_pkgs in server_packages.items():
        if other_server != server:
            other_packages |= other_pkgs

    unique_to_server = packages - other_packages
    if unique_to_server:
        print(f"Unique to {server}: {unique_to_server}")

# Compliance check: required packages must be on all servers
REQUIRED_PACKAGES = {'python3', 'curl', 'git'}

def compliance_check(server_packages, required):
    non_compliant = {}
    for server, packages in server_packages.items():
        missing = required - packages
        if missing:
            non_compliant[server] = missing

    if non_compliant:
        print("\n❌ COMPLIANCE FAILURES:")
        for server, missing in non_compliant.items():
            print(f"  {server}: Missing {missing}")
    else:
        print("\n✅ All servers compliant")

    return non_compliant

compliance_check(server_packages, REQUIRED_PACKAGES)

# Security audit: blacklisted packages
BLACKLISTED = {'nmap', 'telnet', 'netcat'}

def security_audit(server_packages, blacklisted):
    violations = {}
    for server, packages in server_packages.items():
        found = packages & blacklisted
        if found:
            violations[server] = found

    if violations:
        print("\n🚨 SECURITY VIOLATIONS:")
        for server, pkgs in violations.items():
            print(f"  {server}: Blacklisted packages found: {pkgs}")

    return violations

security_audit(server_packages, BLACKLISTED)

Q29: How do you use frozenset in DevOps?

python
# frozenset = immutable version of set
# Can be used as dictionary key
# Can be used in sets of sets

# Use case: Tracking server group configurations
# where the group membership shouldn't change

web_tier = frozenset(['web-01', 'web-02', 'web-03'])
db_tier = frozenset(['db-01', 'db-02'])
cache_tier = frozenset(['cache-01'])

# Use frozenset as dict key
tier_configs = {
    web_tier: {'port': 80, 'protocol': 'HTTP', 'replicas': 3},
    db_tier: {'port': 3306, 'protocol': 'TCP', 'replicas': 2},
    cache_tier: {'port': 6379, 'protocol': 'TCP', 'replicas': 1},
}

# Lookup config by tier
def get_tier_config(server_name):
    for tier, config in tier_configs.items():
        if server_name in tier:
            return config
    return None

config = get_tier_config('web-01')
print(f"web-01 config: {config}")

# Firewall rule groups (immutable)
ALLOWED_SOURCE_IPS = frozenset([
    '10.0.1.0/24',
    '10.0.2.0/24',
    '192.168.1.0/24'
])

def is_ip_allowed(ip_cidr):
    return ip_cidr in ALLOWED_SOURCE_IPS

# Set of frozensets (unique server groups)
all_tiers = {web_tier, db_tier, cache_tier}
# Regular set cannot contain sets (unhashable)
# frozenset can be in a set ✅

print(f"Number of tiers: {len(all_tiers)}")

Q30-Q35: Set Quick Practice Questions

python
# Q30: Remove duplicates while tracking count
from collections import Counter

events = [
    'ERROR', 'INFO', 'ERROR', 'WARNING',
    'ERROR', 'INFO', 'CRITICAL', 'ERROR'
]

unique_events = set(events)
event_counts = Counter(events)

print(f"Unique event types: {unique_events}")
for event, count in event_counts.most_common():
    print(f"  {event}: {count} times")

# Q31: Check if all required services are running
required_services = {'nginx', 'mysql', 'redis', 'celery'}
running_services = {'nginx', 'mysql', 'redis', 'memcached'}

all_running = required_services.issubset(running_services)
print(f"All required running: {all_running}")

missing = required_services - running_services
if missing:
    print(f"Missing services: {missing}")

# Q32: Add and remove from set
monitoring_targets = {'web-01', 'web-02', 'db-01'}

monitoring_targets.add('cache-01')          # Add one
monitoring_targets.update(['lb-01', 'lb-02']) # Add multiple
monitoring_targets.discard('web-02')        # Remove (no error if missing)
monitoring_targets.remove('db-01')          # Remove (error if missing)

print(f"Monitoring: {monitoring_targets}")

# Q33: isdisjoint - no common elements
prod_servers = {'web-01', 'db-01', 'cache-01'}
dev_servers = {'dev-web-01', 'dev-db-01'}

completely_separate = prod_servers.isdisjoint(dev_servers)
print(f"Prod and Dev completely separate: {completely_separate}")

# Q34: superset and subset checks
all_servers = {'web-01', 'web-02', 'db-01', 'cache-01', 'lb-01'}
monitored = {'web-01', 'web-02', 'db-01'}

print(f"All servers monitored: {monitored.issubset(all_servers)}")
print(f"All servers in system: {all_servers.issuperset(monitored)}")

not_monitored = all_servers - monitored
print(f"Not monitored: {not_monitored}")

# Q35: Pop from set (random removal)
servers_to_process = {'web-01', 'web-02', 'web-03', 'db-01'}

while servers_to_process:
    server = servers_to_process.pop()  # Random element
    print(f"Processing: {server}")
    # Process server...

print("All servers processed!")
SECTION 4 — DICTIONARIES (Q36-Q50)

Q36: What is a Dictionary and how is it used in DevOps?

python
# Dictionary = key-value pairs, ordered (Python 3.7+),
# mutable, keys must be unique

# DevOps use cases:
server_config = {
    'hostname': 'web-01',
    'ip': '10.0.1.10',
    'port': 80,
    'env': 'prod',
    'replicas': 3,
    'tags': ['web', 'nginx', 'production']
}

# Key operations:
print(server_config['hostname'])          # Access
print(server_config.get('cpu', 'N/A'))   # Safe access with default

server_config['cpu'] = 45.2              # Add/update
del server_config['replicas']            # Delete

# Check existence
if 'ip' in server_config:
    print(f"IP: {server_config['ip']}")

# Iterate
for key, value in server_config.items():
    print(f"  {key}: {value}")

print(f"Keys: {list(server_config.keys())}")
print(f"Values: {list(server_config.values())}")
print(f"Length: {len(server_config)}")

Q37: Write a script to manage server inventory with dictionaries

python
# Complete server inventory management system

class ServerInventory:
    def __init__(self):
        self.servers = {}

    def add_server(self, name, **properties):
        self.servers[name] = {
            'name': name,
            'status': 'unknown',
            **properties
        }
        print(f"✅ Added server: {name}")

    def update_server(self, name, **updates):
        if name not in self.servers:
            print(f"❌ Server not found: {name}")
            return
        self.servers[name].update(updates)
        print(f"✅ Updated: {name}")

    def remove_server(self, name):
        removed = self.servers.pop(name, None)
        if removed:
            print(f"🗑️ Removed: {name}")
        else:
            print(f"❌ Not found: {name}")

    def get_server(self, name):
        return self.servers.get(name)

    def get_by_env(self, env):
        return {
            name: info
            for name, info in self.servers.items()
            if info.get('env') == env
        }

    def get_high_cpu(self, threshold=80):
        return {
            name: info
            for name, info in self.servers.items()
            if info.get('cpu', 0) > threshold
        }

    def summary(self):
        total = len(self.servers)
        by_env = {}
        by_status = {}

        for info in self.servers.values():
            env = info.get('env', 'unknown')
            status = info.get('status', 'unknown')
            by_env[env] = by_env.get(env, 0) + 1
            by_status[status] = by_status.get(status, 0) + 1

        print(f"\n📊 Inventory Summary")
        print(f"Total servers: {total}")
        print(f"By environment: {by_env}")
        print(f"By status: {by_status}")

# Use the inventory
inventory = ServerInventory()

inventory.add_server('web-01', ip='10.0.1.10', env='prod', cpu=45.2)
inventory.add_server('web-02', ip='10.0.1.11', env='prod', cpu=87.5)
inventory.add_server('db-01',  ip='10.0.2.10', env='prod', cpu=92.1)
inventory.add_server('dev-web',ip='10.0.3.10', env='dev',  cpu=23.4)

inventory.update_server('web-01', status='healthy', cpu=67.3)

prod_servers = inventory.get_by_env('prod')
print(f"\nProd servers: {list(prod_servers.keys())}")

high_cpu = inventory.get_high_cpu(threshold=80)
print(f"High CPU: {list(high_cpu.keys())}")

inventory.summary()

Q38: How do you merge and update dictionaries?

python
# Dictionary merging - essential for config management

# Base configuration
base_config = {
    'debug': False,
    'log_level': 'INFO',
    'max_connections': 100,
    'timeout': 30,
    'db_host': 'localhost',
    'db_port': 5432,
}

# Environment-specific override
prod_override = {
    'debug': False,
    'log_level': 'WARNING',
    'max_connections': 500,
    'db_host': 'prod-db.internal',
}

# Method 1: update() - modifies in place
config = base_config.copy()
config.update(prod_override)

# Method 2: ** unpacking - creates new dict (Python 3.5+)
config = {**base_config, **prod_override}
# prod_override values win conflicts

# Method 3: | operator (Python 3.9+)
config = base_config | prod_override

print("Merged config:")
for key, value in config.items():
    source = "override" if key in prod_override else "base"
    print(f"  {key}: {value} ({source})")

# Deep merge (nested dictionaries)
def deep_merge(base, override):
    """Recursively merge override into base"""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) \
                and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

nested_base = {
    'database': {'host': 'localhost', 'port': 5432, 'name': 'mydb'},
    'redis': {'host': 'localhost', 'port': 6379},
    'app': {'debug': True, 'workers': 1}
}

nested_override = {
    'database': {'host': 'prod-db.internal', 'name': 'proddb'},
    'app': {'debug': False, 'workers': 4}
}

merged = deep_merge(nested_base, nested_override)
print(f"\nDB host: {merged['database']['host']}")
print(f"DB port: {merged['database']['port']}")  # Preserved from base
print(f"Workers: {merged['app']['workers']}")

Q39: How do you use defaultdict and Counter for DevOps analytics?

python
from collections import defaultdict, Counter
from datetime import datetime

# defaultdict - provides default value for missing keys

# Track errors per server
server_errors = defaultdict(list)

log_entries = [
    ('web-01', 'ERROR', 'Disk full'),
    ('web-02', 'ERROR', 'Connection timeout'),
    ('web-01', 'ERROR', 'Memory exceeded'),
    ('db-01',  'ERROR', 'Query timeout'),
    ('web-01', 'WARNING', 'High CPU'),
    ('web-02', 'ERROR', 'Service crash'),
]

for server, level, message in log_entries:
    server_errors[server].append({
        'level': level,
        'message': message
    })

for server, errors in server_errors.items():
    print(f"{server}: {len(errors)} issues")

# defaultdict(int) for counting
error_counts = defaultdict(int)
for server, level, message in log_entries:
    if level == 'ERROR':
        error_counts[server] += 1

print(f"\nError counts: {dict(error_counts)}")

# Counter - specialized counting dict
log_levels = [entry[1] for entry in log_entries]
level_counts = Counter(log_levels)

print(f"\nLog level distribution:")
for level, count in level_counts.most_common():
    bar = '█' * count
    print(f"  {level:10s}: {bar} ({count})")

# Most common errors
error_messages = [entry[2] for entry in log_entries if entry[1] == 'ERROR']
top_errors = Counter(error_messages).most_common(3)
print(f"\nTop 3 error types: {top_errors}")

# Server error rate analysis
server_counter = Counter(entry[0] for entry in log_entries)
print(f"\nMost problematic servers: {server_counter.most_common(2)}")

# Combine counters
today_errors = Counter({'web-01': 5, 'web-02': 3})
yesterday_errors = Counter({'web-01': 2, 'db-01': 7})
total_errors = today_errors + yesterday_errors
print(f"\nTotal errors: {dict(total_errors)}")

Q40: Write a deployment tracking system using dictionaries

python
from datetime import datetime
import json

class DeploymentTracker:
    def __init__(self):
        self.deployments = {}
        self.server_deployments = {}

    def record_deployment(self, deploy_id, app_name,
                         version, servers, deployed_by):
        deployment = {
            'id': deploy_id,
            'app': app_name,
            'version': version,
            'servers': servers,
            'deployed_by': deployed_by,
            'status': 'in_progress',
            'started_at': datetime.now().isoformat(),
            'completed_at': None,
            'server_statuses': {
                server: 'pending' for server in servers
            }
        }
        self.deployments[deploy_id] = deployment

        # Track per server
        for server in servers:
            if server not in self.server_deployments:
                self.server_deployments[server] = []
            self.server_deployments[server].append(deploy_id)

        print(f"🚀 Deployment {deploy_id} started")
        return deployment

    def update_server_status(self, deploy_id, server, status):
        if deploy_id not in self.deployments:
            return

        deployment = self.deployments[deploy_id]
        deployment['server_statuses'][server] = status

        # Check if all servers done
        statuses = deployment['server_statuses'].values()
        if all(s == 'success' for s in statuses):
            deployment['status'] = 'success'
            deployment['completed_at'] = datetime.now().isoformat()
            print(f"✅ Deployment {deploy_id} completed!")
        elif any(s == 'failed' for s in statuses):
            deployment['status'] = 'partial_failure'

    def get_deployment_history(self, server):
        deploy_ids = self.server_deployments.get(server, [])
        return [
            self.deployments[did]
            for did in deploy_ids
            if did in self.deployments
        ]

    def get_status_summary(self):
        summary = {
            'total': len(self.deployments),
            'success': 0,
            'failed': 0,
            'in_progress': 0
        }
        for dep in self.deployments.values():
            status = dep['status']
            if status in summary:
                summary[status] += 1
        return summary

# Use tracker
tracker = DeploymentTracker()

dep = tracker.record_deployment(
    deploy_id='DEP-001',
    app_name='my-api',
    version='v2.4.1',
    servers=['web-01', 'web-02', 'web-03'],
    deployed_by='prabal.mishra'
)

# Update individual server statuses
tracker.update_server_status('DEP-001', 'web-01', 'success')
tracker.update_server_status('DEP-001', 'web-02', 'success')
tracker.update_server_status('DEP-001', 'web-03', 'success')

# Check history
history = tracker.get_deployment_history('web-01')
print(f"\nweb-01 deployment history: {len(history)} deployments")

summary = tracker.get_status_summary()
print(f"Deployment summary: {summary}")

# Export to JSON
print(json.dumps(dep, indent=2))

Q41: How do you iterate dictionaries efficiently?

python
# Dictionary iteration patterns for DevOps

server_metrics = {
    'web-01': {'cpu': 45.2, 'mem': 67.3, 'disk': 78.1},
    'web-02': {'cpu': 87.5, 'mem': 89.2, 'disk': 45.6},
    'db-01':  {'cpu': 92.1, 'mem': 94.3, 'disk': 67.8},
    'cache-01':{'cpu': 23.4, 'mem': 45.6, 'disk': 12.3},
}

# 1. Iterate keys
print("All servers:")
for server in server_metrics:
    print(f"  {server}")

# 2. Iterate values
print("\nAll metrics:")
for metrics in server_metrics.values():
    print(f"  {metrics}")

# 3. Iterate key-value pairs (most common)
print("\nServer metrics:")
for server, metrics in server_metrics.items():
    cpu = metrics['cpu']
    status = "🔴" if cpu > 80 else "🟢"
    print(f"  {status} {server}: CPU={cpu}%")

# 4. Comprehension with iteration
high_cpu_servers = {
    server: metrics['cpu']
    for server, metrics in server_metrics.items()
    if metrics['cpu'] > 80
}
print(f"\nHigh CPU: {high_cpu_servers}")

# 5. Sorted iteration
print("\nServers by CPU (highest first):")
sorted_servers = sorted(
    server_metrics.items(),
    key=lambda x: x[1]['cpu'],
    reverse=True
)
for server, metrics in sorted_servers:
    print(f"  {server}: {metrics['cpu']}%")

# 6. Enumerate with dict items
print("\nIndexed server list:")
for i, (server, metrics) in enumerate(server_metrics.items(), 1):
    print(f"  {i}. {server}: CPU={metrics['cpu']}%")

# 7. Filter while iterating
def find_critical_resources(metrics, threshold=80):
    critical = {}
    for server, data in metrics.items():
        critical_resources = {
            resource: value
            for resource, value in data.items()
            if value > threshold
        }
        if critical_resources:
            critical[server] = critical_resources
    return critical

critical = find_critical_resources(server_metrics)
print(f"\nCritical resources: {critical}")

Q42: How do you handle nested dictionaries for complex configs?

python
# Nested dictionaries for complex infrastructure configs

infrastructure = {
    'prod': {
        'web_tier': {
            'servers': ['web-01', 'web-02', 'web-03'],
            'load_balancer': 'lb-01',
            'port': 80,
            'ssl_port': 443,
            'health_check': '/health',
        },
        'db_tier': {
            'primary': 'db-01',
            'replicas': ['db-02', 'db-03'],
            'port': 5432,
            'max_connections': 200,
        },
        'cache_tier': {
            'servers': ['cache-01', 'cache-02'],
            'port': 6379,
            'max_memory': '4gb',
        }
    },
    'staging': {
        'web_tier': {
            'servers': ['stg-web-01'],
            'load_balancer': 'stg-lb-01',
            'port': 80,
            'health_check': '/health',
        },
        'db_tier': {
            'primary': 'stg-db-01',
            'replicas': [],
            'port': 5432,
            'max_connections': 50,
        }
    }
}

# Access nested value safely
def get_nested(d, *keys, default=None):
    """Safely access nested dictionary values"""
    current = d
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key, default)
        else:
            return default
    return current

# Safe deep access
prod_primary_db = get_nested(
    infrastructure, 'prod', 'db_tier', 'primary'
)
print(f"Prod primary DB: {prod_primary_db}")

# Non-existent path returns default
missing = get_nested(
    infrastructure, 'prod', 'monitoring', 'url',
    default='Not configured'
)
print(f"Monitoring: {missing}")

# Get all servers across tiers for an environment
def get_all_servers(infra, env):
    env_config = infra.get(env, {})
    all_servers = []

    for tier_name, tier_config in env_config.items():
        if 'servers' in tier_config:
            all_servers.extend(tier_config['servers'])
        if 'primary' in tier_config:
            all_servers.append(tier_config['primary'])
        if 'replicas' in tier_config:
            all_servers.extend(tier_config['replicas'])
        if 'load_balancer' in tier_config:
            all_servers.append(tier_config['load_balancer'])

    return list(set(all_servers))  # Remove duplicates

prod_servers = get_all_servers(infrastructure, 'prod')
print(f"\nAll prod servers: {sorted(prod_servers)}")

# Flatten nested dict for reporting
def flatten_dict(d, parent_key='', sep='.'):
    """Flatten nested dict to single level"""
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep))
        else:
            items[new_key] = v
    return items

prod_flat = flatten_dict(infrastructure.get('prod', {}))
for key, value in list(prod_flat.items())[:8]:
    print(f"  {key}: {value}")

Q43: Write a config management system using dictionaries

python
import os
import json

class ConfigManager:
    """
    Manages application configuration using dictionaries.
    Supports environment overrides and validation.
    """

    DEFAULTS = {
        'app': {
            'name': 'my-app',
            'version': '1.0.0',
            'debug': False,
            'workers': 4,
        },
        'database': {
            'host': 'localhost',
            'port': 5432,
            'name': 'mydb',
            'pool_size': 10,
            'timeout': 30,
        },
        'redis': {
            'host': 'localhost',
            'port': 6379,
            'db': 0,
            'ttl': 3600,
        },
        'monitoring': {
            'enabled': True,
            'interval': 60,
            'alert_threshold': 80,
        }
    }

    ENV_OVERRIDES = {
        'production': {
            'app': {'debug': False, 'workers': 8},
            'database': {'host': 'prod-db.internal', 'pool_size': 50},
            'redis': {'host': 'prod-redis.internal'},
        },
        'staging': {
            'app': {'debug': True, 'workers': 2},
            'database': {'host': 'stg-db.internal', 'pool_size': 20},
        },
        'development': {
            'app': {'debug': True, 'workers': 1},
            'monitoring': {'enabled': False},
        }
    }

    def __init__(self, environment='development'):
        self.environment = environment
        self.config = self._build_config()

    def _deep_merge(self, base, override):
        result = base.copy()
        for key, value in override.items():
            if key in result and isinstance(result[key], dict):
                result[key] = self._deep_merge(result[key], value)
            else:
                result[key] = value
        return result

    def _build_config(self):
        config = json.loads(json.dumps(self.DEFAULTS))
        env_override = self.ENV_OVERRIDES.get(self.environment, {})
        config = self._deep_merge(config, env_override)
        return config

    def get(self, *keys, default=None):
        current = self.config
        for key in keys:
            if isinstance(current, dict):
                current = current.get(key, default)
            else:
                return default
        return current

    def set(self, value, *keys):
        current = self.config
        for key in keys[:-1]:
            current = current.setdefault(key, {})
        current[keys[-1]] = value

    def validate(self):
        required = [
            ('database', 'host'),
            ('database', 'port'),
            ('app', 'workers'),
        ]
        errors = []
        for keys in required:
            value = self.get(*keys)
            if value is None:
                errors.append(f"Missing: {'.'.join(keys)}")

        if errors:
            raise ValueError(f"Config errors: {errors}")
        return True

    def display(self):
        print(f"\nConfiguration ({self.environment})")
        print("=" * 40)
        for section, values in self.config.items():
            print(f"\n[{section}]")
            for key, value in values.items():
                print(f"  {key}: {value}")

# Usage
config = ConfigManager('production')
config.validate()
config.display()

# Access values
db_host = config.get('database', 'host')
workers = config.get('app', 'workers')
print(f"\nDB: {db_host}")
print(f"Workers: {workers}")

Q44: How do you use dict comprehensions for data transformation?

python
# Dict comprehensions - powerful for data transformation

# 1. Basic dict comprehension
servers = ['web-01', 'web-02', 'db-01', 'cache-01']
server_dict = {server: 'unknown' for server in servers}
print(server_dict)

# 2. From two lists
ips = ['10.0.1.10', '10.0.1.11', '10.0.2.10', '10.0.3.10']
server_ip_map = {
    server: ip
    for server, ip in zip(servers, ips)
}
print(server_ip_map)

# 3. With condition
server_status = {
    'web-01': 'running',
    'web-02': 'stopped',
    'db-01': 'running',
    'cache-01': 'stopped',
    'lb-01': 'running'
}

# Only running servers
running = {
    server: status
    for server, status in server_status.items()
    if status == 'running'
}
print(f"Running: {running}")

# 4. Transform values
cpu_data = {
    'web-01': 45.234567,
    'web-02': 87.891234,
    'db-01': 92.123456,
}

rounded_cpu = {
    server: round(cpu, 1)
    for server, cpu in cpu_data.items()
}
print(f"Rounded: {rounded_cpu}")

# 5. Invert dictionary
server_to_ip = {'web-01': '10.0.1.10', 'web-02': '10.0.1.11'}
ip_to_server = {ip: server for server, ip in server_to_ip.items()}
print(f"IP lookup: {ip_to_server}")

# 6. Group by (like SQL GROUP BY)
server_list = [
    {'name': 'web-01', 'env': 'prod', 'cpu': 45},
    {'name': 'web-02', 'env': 'prod', 'cpu': 87},
    {'name': 'dev-01', 'env': 'dev',  'cpu': 23},
    {'name': 'dev-02', 'env': 'dev',  'cpu': 34},
]

from collections import defaultdict
by_env = defaultdict(list)
for server in server_list:
    by_env[server['env']].append(server['name'])

print(f"By env: {dict(by_env)}")

# 7. Complex transformation
metrics = {
    'web-01': {'cpu': 45, 'mem': 67, 'disk': 78},
    'web-02': {'cpu': 87, 'mem': 89, 'disk': 45},
}

# Add alert status to each server
enhanced_metrics = {
    server: {
        **data,
        'alert': any(v > 80 for v in data.values()),
        'health': 'critical' if any(v > 90 for v in data.values())
                  else 'warning' if any(v > 80 for v in data.values())
                  else 'healthy'
    }
    for server, data in metrics.items()
}

for server, data in enhanced_metrics.items():
    print(f"{server}: {data['health']}")

Q45-Q50: Dictionary Quick Practice Questions

python
# Q45: Get, setdefault, and pop
config = {'host': 'localhost', 'port': 5432}

# get with default (no KeyError)
host = config.get('host', 'unknown')
debug = config.get('debug', False)  # Returns False if missing
print(f"Host: {host}, Debug: {debug}")

# setdefault - set if key doesn't exist
config.setdefault('timeout', 30)      # Sets to 30
config.setdefault('host', 'CHANGED')  # Does NOT change existing
print(config)

# pop - remove and return value
port = config.pop('port', 'N/A')  # Returns value and removes
print(f"Removed port: {port}")

# Q46: Sort dictionary by value
server_cpu = {'web-02': 87, 'web-01': 45, 'db-01': 92, 'cache-01': 23}

sorted_by_cpu = dict(sorted(
    server_cpu.items(),
    key=lambda x: x[1],
    reverse=True
))
print("Sorted by CPU:", sorted_by_cpu)

# Q47: Find servers meeting multiple criteria
inventory = [
    {'name': 'web-01', 'env': 'prod', 'cpu': 45, 'region': 'us-east'},
    {'name': 'web-02', 'env': 'prod', 'cpu': 87, 'region': 'us-west'},
    {'name': 'dev-01', 'env': 'dev',  'cpu': 23, 'region': 'us-east'},
]

def find_servers(**criteria):
    return [
        s for s in inventory
        if all(s.get(k) == v for k, v in criteria.items())
    ]

prod_east = find_servers(env='prod', region='us-east')
print(f"Prod US-East: {[s['name'] for s in prod_east]}")

# Q48: Merge list of dicts by key
deployments = [
    {'server': 'web-01', 'version': 'v1.0', 'status': 'success'},
    {'server': 'web-02', 'version': 'v1.0', 'status': 'failed'},
    {'server': 'web-01', 'version': 'v1.1', 'status': 'success'},
]

# Get latest deployment per server
latest_deployments = {}
for dep in deployments:
    server = dep['server']
    latest_deployments[server] = dep

print("Latest deployments:")
for server, dep in latest_deployments.items():
    print(f"  {server}: {dep['version']} ({dep['status']})")

# Q49: Update nested dictionary safely
def safe_update(d, keys, value):
    """Update nested dict, creating keys if needed"""
    current = d
    for key in keys[:-1]:
        current = current.setdefault(key, {})
    current[keys[-1]] = value
    return d

metrics = {}
safe_update(metrics, ['web-01', 'cpu', 'current'], 45.2)
safe_update(metrics, ['web-01', 'cpu', 'max'], 87.5)
safe_update(metrics, ['web-01', 'memory', 'used_gb'], 12.3)
print(metrics)

# Q50: Real world - parse config file to dict
config_text = """
host=prod-db.internal
port=5432
name=mydb
pool_size=50
timeout=30
debug=false
"""

def parse_config(text):
    config = {}
    for line in text.strip().split('\n'):
        if '=' in line and not line.startswith('#'):
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()

            # Type conversion
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            elif value.isdigit():
                value = int(value)
            elif value.replace('.', '').isdigit():
                value = float(value)

            config[key] = value

    return config

db_config = parse_config(config_text)
print(f"\nParsed config: {db_config}")
print(f"Types: host={type(db_config['host'])}, "
      f"port={type(db_config['port'])}, "
      f"debug={type(db_config['debug'])}")
QUICK REFERENCE SUMMARY
python
# ============================================
# WHEN TO USE WHICH DATA STRUCTURE
# ============================================

# LIST → When you need:
# ✅ Ordered sequence
# ✅ Duplicates allowed  
# ✅ Frequent append/pop
# ✅ Iteration in order
# Example: servers = ['web-01', 'web-02']

# TUPLE → When you need:
# ✅ Immutable sequence
# ✅ Dict keys or set elements
# ✅ Function return multiple values
# ✅ Fixed configuration
# Example: SERVER_PORTS = (22, 80, 443)

# SET → When you need:
# ✅ Unique elements only
# ✅ Fast membership test
# ✅ Set operations (union, intersect)
# ✅ Remove duplicates
# Example: running = {'web-01', 'web-02'}

# DICT → When you need:
# ✅ Key-value mapping
# ✅ Fast key lookup
# ✅ Structured data
# ✅ JSON-like configs
# Example: config = {'host': 'localhost'}

# ============================================
# PERFORMANCE CHEAT SHEET
# ============================================
# Membership test:
#   Set: O(1) ← FASTEST
#   Dict: O(1) ← FASTEST  
#   List: O(n) ← SLOW for large lists
#   Tuple: O(n)

# Append:
#   List: O(1) amortized ← FAST
#   Set: O(1) ← FAST

# Insert at position:
#   List: O(n) ← SLOW

# Key lookup:
#   Dict: O(1) ← FASTEST
# ============================================

Master these 50 questions and you will handle any Python data structures question in DevOps interviews confidently! 🚀