Version 1 — Standard (2 minutes — use this most)
"Good morning. Thank you for this opportunity.

My name is Prabal Mishra and I am an
Application Support Engineer with 4+ years
of hands-on experience in production support,
incident management, and system monitoring
for enterprise-level banking applications.

I am currently at Tata Consultancy Services
working for Commonwealth Bank of Australia —
one of Australia's largest financial institutions.
My day-to-day work involves tier-2 and tier-3
support for Credit Risk and Market Risk
applications running on Linux and UNIX platforms.

My core strengths are incident management using
ServiceNow, Autosys batch job scheduling,
Oracle and MySQL database administration,
shell scripting for automation, and root cause
analysis for complex production issues.

Some highlights from my current role:
I have maintained 99.9% application uptime
across 24x7 operations, reduced P2 incident
resolution time by 35%, automated 40% of
manual monitoring tasks through Bash scripting,
and managed 100+ production Autosys jobs with
zero missed SLA windows.

I also have strong experience in ITIL practices,
SOX compliance, change management through
ServiceNow, and cross-functional collaboration
with development, DBA, QA, and infrastructure
teams.

I am excited about this opportunity and look
forward to contributing my production support
expertise to your team."
Version 2 — Short (1 minute — when asked to be brief)
"Good morning. My name is Prabal Mishra.

I am an Application Support Engineer at TCS
with 4+ years of experience supporting
enterprise banking applications for
Commonwealth Bank of Australia.

My expertise is in tier-2 and tier-3
production support, incident management
on ServiceNow, Autosys batch scheduling,
Oracle and MySQL databases, and Linux
shell scripting for automation.

Key achievements: 99.9% uptime maintained,
35% MTTR reduction, 40% manual tasks
automated, and zero SOX audit findings
across two consecutive audits.

I am looking forward to discussing how my
experience aligns with this role."
Version 3 — Senior Role (2.5 minutes)
"Good morning. My name is Prabal Mishra.

I bring 4+ years of enterprise production
support experience from TCS, where I work
for Commonwealth Bank of Australia —
supporting Credit Risk and Market Risk
applications that are critical to the bank's
daily operations.

What makes my background unique is the
combination of depth and breadth. On the
technical side I am hands-on with Linux
administration, Oracle and MySQL databases,
Autosys job scheduling, Bash scripting,
and ITSM tools including ServiceNow and
Salesforce. On the operational side I have
managed the full P1 to P3 incident lifecycle,
handled SOX compliance audits, led change
management processes, and built a knowledge
base of 50+ articles that reduced repeat
escalations by 30%.

I have operated in a true 24x7 banking
environment where uptime is non-negotiable —
which has sharpened my instincts for
proactive monitoring, fast root cause analysis,
and clear stakeholder communication under
pressure.

My numbers speak to what I have delivered:
99.9% uptime, 35% faster incident resolution,
40% reduction in manual effort through
automation, and zero audit findings across
two SOX compliance cycles.

I am genuinely passionate about production
stability and operational excellence and I
am looking for an environment where I can
continue to grow and take on more complex
challenges. I believe this role is that
opportunity and I look forward to our
conversation."
50 INTERVIEW QUESTIONS AND ANSWERS
SECTION 1 — PRODUCTION SUPPORT FUNDAMENTALS (Q1-Q10)

Q1: Tell me about your production support experience

Answer:
"I have 4+ years of tier-2 and tier-3
production support experience at TCS
for Commonwealth Bank of Australia.

The applications I support are Credit Risk
and Market Risk — core banking systems
deployed on Linux and UNIX platforms
that run 24x7 and directly impact the
bank's financial operations.

My daily responsibilities include:
→ Monitoring system health and logs
→ Triaging and resolving incidents
  in ServiceNow
→ Managing Autosys batch jobs
→ Oracle and MySQL database queries
  and administration
→ Shell scripting for automation
→ Change management and releases
→ SOX compliance and audit support

What I am most proud of is maintaining
99.9% application uptime over the course
of my engagement — in a banking environment
where even minutes of downtime have
significant business and regulatory impact."

Q2: What is the difference between Tier 1, Tier 2, and Tier 3 support?

Answer:
"Support tiers represent increasing
levels of technical complexity
and escalation.

Tier 1 — First Line Support:
→ Initial point of contact
→ Basic troubleshooting
→ Password resets, access issues
→ Follows scripts and runbooks
→ Logs ticket in ServiceNow
→ Resolves simple issues or escalates

Tier 2 — Application Support (My level):
→ Deeper technical investigation
→ Application-specific expertise
→ Log analysis, database queries
→ Autosys job failures
→ Root cause analysis
→ Coordinates with development teams
→ Resolves most production issues

Tier 3 — Engineering/Development:
→ Code-level fixes required
→ Architecture changes
→ Vendor escalations
→ Complex infrastructure issues
→ Development team involvement
→ Takes code to production

In my role at CBA I handle tier-2 issues
directly and escalate to tier-3 when
code changes are needed. I always
aim to resolve at tier-2 to reduce
escalations and protect development
team capacity."

Q3: How do you prioritise incidents when multiple come in at the same time?

Answer:
"Incident prioritisation follows the
ITIL framework which I apply daily
in my role at CBA.

Priority levels in our environment:

P1 — Critical:
→ Complete system outage
→ Core banking application down
→ Entire user base impacted
→ Response: Immediate — within 15 mins
→ Resolution target: 1-2 hours
→ War-room initiated, all hands on

P2 — High:
→ Major functionality impaired
→ Significant user group affected
→ Workaround may exist
→ Response: Within 30 minutes
→ Resolution target: 4 hours

P3 — Medium:
→ Minor functionality affected
→ Limited user impact
→ Workaround available
→ Resolution target: 8-24 hours

P4 — Low:
→ Minimal impact
→ Informational or cosmetic
→ Resolution target: 72 hours

When multiple tickets arrive together
I first check for P1s — those get
immediate attention regardless of
anything else. For same-priority
tickets I assess business impact:
which application, how many users,
is there a regulatory reporting
deadline today, is it market hours.
I communicate status to all
stakeholders immediately and
provide ETA updates every 30
minutes on P1/P2 incidents."

Q4: Walk me through how you handle a P1 incident from start to resolution

Answer:
"This is my bread and butter —
I handle P1s regularly in a
24x7 banking environment.

Step 1: Alert received
→ PagerDuty or monitoring alert fires
→ Or ServiceNow ticket raised as P1
→ I acknowledge immediately
→ Start the clock — SLA begins

Step 2: Initial assessment (first 5 mins)
→ What application is affected?
→ What is the exact symptom?
→ How many users impacted?
→ When did it start?
→ Any recent changes deployed?
  (check change log in ServiceNow)

Step 3: Notify stakeholders
→ Incident bridge call initiated
→ Notify: Application manager,
  development lead, DBA team,
  infrastructure team
→ Send initial impact communication
  to business stakeholders
→ Update ServiceNow ticket with
  initial findings

Step 4: Investigation
→ Check application logs on Linux:
  tail -f /app/logs/app.log
  grep -i error /app/logs/app.log
→ Check Autosys jobs if batch related
→ Check Oracle database connections
→ Check CPU, memory, disk on server
→ Check network connectivity
→ Compare with yesterday's baseline

Step 5: Coordinate resolution
→ Share findings on bridge call
→ Engage correct team
  (dev for code, DBA for database,
  infra for server/network)
→ Execute fix or workaround
→ Verify restoration

Step 6: Closure
→ Confirm with business that
  service is restored
→ Update ServiceNow ticket
→ Send all-clear communication
→ Schedule post-incident review

Step 7: Post-Incident Review (PIR)
→ Within 24-48 hours
→ Timeline of events
→ Root cause identified
→ Action items to prevent recurrence
→ Knowledge base article created

This structured approach is why we
achieved 35% reduction in MTTR
in our environment."

Q5: What is Root Cause Analysis (RCA) and how do you perform it?

Answer:
"Root Cause Analysis is the process
of identifying the fundamental reason
why an incident occurred — not just
fixing the symptom but preventing
it from happening again.

My RCA approach uses the
5 Whys technique:

Example from my CBA experience:

Problem: Credit Risk batch job failed
at 2 AM causing morning report delay

Why 1: Why did the job fail?
→ Database connection timed out

Why 2: Why did connection time out?
→ Database was running slow

Why 3: Why was database slow?
→ Tablespace was 98% full

Why 4: Why was tablespace full?
→ Archive logs accumulated
  for 3 months not purged

Why 5: Why were archive logs not purged?
→ No automated purge job existed
  and no monitoring on tablespace

Root Cause: Missing automated
tablespace monitoring and purge process

Resolution:
→ Immediate: Purge old archive logs
→ Short term: Set up tablespace
  alert at 80% threshold
→ Long term: Create Autosys job
  for weekly automated purge
→ Knowledge article created

Result: This class of incident
never recurred in our environment.

A good RCA results in permanent
prevention not just a temporary fix."

Q6: What monitoring do you do daily and what tools do you use?

Answer:
"Daily monitoring in my role
covers multiple layers:

Application Layer:
→ Review application logs for
  errors, warnings, exceptions
