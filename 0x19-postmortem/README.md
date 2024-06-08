Postmortem: Outage Incident

Issue Summary:

Duration: The outage occurred from 10:00 AM to 12:30 PM (UTC-7) on June 8, 2024.
Impact: The AcmeCor website experienced complete unavailability during the outage. Users attempting to access the site encountered HTTP 503 errors. Approximately 30% of users were affected.
Root Cause: A misconfigured caching layer caused excessive memory consumption, leading to server crashes.
Timeline:

10:00 AM: Monitoring system triggered an alert due to unresponsiveness.
10:15 AM: Engineers noticed increased latency and began investigating.
10:30 AM: Assumed root cause: Database overload due to high traffic.
11:00 AM: Investigated database performance, but no issues found.
11:30 AM: Escalated incident to senior infrastructure team.
12:00 PM: Realized cache misconfiguration was causing memory leaks.
12:30 PM: Fixed cache settings and restarted servers.
Root Cause and Resolution:

Cause: The cache expiration time was set too long, causing memory leakage.
Fix: Adjusted cache settings to ensure timely expiration.
Corrective and Preventative Measures:

Improvements:
Implement automated cache expiration checks.
Enhance monitoring for memory usage.
Regularly review caching configurations.
Tasks:
Patch Nginx server to enforce cache expiration.
Add memory monitoring alerts.
Document cache configuration best practices.
