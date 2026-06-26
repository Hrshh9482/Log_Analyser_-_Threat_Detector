import re
import sys
print("----------------------------")
print("       Threat Report        ")
print("----------------------------")

file = sys.argv[1]

with open(file, "r") as f:
    content = f.readlines()

failed_count = 0
priv_escalate = 0
for line in content:
    if re.search(r'\bFailed\b', line, re.IGNORECASE):
        failed_count+=1
    if re.search(r'\b(sudo|privilage|administrator)\b',line,re.IGNORECASE):
        priv_escalate +=1
#        print(line.strip())
print(f"Failed Logins : {failed_count}")

print(" ")
print(f"Privilege Escalations : {priv_escalate}")
print(' ')
print("Possible Brute Force :")
if failed_count >=5:
    print("YES")
else:
    print("NO")
print(" ")

attackers = {}

for line in content:
    # Find an IPv4 address
    ip = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)

    if ip:
        ip = ip.group()

        if ip in attackers:
            attackers[ip] += 1
        else:
            attackers[ip] = 1

print(f"\nUnique Attackers : {len(attackers)}")

top_ip = max(attackers, key=attackers.get)

print("\nTop Attacker :")
print(top_ip)
print(f"{attackers[top_ip]} attempts")
risk = "low"
if failed_count >= 5 and priv_escalate > 0:
    risk = "Critical"
elif failed_count >= 5:
    risk = "High"
elif failed_count >= 1:
    risk = "Medium"

print(f"Risk Level : {risk}")
print("----------------------------")