→ Commands I use:
  tail -100 /app/logs/app.log
  grep -i 'error\|exception\|fatal'
  /app/logs/app.log | tail -50
  grep -c 'ERROR' app.log
  (count errors and compare to baseline)

Autosys Batch Layer:
→ Review overnight batch job status
  every morning
→ Check for failed, on-ice,
  or terminated jobs
→ Verify completion times
  against expected SLA

Database Layer:
→ Check Oracle alert log for ORA- errors
→ Monitor tablespace utilisation
→ Check active sessions and locks
→ Verify backup job status

Infrastructure Layer:
→ CPU utilisation
→ Memory usage
→ Disk space (df -h)
→ Network connectivity

ServiceNow:
→ Review open P1/P2 tickets
→ Check tickets breaching SLA
→ Review overnight incidents

This proactive monitoring approach
is how we maintain 99.9% uptime —
we catch issues before users do."

Q7: What is SLA and how do you ensure you meet it?

Answer:
"SLA — Service Level Agreement —
is the contractual commitment on
response and resolution times
for incidents by priority.

At CBA our SLAs are:
→ P1: Response 15 min, Resolve 2 hrs
→ P2: Response 30 min, Resolve 4 hrs
→ P3: Response 2 hrs, Resolve 24 hrs
→ P4: Response 8 hrs, Resolve 72 hrs

How I ensure SLA compliance:

1. ServiceNow SLA clock visibility
   → Every ticket shows SLA countdown
   → I check this first thing
   → Filter for near-breach tickets

2. Proactive monitoring
   → Catching issues early reduces
     resolution time
   → Most P1s start as warnings
     if you catch them in time

3. Clear escalation paths
   → I know exactly who to call
     for each application
   → No time wasted finding
     the right person

4. Parallel working
   → While investigation runs
     I am already communicating
     to stakeholders
   → No sequential processing

5. Shift handover discipline
   → Detailed handover notes
   → No SLA gaps between shifts

Result: We have consistently
maintained SLA compliance above
98% throughout my engagement."

Q8: How do you handle an incident where you cannot find the root cause?

Answer:
"This happens in complex environments
and knowing how to handle it
professionally is critical.

Step 1: Restore service first
→ Root cause finding is secondary
  to service restoration
→ Restart the application
→ Fail over to standby
→ Apply a known workaround
→ Business is back online first

Step 2: Preserve evidence
→ Before restarting: take log snapshots
→ Copy heap dumps if application crashed
→ Note exact timestamps
→ Screenshot monitoring dashboards
→ This evidence is needed for RCA

Step 3: Communicate honestly
→ Update stakeholders:
  'Service restored. Root cause
   investigation ongoing. Update
   by [specific time].'
→ Never say 'We do not know'
  without a follow-up plan

Step 4: Structured investigation
→ Review all logs from the
  incident window
→ Check change records —
  anything deployed recently?
→ Check infrastructure changes
→ Compare with similar past incidents
→ Engage vendor support if needed
  (Oracle SR, for example)

Step 5: Document and escalate
→ If unable to identify cause
  within expected timeframe
→ Raise to Tier 3 engineering
→ Engage application vendor
→ Document everything attempted

Step 6: Trend analysis
→ If incident repeats without
  clear cause: look for patterns
→ Same time of day?
→ Same batch job running?
→ Memory leak pattern?

Being transparent and systematic
even when you do not have an answer
builds more trust than pretending."

Q9: What is Change Management and how do you follow it?

Answer:
"Change Management in ITIL is the
process of controlling changes to
production systems to minimise
risk and disruption.

At CBA we follow a strict
change management process:

Types of changes:

Standard Change:
→ Pre-approved, low risk
→ Routine maintenance tasks
→ No CAB approval needed
→ Example: SSL certificate renewal

Normal Change:
→ Requires CAB review and approval
→ Risk assessment completed
→ Rollback plan mandatory
→ Deployment window agreed
→ Example: Application patch

Emergency Change:
→ Unplanned fix for P1 incident
→ Post-implementation review required
→ Expedited CAB approval
→ Higher scrutiny in review

My change management process:

1. Raise Change Request in ServiceNow
   → Detailed description
   → Risk assessment (Low/Medium/High)
   → Implementation steps
   → Rollback steps — ALWAYS
   → Testing plan
   → Deployment window

2. CAB review meeting
   → Present the change
   → Answer technical questions
   → Get approval or rework

3. Deployment night
   → Confirm team availability
   → Execute pre-deployment checklist
   → Deploy in change window
   → Run smoke tests
   → Confirm success or rollback

4. Post-deployment verification
   → Monitor for 30-60 minutes
   → Confirm with application team
   → Update change record to Closed

I have zero unauthorised changes
in my entire engagement — every
change in production is documented
and approved."

Q10: How do you handle on-call duties and after-hours incidents?

Answer:
"On-call support is a core part
of supporting 24x7 banking systems.

My on-call approach:

Preparation:
→ Keep runbooks updated and accessible
  on my phone (not just on laptop)
→ Know escalation contacts by heart
→ Ensure VPN access works from home
→ Alert thresholds tuned to avoid
  unnecessary wake-up calls

When alert fires at 2 AM:
→ Acknowledge within defined SLA
→ Quickly assess: real issue or false alarm?
→ Check monitoring dashboard first
→ Triage: Can I resolve alone or
  do I need to wake someone up?
→ Make that decision quickly
  (better to engage early for P1s)

Communication:
→ Even at 2 AM: send a brief update
  to the incident channel
→ Business stakeholders notified
  if business impact confirmed
→ No surprises in the morning

Handover:
→ When morning shift starts:
  detailed verbal and written handover
→ What happened, what was done,
  what still needs follow-up

Work-life balance reality:
→ Good on-call means fewer calls
→ Proactive monitoring prevents
  most overnight incidents
→ Our automation work reduced
  unnecessary on-call triggers by 40%"
SECTION 2 — AUTOSYS & BATCH JOBS (Q11-Q18)

Q11: What is Autosys and how have you used it?

Answer:
"Autosys is an enterprise job scheduling
tool from Broadcom (formerly CA Technologies).
It automates, monitors, and manages
batch job execution across distributed
environments.

In my role at CBA I use Autosys daily
to manage 100+ production batch jobs
for Credit Risk and Market Risk
application workflows.

Key components I work with:

Job Definition:
→ Box jobs (containers for multiple jobs)
→ Command jobs (execute scripts)
→ File watcher jobs (trigger on file arrival)
→ FTP jobs (file transfers)

Job Dependencies:
→ Jobs chained using
  condition: s(previous_job) = 'SUCCESS'
→ Box jobs group related jobs
→ Failure of one job can stop chain

Key Autosys commands I use daily:
→ autorep -J job_name -s (job status)
→ sendevent -J job_name -E STARTJOB
  (manually start a job)
→ sendevent -J job_name -E KILLJOB
  (kill a running job)
→ sendevent -J job_name -E ON_ICE
  (put job on hold)
→ sendevent -J job_name -E OFF_ICE
  (release from hold)
→ autorep -J job_name -q
  (job definition)

Common statuses I monitor:
→ SUCCESS: Completed normally
→ FAILURE: Job failed
→ RUNNING: Currently executing
→ INACTIVE: Waiting for start
→ ON_HOLD: Manually held
→ ON_ICE: Dependency not met
→ TERMINATED: Killed mid-run"

Q12: What do you do when an Autosys job fails?

Answer:
"Autosys job failure investigation
is one of my most frequent activities.
Here is my exact process:

Step 1: Identify the failed job
→ Check Autosys monitoring dashboard
  OR receive alert via email/PagerDuty
→ Note exact job name and failure time

Step 2: Check job status
→ autorep -J job_name -s
→ Note: exit code, start time, end time

Step 3: Check job output/log
→ Find log file location from
  job definition
→ autorep -J job_name -q
  (shows std_out_file path)
→ Review last 100 lines of log:
  tail -100 /path/to/job.log
→ Look for: ERROR, FAILED, exception,
  ORA- (Oracle errors), permission denied,
  file not found, disk full

Step 4: Identify root cause
Common causes I have seen:
→ Database connection failure
→ Input file not arrived (file watcher)
→ Disk space full on server
→ Dependent job failed first
→ Script permission changed
→ Network timeout to external system
→ Invalid data in input file

Step 5: Resolve or escalate
→ If DB connection: check DB health
→ If file missing: check upstream
  data feed
→ If disk full: clear space,
  alert infra team
→ If script error: fix or escalate
  to development team

Step 6: Rerun the job
→ sendevent -J job_name -E STARTJOB
→ Monitor to confirm SUCCESS

Step 7: Document
→ Update ServiceNow ticket
→ Note cause and resolution
→ If recurring: create knowledge article
  and raise for permanent fix"

Q13: What is the difference between ON_ICE and ON_HOLD in Autosys?

Answer:
"Both statuses pause a job but
for different reasons:

ON_ICE:
→ Job's starting conditions
  are not met
→ Usually a dependency issue:
  dependent job has not succeeded yet
→ Job is waiting automatically
→ System puts it ON_ICE
→ Will automatically start when
  conditions are met
→ You can manually override with
  OFF_ICE if needed
→ Common scenario: File watcher job
  waiting for input file to arrive

ON_HOLD:
→ Job has been manually held
  by an operator or support team
