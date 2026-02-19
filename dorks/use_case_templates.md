# 🧠 Use Case Playbook

This playbook helps Tier 1 SOC analysts enrich alerts, pivot on infrastructure, and identify exposure using curated Google and Shodan dorks.

---

## ⚡ Quick Triage Workflow

1. **Identify IOC type**: domain / IP / hostname / org / leaked keyword.
2. **Run low-risk pivots first**: passive DNS, Shodan banner lookup, Google `site:` queries.
3. **Validate findings**: confirm ownership/scope before escalation.
4. **Capture evidence**: query used, timestamp, screenshot, confidence.
5. **Escalate with context**: likely impact, recommended action, ATT&CK mapping if relevant.

---

## 🎯 Use Case 1: Suspicious Domain in Phishing Email

**Alert**: An email contains `login-reset.com`.

**Actions**

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

---

## 🎯 Use Case 2: Exposed Login Portals

**Alert**: Brute-force activity on unknown login page.

**Actions**

- Google
  ```
  inurl:admin intitle:login
  inurl:cpanel intitle:"cPanel"
  ```
- Shodan
  ```
  http.title:"Admin Login"
  http.favicon.hash:-1571472432
  ```

---

## 🎯 Use Case 3: Investigate IP from Alert

**Alert**: IDS flags traffic to `45.155.204.147`.

**Actions**

- Shodan (host profile)
  ```
  ip:45.155.204.147
  ```
- Google pivot
  ```
  "45.155.204.147" site:pastebin.com
  ```

Why it matters: catches reused infrastructure and leaked IOCs.

---

## 🎯 Use Case 4: Credential Leak Investigation

**Alert**: Possible credential dump.

**Actions**

- Google
  ```
  filetype:txt intext:@gmail.com intext:password
  intitle:"index of" passwd OR credentials
  ```

Why it matters: helps identify exposed dumps and takedown targets.

---

## 📢 Safety Notes

- Use only on systems/data where you have explicit authorization.
- Respect legal boundaries and provider terms of service.
- Treat all discovered data as sensitive until verified.
