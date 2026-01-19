# 🌐 Shodan Dorks

| Use Case | Shodan Query | Description |
| :--- | :--- | :--- |
| Apache OFBiz | `http.html:"Apache OFBiz"` | Detects exposed Apache OFBiz portals |
| ASN Lookup | `asn:ASxxxx` | Finds all IPs belonging to a specific ASN |
| Atlassian Confluence | `http.component:"Atlassian Confluence"` | Uncovers Confluence instances |
| Atlassian Connect JSON | `html:"atlassian-connect.json"` | Finds exposed Atlassian config files |
| Atlassian Jira | `http.component:"Atlassian Jira"` | Uncovers Jira instances |
| BitBucket Components | `http.component:"BitBucket"` | Finds Bitbucket servers |
| BitBucket Login Page | `title:"Log in - Bitbucket"` | Detects Bitbucket login portals |
| BMC Remedy | `http.html:"BMC Remedy"` | Detects exposed BMC Remedy portals |
| Bomgar Remote Support | `"Server: Bomgar" "200 OK"` | Detects exposed Bomgar remote support |
| Cisco Smart Install | `"smart install client active"` | Detects legacy Cisco exposures |
| Citrix Gateway HTML | `html:"/citrix/xenapp"` | Matches Citrix XenApp paths |
| Citrix Gateway Title | `title:"citrix gateway"` | Detects Citrix login portals |
| Cobalt Strike Beacon | `product:"Cobalt Strike Beacon"` | Flags possible active beacons |
| Cobalt Strike Team Server | `product:"cobalt strike team server"` | Finds Cobalt Strike infra |
| Elasticsearch | `product:"Elasticsearch"` | Often exposed without auth |
| GlobalProtect Portal | `http.html:"Global Protect"` | Palo Alto VPN detection |
| Juniper Web Device Login | `http.title:"Log In - Juniper Web Device Manager"` | Detects Juniper device login pages |
| MOVEit SSH Banner | `"SSH-2.0-MOVEit"` | Finds MOVEit file transfer SSH ports |
| next.js | `X-Powered-By: Next.js` | Finds web apps running next.js |
| Open RDP | `port:3389` | RDP service exposure |
| Organisation (e.g. Microsoft) | `org:microsoft` | Find all Microsoft-hosted assets |
| Pulse Secure VPN | `product:"Pulse Secure"` | Finds Pulse VPN endpoints |
| Running n8n servers | `http.favicon.hash:-831756631` | Detects n8n web server running on any port |
| Same CN on SSL certs | `ssl.cert.subject.cn:"oracle.com"` | SSL pivot on shared cert common name |
| SAP NetWeaver Portal | `html:"SAP NetWeaver"` | Detects exposed SAP systems |
| Unencrypted Services | `not ssl` | Finds services that don’t use TLS |
| Windows RDP Fingerprint | `"\x03\x00\x00\x0b\x06\xd0\x00\x00\x124\x00"` | Identifies RDP protocol exposure |