→ Deliberate human intervention
→ Will NOT start even if all
  conditions are met
→ Someone must explicitly release:
  sendevent -J job_name -E RELEASE
→ Common scenario: Holding a job
  while a maintenance window
  is in progress, or while an
  upstream dependency is being fixed

Summary:
ON_ICE = waiting for automatic condition
ON_HOLD = manually paused by a person

Both prevent the job from running but
for fundamentally different reasons.
Always check which it is before
deciding how to respond."

Q14: How do you monitor overnight batch jobs in the morning?

Answer:
"Morning batch review is one of
the first things I do every shift.

My morning batch review process:

Step 1: Dashboard review
→ Open Autosys dashboard or
  Autosys GUI (Workload View)
→ Filter to show jobs from
  previous night's window
→ Look for: FAILURE, TERMINATED,
  or jobs still RUNNING past SLA time

Step 2: Check critical job chain first
→ Some jobs are business-critical:
  if they fail, reporting is delayed
→ These get checked first
→ Know the priority order of jobs

Step 3: Investigate failures
→ For each failed job:
  check logs (as per Q12 process)
→ Assess if rerun is safe:
  is it idempotent? Has data
  already been partially processed?

Step 4: Check completion times
→ Even successful jobs checked
  against expected SLA window
→ Job completed 3 hours late
  even with SUCCESS status
  could indicate a performance issue

Step 5: Cross-check with databases
→ Did the batch actually load data?
→ SELECT COUNT(*) FROM target_table
  WHERE load_date = TRUNC(SYSDATE)
→ Verify record counts match expected

Step 6: Daily status report
→ Send batch run summary to
  application and business teams:
  'Batch completed: X of Y jobs
   successful. 2 failures investigated
   and resolved. Data available
   by 8 AM as expected.'

This proactive communication means
business teams trust the process
and rarely chase the support team."

Q15: What do you do if a job completes with SUCCESS but data is wrong?

Answer:
"This is a tricky scenario and
more common than people expect.

Autosys shows SUCCESS because the
script completed without a non-zero
exit code — but the data may be
incorrect if the script does not
validate its own output.

My investigation approach:

Step 1: Verify the data issue
→ Run validation SQL query:
  SELECT COUNT(*), SUM(amount)
  FROM transactions
  WHERE process_date = TRUNC(SYSDATE)
→ Compare with expected values
→ Confirm it is a real data problem
  not a reporting issue

Step 2: Check job logs carefully
→ SUCCESS exit code does not mean
  all data was processed correctly
→ Look in logs for:
  'Records processed: 0'
  'Warning: file empty'
  'Skipped X records due to validation'
→ Job may have processed empty file
  and exited with 0 (success)

Step 3: Check input files
→ Did the correct file arrive?
→ Correct date in filename?
→ Correct record count in file?
→ File not corrupted (checksum)?

Step 4: Check transformation logic
→ Any data type conversion failures?
→ Any records silently rejected?
→ SQL insert errors swallowed by script?

Step 5: Escalate with evidence
→ This is typically a development
  defect or data quality issue
→ Raise to dev team with full evidence:
  input file, log extract, SQL results
→ Rerun may or may not fix it —
  depends on root cause

Lesson: A SUCCESS status in Autosys
means the script ran without crashing —
it does not guarantee data correctness.
Always validate data separately."

Q16: What is a Box job in Autosys?

Answer:
"A Box job in Autosys is a container
or parent job that groups multiple
related jobs together.

Purpose:
→ Logical grouping of related jobs
→ Control when the entire group runs
→ Dependencies can be set at Box level
→ If Box fails: all child jobs stop

Structure:
Box: BOX_CREDIT_RISK_NIGHTLY
  Job 1: EXTRACT_SOURCE_DATA
  Job 2: VALIDATE_DATA
  Job 3: LOAD_TO_WAREHOUSE
  Job 4: GENERATE_REPORTS
  Job 5: SEND_NOTIFICATIONS

Benefits:
→ One schedule for the entire group
→ Clear ownership of related jobs
→ Easier monitoring — check Box status
→ Dependencies managed at Box level:
  Job 3 depends on Job 2 success
  Job 2 depends on Job 1 success

Commands:
→ Checking Box status:
  autorep -J BOX_CREDIT_RISK_NIGHTLY -s
→ Starting entire Box:
  sendevent -J BOX_CREDIT_RISK_NIGHTLY
  -E STARTJOB
→ Killing entire Box and all children:
  sendevent -J BOX_CREDIT_RISK_NIGHTLY
  -E KILLJOB

At CBA most of our batch workflows
are organised into Box jobs by
application module and run time —
overnight boxes, end-of-day boxes,
and intraday boxes."

Q17: How do you add or modify an Autosys job?

Answer:
"Adding or modifying Autosys jobs
in production follows our change
management process — it is a
change request, not an ad-hoc action.

Process:

Step 1: Raise change request
→ ServiceNow change request
→ Attach JIL (Job Information
  Language) file with changes
→ Approval from application owner

Step 2: Test in lower environment
→ Test in DEV or SIT first
→ Verify job runs correctly
→ Verify dependencies work
→ Verify alerts fire correctly

Step 3: Production change window
→ Only during approved window
→ Use JIL to create/update job:
  jil < job_definition.jil

JIL example for a new job:
insert_job: DAILY_REPORT_JOB
job_type: CMD
command: /app/scripts/daily_report.sh
machine: prod-server-01
owner: appuser
permission: gx, wx
start_times: '02:00'
condition: s(EXTRACT_JOB) = 'SUCCESS'
description: Daily credit risk report
std_out_file: /app/logs/daily_report.log
std_err_file: /app/logs/daily_report.err
alarm_if_fail: 1
alarm_if_late: 1

Step 4: Verify in production
→ Check job is visible:
  autorep -J DAILY_REPORT_JOB -q
→ Confirm definition is correct
→ Do NOT manually trigger unless
  required — let next scheduled
  run confirm it works"

Q18: What do you check when a job keeps running longer than expected?

Answer:
"A job running much longer than
its normal SLA is a warning sign
even if it has not failed yet.

My investigation:

Step 1: Check the job runtime
→ autorep -J job_name -s
→ Note start time, calculate duration
→ Compare with historical average:
  How long does this job normally take?

Step 2: Check what the job is doing
→ Login to server running the job
→ ps -ef | grep job_script_name
→ Check CPU and memory:
  top -p <PID>

Step 3: Check database
If job does database work:
→ Is there a long-running query?
  SELECT * FROM v$session
  WHERE status = 'ACTIVE'
  AND username = 'APPUSER'
→ Are there database locks?
  SELECT * FROM v$locked_object
→ Is tablespace getting full during run?

Step 4: Check server resources
→ df -h (disk space)
→ free -m (memory)
→ iostat (I/O bottleneck?)

Step 5: Check logs mid-run
→ tail -f /path/to/job.log
→ Is it actively processing?
→ Or stuck at one line?

Step 6: Decision
→ If processing normally but slowly:
  Alert but let it run, monitor closely
→ If stuck/hung:
  Kill and restart with dev team aware
→ If resource issue:
  Fix resource first, then restart

Communication:
→ Even while investigating:
  notify relevant teams if
  job will miss its SLA window
→ Business needs to know if
  morning reports will be delayed"
SECTION 3 — LINUX & SHELL SCRIPTING (Q19-Q25)

Q19: What Linux commands do you use most in production support?

Answer:
"Linux commands are my daily toolkit.
Most frequently used in production:

LOG INVESTIGATION:
tail -f /app/logs/app.log
  (live log monitoring)

tail -100 /app/logs/app.log
  (last 100 lines)

grep -i 'error\|exception\|fatal' app.log
  (find errors case-insensitive)

grep -c 'ERROR' app.log
  (count errors)

grep 'ERROR' app.log | wc -l
  (count with pipe)

awk '/ERROR/ {print $0}' app.log
  (pattern matching)

grep 'ERROR' app.log | tail -20
  (last 20 error lines)

SYSTEM HEALTH:
df -h
  (disk space — critical to check daily)

free -m
  (memory usage in MB)

top
  (CPU and memory live)

ps -ef | grep application_name
  (check if process running)

uptime
  (server uptime and load average)

netstat -tuln
  (open ports and listening services)

PROCESS MANAGEMENT:
kill -9 PID
  (force kill process)

nohup script.sh &
  (run in background)

ps aux | grep java
  (find Java processes)

FILE OPERATIONS:
find /app/logs -name '*.log'
  -mtime +7 (files older than 7 days)

chmod 755 script.sh
  (permissions)

chown appuser:appgrp file.txt
  (ownership)

wc -l filename.txt
  (count lines — verify file record count)

ARCHIVE AND TRANSFER:
tar -czf backup.tar.gz /app/logs/
cp -r /source /destination
scp file.txt user@server:/path"

Q20: Walk me through a shell script you wrote for automation

Answer:
"One of my most impactful scripts
at CBA was an automated log monitoring
and alerting script.

The problem:
We were manually checking 8 application
log files every morning for errors.
This took 30-45 minutes daily and
errors were sometimes missed.

The script I wrote:

#!/bin/bash

# Daily Log Error Check Script
# Runs via Autosys at 7 AM daily

