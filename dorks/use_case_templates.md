# 🧠 Use Case Playbook

This playbook helps Tier 1 SOC analysts enrich alerts, pivot on infrastructure, and identify exposure using curated Google and Shodan dorks.

---

## 🎯 Use Case 1: Suspicious Domain in Phishing Email

**Alert**: An email contains `login-reset.com`.

**Actions**:
🕸️ Search for exposed pages or leaked content:  
- Google
  ```
  site:login-reset.com intitle:"index of"
  site:login-reset.com filetype:pdf OR filetype:xls
  ```
- Shodan
  ```
  ssl:"login-reset.com"
  hostname:"login-reset.com"
  ```

## 🎯 Use Case 2: Exposed Login Portals
🕸️ Alert: Brute-force activity on unknown login page:
- Google
  ```
  inurl:admin intitle:login
  inurl:cpanel intitle:"cPanel"
  ```
- Shodan
  ```
  http.title:"Admin Login"
  http.favicon.hash:-1571472432  # Common login panels
  ```
  
 ## 🎯 Use Case 3: Investigate IP from Alert
🕸️ Alert: IDS flags traffic to 45.155.204.147
Actions
- Shodan - Find Connected domains
  ```
  ip:45.155.204.147"
  ```
- Pivot using Google:
  ```
  "45.155.204.147" site:pastebin.com
  ```
  Why it matters: Catch reused IPs across threat clusters or leaked IOCs.

 ## 🎯 Use Case 4: Credential Leak Investigation
🕸️ Alert: SOC receives report of possible login dump.
Actions
- Search for exposed credential files  using Google:
  ```
  filetype:txt intext:@gmail.com intext:password
  intitle:"index of" passwd OR credentials
  ```
  Why it matters: Identify exposed dumps and takedown targets.  
