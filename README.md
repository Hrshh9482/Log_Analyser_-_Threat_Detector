# Log Analyser & Threat Detector

A Python-based security log analysis tool that detects threats and generates a threat report from system logs.

## Features
- Detects failed login attempts
- Identifies privilege escalation attempts (sudo, administrator)
- Brute force detection (threshold: 5+ failed logins)
- Tracks unique attacker IPs
- Identifies top attacker by attempt count
- Risk level assessment (Low / Medium / High / Critical)

## Usage
```bash
python log_analyser.py <logfile>
```

## Example
```bash
python log_analyser.py auth.log
```

## Sample Output
----------------------------
       Threat Report        
----------------------------
Failed Logins : 76
 
Privilege Escalations : 3
 
Possible Brute Force :
YES
 

Unique Attackers : 10

Top Attacker :
192.168.1.15
28 attempts
Risk Level : Critical
----------------------------

## Skills Demonstrated
- Python scripting
- Regex pattern matching
- Log analysis
- Threat detection logic
- Blue team security concepts

## Tools & Libraries
- Python 3
- `re` module
- `sys` module
