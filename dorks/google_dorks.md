# 📄 Google Dorks (SOC Use)
Collection of Google dorks organised by use case.

---

## 🌍 Search Filters – `site`

| Filter | Description | Example |
|--------|-------------|---------|
| `site` | Identify subdomains not including www | `site:google.com -site:www.google.com` |
| `site` | Find important people on LinkedIn by company | `site:linkedin.com bbc chief` |
| `site` | Find LinkedIn users by location | `site:linkedin.com intext:location` |
| `site` | Search Twitter | `site:twitter.com bbc` |
| `site` | S3 buckets for confidential data | `site:s3.amazonaws.com confidential companyname` |
| `site` | Documents on OneDrive | `site:onedrive.live.com` |
| `site` | Government data pages | `site:gov inurl:data` |
| `site` | Admin pages on a specific site | `site:example.com inurl:admin` |
| `site` | Email exposure check | `site:pastebin.com "yourcompany.com" OR "@yourcompany.com"` |

---

## 📄 Search Filters – `intitle`

| Filter | Description | Example |
|--------|-------------|---------|
| `intitle` / `inurl` | Find open FTP servers | `intitle:"index of" inurl:ftp` |
| `intitle` | WordPress admin login | `intitle:"Index of" wp-admin` |
| `intitle` | Default Apache2 pages | `intitle:"Apache2 Ubuntu Default Page: It works"` |
| `intitle` | IIS default pages | `intitle:"IIS Windows Server" inurl:example.com` |

---

## 🔗 Search Filters – `inurl`

| Filter | Description | Example |
|--------|-------------|---------|
| `inurl` | F5 BigIP login | `inurl:/tmui/login.jsp` |
| `inurl` | Pages with "login" in the URL | `inurl:login` |
| `inurl` | Services on port 8443 | `inurl:8443 -intext:8443` |

---

## 🧾 Search Filters – `intext`

| Filter | Description | Example |
|--------|-------------|---------|
| `intext` | Open directories | `intext:"index of" "parent directory"` |
| `intext` | Password mentions | `intext:password` |

---

## 🧰 Search Filters – Other Operators

| Filter | Description | Example |
|--------|-------------|---------|
| `filetype` | File extension search | `filetype:pdf` |
| `intext` | Email domain match | `intext:"@domainname.com"` |
| `related` | Find related pages to a URL | `related:www.bbc.co.uk` |
| — | XLS files with "email" in URL | `filetype:xls inurl:"email.xls"` |
| `map` | Forces Google Maps location | `map:london` |
| `stock` | Stock-related info | `stock:goog` |
| — | Wildcard match on email | `fred.smith*.com` |
| `ip` | IP-based search | `ip:8.8.8.8` |

---

## 📢 Disclaimer

This cheatsheet is for **educational and authorised security testing only**. Always get proper permission before using these queries in a real-world context.

---

## 💬 Contributions

Spotted an issue or want to add more queries? Submit a Pull Request or open an Issue. Let’s keep this list evolving.
