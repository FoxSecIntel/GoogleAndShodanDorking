# 🧠 Use Case Playbook

### 🎯 Scenario: Suspicious domain in phishing email

1. Google dork:
site:malicious-site.com filetype:pdf
intitle:index.of "malicious-site.com"

2. Shodan dork:
hostname:"malicious-site.com"
ssl:"malicious-site.com"

3. Result: See if the domain is reused across other infra.