LOG_DIR='/app/logs'
REPORT_FILE='/tmp/daily_error_report.txt'
EMAIL_LIST='support-team@cba.com.au'
DATE=$(date +%Y-%m-%d)
ERROR_THRESHOLD=10

echo 'Daily Error Report - '$DATE > $REPORT_FILE
echo '=========================' >> $REPORT_FILE

TOTAL_ERRORS=0

for LOG_FILE in $LOG_DIR/*.log; do
    APP_NAME=$(basename $LOG_FILE .log)
    ERROR_COUNT=$(grep -c 'ERROR' $LOG_FILE 2>/dev/null || echo 0)
    TOTAL_ERRORS=$((TOTAL_ERRORS + ERROR_COUNT))

    echo '' >> $REPORT_FILE
    echo 'Application: '$APP_NAME >> $REPORT_FILE
    echo 'Error Count: '$ERROR_COUNT >> $REPORT_FILE

    if [ $ERROR_COUNT -gt $ERROR_THRESHOLD ]; then
        echo 'STATUS: ALERT - Above threshold' >> $REPORT_FILE
        grep 'ERROR' $LOG_FILE | tail -5 >> $REPORT_FILE
    else
        echo 'STATUS: NORMAL' >> $REPORT_FILE
    fi
done

echo '' >> $REPORT_FILE
echo 'Total Errors: '$TOTAL_ERRORS >> $REPORT_FILE

# Send email report
mail -s 'Daily Log Report - '$DATE $EMAIL_LIST < $REPORT_FILE

Result:
→ Morning check time: 30 min → 5 min
→ No errors missed
→ Part of the 40% effort reduction
  I achieved through automation
→ Now runs as Autosys job daily at 7 AM"

Q21: How do you check if a process or service is running on Linux?

Answer:
"Multiple ways depending on the
type of service:

For any process:
ps -ef | grep application_name
→ If output shows the process
  with a real PID it is running
→ If only shows the grep command
  itself it is NOT running

For systemd services (modern Linux):
systemctl status service_name
→ Active: active (running) = OK
→ Active: inactive (dead) = not running
→ Active: failed = crashed

For specific port (is application
listening on expected port?):
netstat -tuln | grep :8080
ss -tuln | grep :8080

Check if application is responding:
curl -s http://localhost:8080/health
→ Returns response = running
→ Connection refused = not running

Check Java processes specifically:
ps aux | grep java
→ Shows all Java processes
→ Check against expected process list

Check by PID file
(many apps write their PID to file):
cat /app/run/myapp.pid
→ Get the PID
kill -0 $(cat /app/run/myapp.pid)
→ Exit 0 = process alive
→ Exit 1 = process dead

At CBA I use a combination —
ps to check process exists,
netstat to verify port is listening,
and curl to verify application
is actually responding to requests.
All three together confirm true health."

Q22: How do you search for a specific error in logs across multiple servers?

Answer:
"Log searching across multiple servers
is a common production support task.

Single server:
grep -i 'ORA-00001' /app/logs/app.log
  (case insensitive search)
grep -n 'ORA-00001' /app/logs/app.log
  (show line numbers)
grep -A 5 'Exception' /app/logs/app.log
  (5 lines AFTER match — context)
grep -B 3 'Exception' /app/logs/app.log
  (3 lines BEFORE match — context)
grep -C 5 'Exception' /app/logs/app.log
  (5 lines before AND after)

Date-specific error search:
grep '2024-01-15.*ERROR' app.log
  (errors on specific date)
grep '2024-01-15 02:' app.log
  (errors in 2 AM hour)

Multiple files on one server:
grep -r 'ERROR' /app/logs/
  (recursive search all files)
grep -l 'ORA-04031' /app/logs/*.log
  (which files contain this error?)

Multiple servers using SSH:
for server in web01 web02 db01; do
    echo 'Checking '$server
    ssh $server 'grep -c ERROR
    /app/logs/app.log'
done

Search compressed old logs:
zgrep 'ERROR' app.log.gz
  (grep inside gzip file)

At CBA we also use centralised
log management where all server
logs are forwarded to a central
platform — I can search across
all servers from one place using
keyword and time filters.
This is much faster than
SSH-ing to each server individually."

Q23: What does this command do: grep -i 'error' app.log | awk '{print $1,$2}' | sort | uniq -c | sort -rn | head -10

Answer:
"This is a log analysis pipeline
and I use commands like this
regularly. Breaking it down:

grep -i 'error' app.log
→ Find all lines containing 'error'
  (case insensitive: Error, ERROR, error)

| awk '{print $1,$2}'
→ From each matching line print
  only field 1 and field 2
→ Typically: date and time
→ Example output: '2024-01-15 02:34:15'

| sort
→ Sort the date-time values
  alphabetically/chronologically

| uniq -c
→ Count consecutive duplicate lines
→ Prepend count to each unique line
→ Output: '    5 2024-01-15 02:34'

| sort -rn
→ Sort numerically (-n) in reverse (-r)
→ Highest counts appear first

| head -10
→ Show only top 10 results

Overall purpose:
Finds which time periods had the
most errors in the application log.

Output example:
     47 2024-01-15 02:34
     23 2024-01-15 02:35
     12 2024-01-15 03:12
      8 2024-01-15 04:01

This tells me the error spike
was between 02:34 and 02:35 AM
on 15th January — I now know
exactly where to focus my
investigation in the logs.

This type of analysis is how
I identify error patterns and
peak failure times quickly."

Q24: How do you check disk space and what do you do when it is nearly full?

Answer:
"Disk space monitoring is critical —
full disk causes application crashes,
batch job failures, and database issues.

Check disk space:
df -h
→ Human readable (GB/MB)
→ Shows all mounted filesystems

df -h /app
→ Specific mount point

Check what is consuming space:
du -sh /app/logs/*
→ Size of each directory/file

du -sh /app/logs/* | sort -rh | head -10
→ Top 10 largest items

Find large files:
find /app -size +1G -type f
  (files over 1GB)

find /app/logs -name '*.log'
  -mtime +30 -size +100M
  (old large log files)

What I do when disk is nearly full:

Immediate actions (buy time):
1. Identify what is consuming space
   du -sh /app/logs/*
2. Archive and compress old logs:
   tar -czf logs_jan2024.tar.gz
   /app/logs/2024-01/
   (then delete originals)
3. Delete old archived files
   that are already backed up
4. Truncate or rotate application logs
   if safe to do so

Alert infra team:
→ Raise ticket for permanent fix:
  increase volume size
  or add mount point

Permanent preventive measures:
→ Set up monitoring alert at 80%
→ Autosys job for weekly log cleanup
→ Log rotation configured (logrotate)
→ Retention policy enforced

At CBA I set up a daily disk
check script that alerts the team
at 80% threshold — we never reach
90%+ any more since implementing this."

Q25: What is the difference between kill, kill -9, and killall?

Answer:
"These commands terminate processes
but with important differences:

kill PID:
→ Sends SIGTERM signal (15) by default
→ Graceful termination request
→ Process CAN ignore this signal
→ Application gets chance to:
  clean up temp files
  close database connections
  flush buffers to disk
  complete current transaction
→ Always try this FIRST
→ Example: kill 12345

kill -9 PID:
→ Sends SIGKILL signal (9)
→ Immediate forced termination
→ Process CANNOT ignore this
→ Kernel kills process immediately
→ No cleanup possible:
  may leave temp files
  may leave DB connections open
  may cause data corruption
→ Use only when kill fails
→ Last resort
→ Example: kill -9 12345

killall process_name:
→ Kills ALL processes with that name
→ Sends SIGTERM by default
→ Example: killall java
  (kills ALL Java processes)
→ Dangerous in production —
  can kill multiple apps at once
→ Use with caution — confirm
  which processes will be killed first:
  ps -ef | grep java

My approach in production:
1. Always try kill (SIGTERM) first
2. Wait 30 seconds
3. Check if process died: ps -ef | grep PID
4. If still running: kill -9

Never use killall in production
without confirming exactly which
processes will be affected."
SECTION 4 — ORACLE DATABASE (Q26-Q32)

Q26: What Oracle database administration tasks do you perform?

Answer:
"In my support role I perform
DBA-adjacent tasks — not full
DBA responsibilities but the
operational tasks that production
support requires.

Daily tasks:

1. Check Oracle alert log for errors:
   tail -100 $ORACLE_BASE/diag/rdbms/
   ORCL/ORCL/trace/alert_ORCL.log
   Look for: ORA- errors, block
   corruption, archivelog issues

2. Monitor tablespace usage:
   SELECT tablespace_name,
   ROUND(used_space * 8192/1024/1024) used_MB,
   ROUND(tablespace_size * 8192/1024/1024) total_MB,
   ROUND(used_percent,2) pct_used
   FROM dba_tablespace_usage_metrics
   ORDER BY pct_used DESC;

3. Check active sessions and locks:
   SELECT s.sid, s.serial#,
   s.username, s.status,
   s.sql_id
   FROM v$session s
   WHERE s.status = 'ACTIVE'
   AND s.username IS NOT NULL;

4. Check long-running queries:
   SELECT s.username, s.sql_id,
   sq.elapsed_time/1000000 elapsed_secs
   FROM v$session s
   JOIN v$sql sq ON s.sql_id = sq.sql_id
   WHERE s.status = 'ACTIVE'
   ORDER BY elapsed_secs DESC;

5. Verify backup status:
   Check RMAN backup logs
   Confirm backup completed nightly

6. Data extraction for incidents:
   Write SELECT queries to
   investigate data issues
   reported by business users"

Q27: What is a tablespace and what do you do when it is full?

Answer:
"A tablespace is a logical storage
container in Oracle database.
It stores tables, indexes, and
other database objects.

Common tablespaces:
→ SYSTEM: Core Oracle data dictionary
→ SYSAUX: Auxiliary Oracle data
→ USERS: Default user objects
→ TEMP: Temporary sort operations
→ UNDOTBS: Undo/rollback data
→ Custom: Application-specific (e.g. CREDIT_RISK_DATA)

Check tablespace usage:
SELECT tablespace_name,
ROUND(used_space * 8192/1024/1024,2) used_MB,
ROUND(tablespace_size * 8192/1024/1024,2) total_MB,
ROUND(used_percent,2) pct_used
FROM dba_tablespace_usage_metrics
ORDER BY pct_used DESC;

When tablespace is nearly full:

Immediate actions:
1. Add a datafile to the tablespace:
   ALTER TABLESPACE CREDIT_RISK_DATA
   ADD DATAFILE '/u01/oradata/credit_risk_data02.dbf'
   SIZE 2G AUTOEXTEND ON NEXT 512M
   MAXSIZE 10G;
   (This is done by DBA — I raise
   the request and get approval)

2. Enable autoextend if not on:
   ALTER DATABASE DATAFILE
   '/u01/oradata/credit_risk_data01.dbf'
   AUTOEXTEND ON NEXT 256M MAXSIZE 5G;

3. Purge unnecessary data:
   Work with DBA to identify and
   archive old data if retention
   policy allows

4. TEMP tablespace full specifically:
   May indicate runaway sort operation
   Kill the session:
   ALTER SYSTEM KILL SESSION 'SID,SERIAL#';

Prevention:
→ Alert at 80% threshold
→ Autosys job to check weekly
→ Regular purge of old data
→ Capacity planning quarterly review"

Q28: What Oracle errors have you encountered most in production?

Answer:
"From my 4+ years at CBA these are
the most common Oracle errors
and how I handle them:

ORA-00942: Table or view does not exist
→ Cause: Wrong schema, wrong table name,
  missing synonym, or permission issue
→ Fix: Verify table name, check grants,
  create synonym if needed

ORA-01555: Snapshot too old
→ Cause: Long-running query, undo
  tablespace too small or retention low
→ Fix: Increase UNDO retention,
  reschedule long queries,
  increase undo tablespace
→ Common in batch jobs doing
  large data reads

ORA-04031: Unable to allocate shared memory
→ Cause: Shared pool full (SGA issue)
→ Fix: Flush shared pool (DBA action),
  increase SGA, investigate
  memory leak in application

ORA-00060: Deadlock detected
→ Cause: Two sessions waiting for
  each other's locks
→ Fix: Oracle auto-resolves by
  killing one session
→ Need to investigate why deadlock
  occurs and fix application logic

ORA-12170: TNS connect timeout occurred
→ Cause: Database listener not running,
  network issue, wrong host/port
→ Fix: Check listener status,
  check network, verify connection string

ORA-01652: Unable to extend temp segment
→ Cause: TEMP tablespace full
→ Fix: Kill large sort operation,
  add space to TEMP tablespace

ORA-00001: Unique constraint violated
→ Cause: Duplicate key being inserted
→ Fix: Application or data issue —
  escalate to development team"

Q29: How do you find and kill a locking session in Oracle?

Answer:
"Database locks blocking other sessions
are a common production issue that
I resolve regularly.

Step 1: Identify the lock:
SELECT
  l.sid blocking_sid,
  l.serial# blocking_serial,
  s.username blocking_user,
  l.type lock_type,
  o.object_name locked_object
FROM v$lock l
JOIN v$session s ON l.sid = s.sid
JOIN dba_objects o ON l.id1 = o.object_id
WHERE l.block = 1;

Step 2: Find who is waiting:
SELECT
  w.sid waiting_sid,
  ws.username waiting_user,
  b.sid blocking_sid,
  bs.username blocking_user
FROM v$lock w
JOIN v$session ws ON w.sid = ws.sid
JOIN v$lock b ON w.id1 = b.id1
  AND b.block = 1
JOIN v$session bs ON b.sid = bs.sid
WHERE w.request > 0;

Step 3: Review what the blocker is doing:
SELECT sq.sql_text
FROM v$session s
JOIN v$sql sq ON s.sql_id = sq.sql_id
WHERE s.sid = [blocking_sid];

Step 4: Decision
→ Is the blocking session doing
  legitimate long-running work?
  → Wait if near completion
→ Is it a hung/idle session?
  → Kill it

Step 5: Kill the blocking session:
ALTER SYSTEM KILL SESSION 'SID,SERIAL#';
-- Example:
ALTER SYSTEM KILL SESSION '45,1234';

Step 6: Verify lock released:
→ Rerun the lock query — should be empty
→ Confirm waiting sessions proceed

Note: I always get DBA or
application owner confirmation
before killing a session in
production — it can roll back
a long transaction."

Q30: What SQL queries do you commonly write for production support?

Answer:
"I write SQL daily for investigation
and data validation.

Common queries in my role:

Record count validation:
SELECT COUNT(*)
FROM transactions
WHERE process_date = TRUNC(SYSDATE);
(Verify batch loaded expected records)

Data quality check:
SELECT COUNT(*)
FROM transactions
WHERE amount IS NULL
OR customer_id IS NULL
OR process_date IS NULL;
(Check for unexpected nulls)

Find records processed in last hour:
SELECT COUNT(*), MIN(created_dt),
MAX(created_dt)
FROM transactions
WHERE created_dt >= SYSDATE - 1/24;

Duplicate detection:
SELECT customer_id, trade_date,
COUNT(*) cnt
FROM trades
GROUP BY customer_id, trade_date
HAVING COUNT(*) > 1;

Latest record per customer:
SELECT *
FROM transactions t
WHERE created_dt = (
  SELECT MAX(created_dt)
  FROM transactions
  WHERE customer_id = t.customer_id
);

Check data for specific date range:
SELECT trade_date, COUNT(*), SUM(amount)
FROM trades
WHERE trade_date BETWEEN
  TO_DATE('01-JAN-2024','DD-MON-YYYY')
  AND TO_DATE('31-JAN-2024','DD-MON-YYYY')
GROUP BY trade_date
ORDER BY trade_date;

Reconciliation query:
SELECT
  a.total_source,
  b.total_target,
  a.total_source - b.total_target variance
FROM
  (SELECT SUM(amount) total_source FROM source_table) a,
  (SELECT SUM(amount) total_target FROM target_table) b;
(Verify source and target match after ETL)"

Q31: What is the difference between DELETE, TRUNCATE, and DROP?

Answer:
"Critical to know — wrong choice
in production can cause disaster.

DELETE:
→ DML statement
→ Removes rows one by one
→ CAN be rolled back (inside transaction)
→ Fires triggers
→ WHERE clause to delete specific rows:
  DELETE FROM temp_data
  WHERE process_date < TRUNC(SYSDATE)-30;
→ Slow for large tables
→ Undo logs generated
→ High-water mark NOT reset

TRUNCATE:
→ DDL statement
→ Removes ALL rows instantly
→ CANNOT be rolled back (implicit commit)
→ Does NOT fire triggers
→ No WHERE clause
→ Much faster than DELETE for full table
→ Resets high-water mark
→ Example:
  TRUNCATE TABLE staging_table;
→ Use for clearing staging tables
  before batch load

DROP:
→ DDL statement
→ Removes the TABLE ITSELF
  (not just the data — the structure too)
→ CANNOT be rolled back
→ Table goes to RECYCLE BIN
  (can be recovered: FLASHBACK TABLE)
→ Example:
  DROP TABLE old_archive_table;
→ Use when table no longer needed

My production rule:
→ DELETE when I need WHERE clause
  or need rollback option
→ TRUNCATE when clearing entire
  staging table (safe, fast)
→ NEVER DROP in production without
  explicit DBA and business approval
  and confirmed backup"

Q32: What is your experience with database backup and recovery?

Answer:
"At CBA I do not perform RMAN backups
myself — that is the DBA team's
responsibility. But I work with
backup and recovery regularly
from a support perspective.

What I do:

Verify backup completion:
→ Check nightly RMAN backup logs
→ Verify backup job SUCCESS in Autosys
→ Alert DBA team if backup fails
→ Track backup SLA (backup must
  complete by 6 AM daily)

Backup log check:
tail -50 /app/logs/rman_backup.log
→ Look for: 'backup completed'
→ Look for errors: 'ORA-', 'RMAN-'

Recovery scenarios I handle:

Data recovery request:
→ Business user: 'We deleted records
  by mistake last night'
→ I raise request to DBA team
  with: table name, time of deletion,
  approximate row count
→ DBA uses RMAN or Flashback:
  SELECT * FROM table_name
  AS OF TIMESTAMP (SYSTIMESTAMP - INTERVAL '2' HOUR);
  (Flashback query — my team uses this)

Point-in-time recovery:
→ Escalated to DBA for full PITR
→ I coordinate: define exact recovery
  point, notify business of outage
  window, verify data after recovery

Export/Import for data migration:
→ Oracle Data Pump (expdp/impdp)
→ Used for moving data between
  environments: PROD → UAT refresh

Key knowledge:
→ Full backup: complete database
→ Incremental backup: changes since last
→ Archive logs: required for PITR
→ RMAN: Oracle's backup tool
→ Flashback: quick point-in-time queries"
SECTION 5 — SERVICENOW & ITSM (Q33-Q38)

Q33: Walk me through how you use ServiceNow in your daily work

Answer:
"ServiceNow is the backbone of
our ITSM operations at CBA and
I use it throughout my day.

Morning:
→ Check incident queue:
  Filter by assignment group,
  priority order P1 → P4
→ Check SLA timers — any near breach?
→ Review overnight incidents
  resolved by night shift
→ Read handover notes

During shift:

Incident Management:
→ New alert fires → Create incident
→ Fill: Category, subcategory,
  CI (Configuration Item from CMDB),
  impact, urgency
→ ServiceNow auto-calculates priority
→ Assign to correct team
→ Work notes: internal updates
→ Customer notes: external updates
→ Update every 30 mins on P1/P2

Problem Management:
→ Recurring incidents get linked
  to a Problem ticket
→ Problem ticket tracks RCA
  and permanent fix
→ Known errors documented
  in Known Error Database (KEDB)

Change Management:
→ Raise change requests
→ Link to release schedule
→ CAB review workflow
→ Implementation record post-change

CMDB:
→ Configuration Items linked to incidents
→ Helps identify impact of CI failures
→ Helps identify related incidents

Reporting:
→ Weekly incident summary reports
→ SLA compliance reports
→ MTTR trend reports

Knowledge Base:
→ Create articles after P1/P2 resolution
→ Articles help team resolve faster
  next time
→ Reduces escalations"

Q34: What is ITIL and how do you apply it in your work?

Answer:
"ITIL — IT Infrastructure Library —
is a framework of best practices
for IT service management.
I apply ITIL principles daily.

Key ITIL processes I use:

Incident Management:
→ Restore service as quickly as possible
→ Minimise business impact
→ ITIL priority matrix:
  Impact (how many users) X
  Urgency (how time-sensitive)
  = Priority (P1-P4)

Problem Management:
→ Find root cause of recurring incidents
→ Prevent future occurrence
→ Known Error Database (KEDB) in ServiceNow

Change Management:
→ Control changes to minimise risk
→ Change types: Standard, Normal, Emergency
→ CAB review and approval
→ Rollback plan mandatory

Service Level Management:
→ Monitor against agreed SLAs
→ Report breaches
→ Escalate near-breaches proactively

Knowledge Management:
→ Capture resolution steps
→ Knowledge base in ServiceNow
→ Continuous improvement of articles

Configuration Management (CMDB):
→ Track all CIs and relationships
→ Impact analysis for incidents
→ Accurate CMDB helps faster resolution

Continual Service Improvement:
→ Monthly review of incident trends
→ Identify top recurring issues
→ Drive permanent fixes
→ This led to our 30% reduction
  in repeat escalations

I am planning to formalise this
with ITIL 4 Foundation certification
as my next professional development step."

Q35: What is the difference between an Incident and a Problem in ITIL?

Answer:
"This is a fundamental ITIL concept
and critical to get right.

INCIDENT:
→ Unplanned interruption or degradation
  of an IT service
→ Focus: RESTORE service FAST
→ Root cause not the priority
→ Closed when service is restored
→ Example: Application down at 2 AM
→ ServiceNow: INC0012345

PROBLEM:
→ The underlying cause of one or
  more incidents
→ Focus: PREVENT future incidents
→ Root cause IS the priority
→ Can stay open for weeks during
  investigation
→ Results in: Known Error or permanent fix
→ Example: Memory leak causing
  application crashes every 3 days
→ ServiceNow: PRB0001234

Relationship:
One PROBLEM → can cause → Many INCIDENTS

Timeline:
INC → Resolved (service restored)
PRB → Root cause found → Known Error
Known Error → Fix developed → Change
Change → Implemented → PRB Closed

Example from my experience:
Multiple incidents of DB connection
failures (INC tickets each time)
→ Linked to one Problem ticket
→ RCA identified: connection pool
  not recycling properly
→ Known Error raised
→ Development fix raised as Change
→ Fix deployed → No more incidents
→ Problem closed

Managing the distinction is important
because: fixing incidents without
Problem management means the same
issue keeps coming back and consuming
support time repeatedly."

Q36: How do you manage stakeholder communication during a major incident?

Answer:
"Stakeholder communication during
a P1 is just as important as the
technical resolution. Poor
communication loses trust even
if you fix the issue quickly.

My communication approach:

First 5 minutes — Initial notification:
Email/Teams message to all stakeholders:
'[P1 INCIDENT ACTIVE]
Application: Credit Risk Portal
Impact: Users unable to log in
Started: 02:34 AM EST
We are investigating. Next update: 03:00 AM'

Every 30 minutes — Status update:
'[P1 UPDATE - 03:00 AM]
Status: Investigating
Finding: Database connection pool
  exhausted — root cause being identified
ETA to resolve: Approx 03:30 AM
Next update: 03:30 AM'

On resolution — All-clear:
'[P1 RESOLVED - 03:28 AM]
Application: Credit Risk Portal
Resolution: Connection pool reset,
  application restarted
Duration: 54 minutes
All users can now log in normally
Post-incident review: Tomorrow 10 AM
Thank you for your patience.'

Key principles:
→ Never go silent — no update IS an update
  (a bad one)
→ Give specific ETAs even if uncertain:
  'Approximately 30-45 minutes'
  is better than 'unknown'
→ Use plain language — business
  stakeholders do not want
  technical jargon
→ Acknowledge business impact explicitly:
  'We understand this is impacting
  your morning reporting deadline'
→ Own the communication — do not
  make stakeholders chase you

After the incident:
→ Post-Incident Review invitation sent
→ Full timeline and RCA shared
→ Prevention actions committed with dates"

Q37: What is a Post-Incident Review (PIR) and how do you conduct one?

Answer:
"A Post-Incident Review — also called
Post-Mortem or PIR — is a structured
review of a significant incident
to learn from it and prevent recurrence.

We conduct PIRs for all P1 incidents
and significant P2s.

When:
→ Within 24-48 hours of P1 resolution
→ While details are still fresh
→ All key participants available

Who attends:
→ Support team members who worked the incident
→ Development team (if they were involved)
→ DBA (if database issue)
→ Infrastructure (if server issue)
→ Service manager / application owner

PIR structure I follow:

1. Incident timeline (10 minutes)
→ When was issue detected?
→ When was impact confirmed?
→ When was resolution found?
→ When was service restored?
→ Factual — no blame at this stage

2. Impact assessment (5 minutes)
→ How many users affected?
→ What business processes impacted?
→ Any financial or regulatory impact?
→ Total outage duration?

3. Root cause (15 minutes)
→ What was the technical root cause?
→ Why did it happen?
→ Could monitoring have caught it earlier?

4. What went well (5 minutes)
→ Celebrate what worked
→ Fast detection? Good comms?
→ Quick escalation?

5. What could be better (10 minutes)
→ Gaps in monitoring?
→ Runbook missing a step?
→ Wrong team engaged first?
→ Communication delays?

6. Action items (10 minutes)
→ Specific, measurable actions
→ Owner assigned to each
→ Due date for each
→ Tracked in ServiceNow Problem ticket

My PIR output is a document that goes
to the application owner and service
manager. Action items reviewed
in next monthly service review."

Q38: How do you handle a situation where you missed an SLA?

Answer:
"Missing an SLA is serious in a
banking environment. How you handle
it matters as much as preventing it.

Immediate response:
→ Acknowledge the breach honestly —
  do not minimise or make excuses
→ Notify service manager immediately
→ Focus first on resolving the incident
  before explaining the breach

Post-resolution — explain what happened:
→ What was the incident?
→ When was it raised?
→ When was it resolved?
→ By how much was SLA missed?
→ What were the contributing factors?

Honest contributing factors I would cite:
→ Incorrect initial categorisation
  (P3 should have been P2)
→ Alert notification delayed
  (monitoring gap identified)
→ Wrong team engaged first
  (escalation matrix unclear)
→ Complexity not anticipated
  (fair if genuinely complex)

What I would NOT say:
→ 'The SLA is too tight' — not helpful
→ 'It was not our fault' — ownership
→ 'The development team was slow'
  — blame culture

Action items after missed SLA:
→ Identify specific gap that caused breach
→ Fix that specific gap
→ Update runbook if process gap
→ Review categorisation guidelines
  if mis-categorised
→ Follow up in next service review

Track and report:
→ SLA breach logged in ServiceNow
→ Root cause documented
→ Prevention action tracked

The goal is: this specific
type of breach never happens again.
One missed SLA that leads to
a permanent improvement is more
valuable than hiding the issue."
SECTION 6 — SOX COMPLIANCE & AUDIT (Q39-Q42)

Q39: What is SOX compliance and what does it mean for your work?

Answer:
"SOX — Sarbanes-Oxley Act — is a
US federal law that sets requirements
for financial reporting and internal
controls for publicly traded companies.
CBA as an Australian bank that
operates globally follows SOX
equivalent standards.

What SOX means for application support:

Access Control:
→ Least privilege principle: everyone
  gets only the access they need
→ No shared accounts — individual
  user IDs for every person
→ Regular access reviews (quarterly)
→ Immediate revocation on termination
→ Privileged access requires approval
  and is time-limited

Change Management:
→ ALL changes must be approved
→ Separation of duties: developer
  cannot deploy their own code
→ Change records must be complete
  and accurate
→ Emergency changes require
  post-implementation review

Audit Trails:
→ All actions logged with user ID
  and timestamp
→ Log files must not be modifiable
→ Audit logs retained for required period
→ Regular log reviews

My specific SOX activities:
→ Quarterly user access review:
  Confirm all users on access list
  still need that access
→ Evidence collection for auditors:
  Change records, access logs,
  approval records
→ Ensure no developer has direct
  production access
→ Zero unauthorised changes — every
  production change has an approved CR

Result: Zero audit findings across
two consecutive SOX audits in my tenure."

Q40: What do you do when an auditor asks for evidence?

Answer:
"Audit evidence requests are common
in my banking environment and I
handle them regularly.

Common audit evidence requests:

1. Change Management Evidence:
Auditor asks: 'Provide all changes
deployed to production in Q3 2024
with approvals'
→ Export from ServiceNow:
  Filter changes by date range,
  environment = Production,
  Status = Closed-Successful
→ Export includes: CR number,
  approver names, approval dates,
  implementation dates, results
→ Provide as CSV or PDF

2. Access Control Evidence:
Auditor asks: 'Who has production
database access and when was it last reviewed?'
→ Pull user access list from
  Oracle database:
  SELECT * FROM dba_users WHERE account_status = 'OPEN';
  SELECT grantee, granted_role FROM dba_role_privs;
→ Access review records from
  last quarterly review

3. Incident Response Evidence:
Auditor asks: 'Show us your P1
incident from March with timeline and RCA'
→ Export ServiceNow incident record
→ Include: timeline, work notes,
  resolution, PIR document

4. Backup Evidence:
→ RMAN backup logs
→ Recovery test records

My approach:
→ Keep audit evidence organised —
  I maintain a folder structure
  by quarter for all evidence
→ Never provide more than asked —
  scope creep in audits is risky
→ If uncertain about a request:
  escalate to service manager
  before responding
→ Meet evidence deadlines — late
  responses raise red flags with auditors"
SECTION 7 — SCENARIO BASED (Q41-Q50)

Q41: SCENARIO — Application is down at 2 AM. Walk me through exactly what you do

Answer:
"This is my routine — I have
handled dozens of 2 AM P1s.

0:00 — Alert received
→ PagerDuty fires on my phone
→ Acknowledge within 2 minutes
→ VPN connected, laptop open

0:02 — Initial assessment
→ Open ServiceNow — is there already
  an incident or do I need to create?
→ Check monitoring dashboard:
  What exactly is down?
  Whole application or one component?
→ Try to access application myself:
  curl -s http://appserver:8080/health

0:05 — First response
→ Create P1 ServiceNow incident if not exists
→ Send initial notification to
  incident channel:
  'P1 ACTIVE: Application X unreachable
   as of 02:01 AM. Investigating.
   Update in 15 mins.'

0:05 to 0:20 — Investigation
→ SSH to application server
→ Check if app process is running:
  ps -ef | grep appname
→ Check application logs:
  tail -100 /app/logs/app.log | grep -i error
→ Check disk space (common cause):
  df -h
→ Check if Autosys jobs are hung:
  autorep -J BOX_APP_JOBS -s
→ Check database connectivity:
  sqlplus -s user/pass@db
  'select 1 from dual;'
→ Check server resources: top, free -m

0:20 — Decision point
Based on findings:

If app process died:
→ Check for OOME (out of memory):
  grep 'OutOfMemory' app.log
→ Check heap dump generated?
→ Restart application:
  sudo systemctl restart appservice
→ Monitor startup: tail -f app.log

If database issue:
→ Wake up DBA on-call immediately
→ Do not attempt DB fixes alone

If disk full:
→ Clear log archives:
  find /app/logs -name '*.log.gz'
  -mtime +7 -delete
→ Restart application

0:45 — Resolution or escalation
→ Service restored: send all-clear
→ Not resolved: wake up development
  lead — full war room

Post-resolution:
→ Update ServiceNow ticket
→ All-clear communication
→ Schedule PIR for next morning"

Q42: SCENARIO — Business reports data missing from a report for yesterday. How do you investigate?

Answer:
"Data missing from reports is a
common and serious issue in banking.
Systematic investigation:

Step 1: Understand the problem exactly
→ Which report?
→ What data is missing?
  All data or specific subset?
→ What date range is affected?
→ When was the issue noticed?
→ Was yesterday's report correct?
  (Is this new or ongoing?)

Step 2: Check the ETL/batch process
→ Did the batch job run for that date?
  autorep -J BATCH_JOB_NAME -s
→ Did it complete with SUCCESS or FAILURE?
→ Check job log for errors:
  grep -i 'error\|warning\|records' /app/logs/batch.log

Step 3: Check source data
→ Did source data arrive?
  ls -la /app/inbound/data_20240115.csv
→ Record count in source file:
  wc -l /app/inbound/data_20240115.csv
→ Is count as expected?

Step 4: Check database
→ How many records loaded vs expected?
  SELECT COUNT(*) FROM fact_table
  WHERE process_date = TO_DATE('15-JAN-2024','DD-MON-YYYY');
→ Are records there but filtered
  incorrectly in the report?
  Run the report SQL directly to check

Step 5: Check report itself
→ Is the report filtering correctly?
→ Date parameter correct?
→ Has report SQL changed recently?
  (Check change records)

Step 6: Communicate finding
→ Inform business with specific answer:
  'Source file received 50,000 records.
   Batch processed 49,800. 200 records
   rejected due to validation errors.
   I am investigating the rejections.
   ETA: 30 minutes.'

Step 7: Resolution
→ If batch failed: rerun
→ If records rejected: fix and rerun
→ If report bug: escalate to dev
→ If data issue in source: notify upstream"

Q43: SCENARIO — You notice a pattern of the same incident occurring every Monday. What do you do?

Answer:
"A repeating pattern is a textbook
Problem Management scenario.

Step 1: Confirm the pattern
→ Review last 4-6 Monday incidents
→ Document: exactly what fails,
  exactly what time, exact error
→ Is it always the same application?
→ Is it always the same component?

Step 2: Ask key questions
→ What runs specifically on Mondays?
→ Is there a weekly batch job?
→ Is there a weekly maintenance window?
→ Does more users come online Monday?
→ Is there a weekly data feed arriving?
→ Did anything change recently?

Step 3: Raise a Problem ticket
→ ServiceNow Problem record
→ Link all the related Monday incidents
→ Document the pattern clearly:
  'Occurred 4 consecutive Mondays
   at approximately 08:30 AM EST.
   Same error: database connection
   timeout on batch_weekly_job.'

Step 4: Root cause investigation
→ Check Autosys: what runs at 08:30 Mondays?
→ Check database: any heavy queries?
→ Check if any batch job runs weekly
  and competes for resources
→ Review server metrics from past Mondays:
  CPU, memory, I/O at 08:30 AM

Step 5: Identify root cause
In my experience this turned out to be:
→ Weekly statistics gathering job running
  same time as business users logging in
→ Resource contention causing timeouts

Step 6: Permanent fix
→ Reschedule statistics job to 06:00 AM
→ Change implemented via Change Request

Step 7: Verify
→ Next Monday: monitor at 08:30 AM
→ No incident = fix confirmed
→ Close Problem ticket after 2-3
  incident-free Mondays

Step 8: Knowledge article
→ Document the pattern and fix
→ Future support team knows
  what to check if Monday issues recur"

Q44: SCENARIO — A change was deployed and immediately caused issues. What do you do?

Answer:
"Post-change incidents are urgent —
rollback may be the fastest path
to service restoration.

First 5 minutes:
→ Confirm correlation: issue started
  immediately after change deployment
→ Check change record: What was changed?
  What files? What config? What DB?

Decision: Rollback or fix-forward?

Rollback if:
→ Rollback plan exists (it always should)
→ Rollback is fast (< 15 minutes)
→ Root cause not yet clear
→ Business impact is high

Fix-forward if:
→ Simple config change that can be
  quickly corrected
→ Rollback would cause data issues
  (if DB changes involved)
→ Team knows exactly what is wrong

Rollback process:
→ Notify all stakeholders:
  'Rolling back change DEP-12345
   due to production impact.
   ETA to restore: 15 minutes.'
→ Follow rollback steps from change record
→ Verify service restored
→ Confirm with business

Post-rollback:
→ Update ServiceNow change record:
  Status = Failed, Rolled Back
→ Create incident linked to change
→ Notify application owner and manager
→ Schedule emergency review:
  What caused the issue?
  What testing was missed?
  When can we redeploy (fixed)?

Prevention:
→ Was this change tested in staging?
→ Was the test environment representative?
→ Was rollback plan tested?
→ Was deployment done in correct window?
→ Were the right people on the bridge call?

Honest assessment:
→ In banking: ANY production issue
  after a change is treated seriously
→ Even if change is not the cause —
  timing correlation means it must
  be investigated before ruling out"

Q45: SCENARIO — You are new to a team and production goes down on your first week. How do you handle it?

Answer:
"This tests your composure and
your ability to contribute
even without deep context.

What I would do:

Immediately:
→ Announce yourself clearly:
  'I am Prabal, new to the team.
   I am here to help. Tell me
   what you need from me.'
→ Do not pretend to know things
  you do not know
→ Do not disappear — your presence
  and support matters

Listen and learn:
→ Let experienced team members lead
→ Watch and understand the process
→ Ask quick clarifying questions
  only when needed: 'Where are the logs?'
  'Which server should I check?'

Take on tasks assigned to you:
→ 'Can you monitor the batch jobs
  while we handle the DB issue?'
→ 'Can you update the stakeholder
  communication every 15 minutes?'
→ 'Can you check the disk space
  on all three servers?'
→ Take ownership of whatever you are given
→ Report back quickly and clearly

Communicate what you see:
→ 'I see 50,000 ERROR lines in this log
  starting at 02:34 AM'
→ Even new to the team: fresh eyes
  sometimes catch things others miss

After resolution:
→ Read the PIR document carefully
→ Ask questions about decisions made:
  'Why did we rollback vs fix-forward?'
→ Update your own notes for next time

What NOT to do:
→ Panic or freeze
→ Make changes without guidance
→ Disappear to 'read documentation'
→ Stay silent because you are new

Every experienced support engineer
was once new in a P1.
What matters is attitude and effort."

Q46: How do you keep your skills current in production support?

Answer:
"The production support landscape
evolves constantly and I stay
current through:

On the job learning:
→ Every P1 and complex incident
  teaches something new
→ PIR reviews build pattern recognition
→ Cross-training with colleagues
  on different application areas

Self-directed learning:
→ Read Oracle documentation
  for new error codes I encounter
→ Linux man pages for commands
→ Autosys documentation for
  advanced features
→ ServiceNow release notes
  (new features quarterly)

Community and forums:
→ Stack Overflow for Linux/SQL questions
→ Oracle support community for ORA- errors
→ ITIL community resources

Certifications planned:
→ ITIL 4 Foundation: formalises
  the ITSM practices I already use
→ AWS Cloud Practitioner: cloud
  awareness for where infrastructure
  is moving

Internal knowledge:
→ Read knowledge base articles
  written by senior colleagues
→ Shadow senior engineers on
  complex P1s when possible
→ Volunteer for cross-team
  projects to learn adjacent systems

Documentation habit:
→ Every complex resolution
  I document in detail
→ This forces me to understand
  what I did and why
→ Six months later that article
  saves an hour of investigation
  for a junior team member"

Q47: What is your experience with Salesforce in production support?

Answer:
"In my role at CBA I use Salesforce
alongside ServiceNow for case management.

How I use Salesforce:

Case Management:
→ Business users and relationship managers
  log support cases in Salesforce
→ Cases come to our support queue
→ I triage, investigate, and update
  cases within Salesforce

Case lifecycle in Salesforce:
→ New: Just logged by user
→ In Progress: Being investigated
→ Pending: Waiting on info from user
→ Resolved: Fix applied
→ Closed: User confirmed resolution

What I handle in Salesforce:
→ Data query issues:
  'The account balance is wrong'
  → I check Oracle DB to verify data
  → Identify if application or data issue
→ Access issues:
  'I cannot see the dashboard'
  → Permission/role issue
  → Check Salesforce profile or
    application access
→ Application errors:
  'Getting error when submitting report'
  → Check application logs
  → Replicate the error if possible
  → Escalate to development

Integration between ServiceNow and Salesforce:
→ Complex technical issues raised
  in Salesforce get mirrored in
  ServiceNow as incidents
→ Ensures ITSM tracking and SLA
  management applies to all issues

I use Salesforce primarily as a
case management and communication
tool rather than for Salesforce
administration or development."

Q48: How do you document a resolution for the knowledge base?

Answer:
"Good knowledge base articles are
one of the most valuable things
a support engineer can produce.
I have written 50+ articles at CBA.

My knowledge base article structure:

Title:
Clear and searchable — use the
exact error message if applicable:
'Autosys Job CREDIT_RISK_EXTRACT
fails with ORA-12170'
(Not: 'Database connection issue')

Summary (2-3 lines):
What the issue is and when it occurs.
'This article covers the resolution
for ORA-12170 TNS timeout errors
occurring during the nightly
CREDIT_RISK_EXTRACT Autosys job,
typically between 01:00-03:00 AM.'

Symptoms:
Exactly what the engineer sees:
→ Autosys job status: FAILURE
→ Exit code: 1
→ Log location: /app/logs/extract.log
→ Log error: ORA-12170: TNS:Connect
  timeout occurred

Root Cause:
What actually caused it:
'Oracle listener service becomes
unresponsive under high connection
load during nightly batch window.
Typically occurs when more than
80 concurrent sessions hit the DB.'

Resolution Steps (numbered):
1. Check if listener is running:
   lsnrctl status
2. If listener down: restart it:
   lsnrctl start
3. Verify listener responding:
   tnsping ORCL
4. Restart Autosys job:
   sendevent -J CREDIT_RISK_EXTRACT
   -E STARTJOB
5. Monitor job to completion:
   autorep -J CREDIT_RISK_EXTRACT -s

Escalation:
If steps above do not resolve:
→ Escalate to DBA team (contact: DBA-support)
→ Provide: listener log, alert log,
  session count at time of failure

Prevention:
→ DBA to review listener configuration
→ Connection pool review recommended

This structure means any team member
can resolve this at 2 AM without
needing to call me or escalate."

Q49: Where do you see yourself in 3 years?

Answer:
"In 3 years I want to have grown
from a solid production support
specialist into a senior application
support lead or service delivery role.

Specifically I want to:

Technical depth:
→ Become the go-to expert for
  complex Oracle database issues
  in the support context
→ Deepen my Linux and automation
  skills — more sophisticated
  monitoring and scripting
→ Build cloud platform knowledge
  as infrastructure migrates to AWS/Azure

Functional growth:
→ ITIL 4 certified — formalise
  the ITSM knowledge I have built
→ Lead PIR sessions rather than
  just attend them
→ Own service improvement initiatives:
  identify patterns, drive fixes

Leadership:
→ Mentor newer support engineers
→ Build and maintain the knowledge base
  as a team resource not just my own
→ Be the first call for the team
  on complex incidents — not because
  I have to be but because I have
  earned that trust

What this organisation can give me:
→ Exposure to more complex systems
→ Opportunity to work with
  more experienced engineers
→ Structured career progression
→ Challenging production environment
  that keeps skills sharp

I am not someone who wants to
stay still — every year I want
to be meaningfully better than
the year before."

Q50: Do you have any questions for us?

Answer — Always ask 2-3 strong questions:

Question 1 (About the role):
"What does a typical first 90 days
look like for someone joining this
team? Is there a structured onboarding
to the applications and environments
or is it more learn-by-doing?"

Question 2 (About the team):
"What is the current biggest
operational challenge the support
team is facing — whether that is
a specific application, a tooling
gap, or a process improvement area?"

Question 3 (About growth):
"How does the organisation support
production support engineers who
want to grow — are there opportunities
to move into senior support roles
or adjacent areas like release
management or service delivery?"

Question 4 (About the environment):
"What is the on-call rotation like?
How many people share on-call duties
and what is the typical frequency
of after-hours incidents?"

Why these questions work:
→ Question 1: Shows you are
  serious about succeeding in the role
→ Question 2: Shows commercial awareness
  and problem-solving orientation
→ Question 3: Shows ambition
  without seeming impatient
→ Question 4: Shows you are realistic
  and want to set clear expectations

Never ask about salary in first interview.
Never say 'No I have no questions.'
Questions show engagement and interest.
No questions sends the wrong signal."
INTERVIEW CHEAT SHEET
YOUR 5 KEY NUMBERS — MEMORISE THESE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ 4+ years production support
→ 99.9% application uptime
→ 35% MTTR reduction
→ 40% manual effort reduced
→ 100+ Autosys jobs managed
→ 50+ knowledge base articles
→ Zero SOX audit findings
→ Zero unauthorised changes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUESTIONS MOST LIKELY TO BE ASKED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ Tell me about your experience (Q1)
⭐ How do you handle a P1? (Q4)
⭐ What do you do when Autosys fails? (Q12)
⭐ Linux commands you use? (Q19)
⭐ Oracle errors encountered? (Q28)
⭐ What is ITIL? (Q34)
⭐ Scenario: App down at 2 AM (Q41)
⭐ What is your greatest achievement?
   → 99.9% uptime / 35% MTTR reduction
⭐ What is your weakness?
   → Limited cloud hands-on experience
     actively addressing with learning
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GOLDEN ANSWER FORMULA:
Every answer = Situation + Action + Result
→ What was the problem?
→ What did YOU specifically do?
→ What was the measurable outcome?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STAY CALM. YOU KNOW THIS WORK.
YOU DO IT EVERY DAY. 🚀