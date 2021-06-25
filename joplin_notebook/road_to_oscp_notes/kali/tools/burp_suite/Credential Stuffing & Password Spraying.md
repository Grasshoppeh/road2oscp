Credential Stuffing & Password Spraying

# Workflow
1. Load up burpe suite
2. Go to a login forum
3. Turn intercept on
4. Enter any username and password combination
5. Press sign in
6. Go into burpe suite under intercept and send it too intruder with a right click
7. Intruder > positions > clear $

# Credential Stuffing
8. Highlight the login and email parameter. In the case of two parameters click pitchfork in the drop down
9. Go into payloads
10. Put in thems you want to use as credentials
11. start attack then pause it after a short while
12. look at some of the failed attempts and find a similarity between them
13. options > grep match > clear and add that sig (optionally clear the other parameters)

# Password Spraying
8. high the email login and set that to a list of emails
9. Change the password to explicitly something it might be, ex: fall2021, password123, etc
10. Run it


This is a very common way to get in, always check this and default credentials. Often times if there is a vulnerability on the open web and your seeing it chances are someone else has seen it. There are bad actors scanning the internet all the time.

NOTE: research the difference between sniper, battering ram, pitchfork, and cluster
IMPORTANT: If the company has active directory you should only do this one or two times and hour or more. This could like them out. You might need to know part of their password policy