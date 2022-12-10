# Google dork cheatsheet

Google dorking, also known as Google hacking, is the practice of using advanced search operators and specialized queries to search for information that is not easily accessible through regular search engines. 

Some examples of Google dorking queries i use to find interesting stuff are shown below:

## Search filters
| Filter          | Description                                        | Example                              |
| :-------------- |:---------------------------------------------------| :------------------------------------|
| site    | Identify subdomains that do not include www  | site:google.com -site:www.google.com |||
| filetype| Search for any kind of file extensions | filetype: pdf |||
| intitle/inurl | Search for open FTP servers | intitle:"index of" inurl:ftp |||
|intitle | Search for WP Admin Login pages | intitle:"Index of" wp-admin |||
|inurl | This query searches for pages that contain the word "login" in the URL | inurl:login |||
|intext | This query searches for pages that contain the word password in the text of the page | intext:password |||
|related | This query searches for pages that are related to the specified URL. | related:www.bbc.co.uk|||
| | This query searches for files types .xls and the word emails in the url | filetype:xls inurl:"email.xls"|||
| intitle | Find those default Apache2 webapages | intitle:"Apache2 Ubuntu Default Page: It works"|||
| intitle | Find those default Windows webpages per url | intitle:"IIS Windows Server" inurl:example.com|||
| site | Find those important people on linkedin by company |site:linkedin.com bbc chief|
|map | Forces Google to provide a map of the location | map:london|||
||Finding email addresses linked to an email address | fred.smith*.com|||
|site|Find information through social media | site:twitter.com bbc|||
|site|Search s3 buckets for confidential files | site:s3.amazonaws.com confidential companyname|||
