Investigate 80 and 443

# Let the games being

Visiting the webpage goes to a default apache webpage. Teaching says this is considered a finding. 
- Box is running apache, potentially php
- Possibly Red Hat Linux
1. Are there other web directories behind this? (How do I search this)
2. This is a red flag that should be put into the report. Says bad security hygine, 


Clicking the link give us a 404 page for /manual/index.html. 
- server give information about what version apache the client is running. Apache 1.3.20 
- Hostname was given which is information leak. We can get hostname naming covention out of it. `kioptrix.level1`

ssh version
```

```
