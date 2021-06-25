Day and a life of a hacker

# Day and a life of a hacker

## Roll out of bed

```
Work life is that of a regular IT guy. Getup do things go to work 
```

## External/Internal Penetration testing

Types of jobs are split into two categories. External and Internal.
External is attacking at network from outside over the web, you don't have access to the internals and you must break in.

- You don't have access to the internal network
- You can work from anywhere that allows work
- You must try and break in

Internal is assuming you've breach the permimiter and you can run code in the environment. This assumes you have internal network access, a dropbox setup, some sort of code execution, logged into their vpn, does not matter somehow on their network.

- This might be active directory pen testing
- Checking how you can pivot around the network
- Checking internal servers for security
- Seeing what you can find

## Web Applications

This is someone asking you to break a website this could be

- Logging in, in a way you should not
- Getting somewhere you shouldn't be able to get to
- Evaluating the Security posture of a website
- etc

## Wireless

This is onsite, go there and try and get into a wireless network.

- Check for guest networks and see if there's any segmentation or not (there should be)
    - More specifically you should not be able to access employee resources from the guest network. Sometimes you can.
- Looking for rogue devices
- Seeing what else might interest you

## Physical / Social / Phishing

A Physical assessment is you go onsite and try to break into the building.

- This could be checking doors, magnetic locks, hinges are on the right side.
- Lock picking
- Cloning badges
- Breaking an entering
- You might have a destination in mind such as a network closet.

Social engineering is trying to trick people

- A lot of times its just cloning badges you know in just making your way into the building through whatever methodology you can.

Phishing is a type of social engineering, these are done in campaigns

- This could be sending emails to get people to click a link
- Calling people up on phone and seeing what information they can get
- In general you want
    - usernames, credentials, personal info, sensitive information, anything you can use to do further attacks

## SOC aka Purple Teaming

Blue team and Red team sit down together and see what they can find.

1.  Blue team will setup defenses and ask for a certain type of attack
2.  Red team will attack
3.  Blue team will see if they can detect and stop the attack
4.  Red team will try again

You might do any of the assessment of any of the items listed above

- It could be random things like plugging into their network
- Running specific attacks
- Checking to see if alerts work and trying to bypass them

These are some of the best assessments out there, both teams learn a lot!

## Writing reports

ahh the IT passtime,,, You will need to write reports to tell them what you found. See my report writing section

## Debriefs

You will need to take your report and talk to people about it.

## Technical Skills you need

(These will pass an interview)
**Base Knowledge**:

- Linux (Preferably Kali/Parrot)
- Networking (OSI Model, Protocols (TCP/UDP/HTTP), etc)
- Scripting (Python, Bash, etc)
- Solid hacking methodology (And the ability to keep learning)
- Tool familiarity (Metasploit, Burp suite, Nessus, etc)

**Preferred Knowledge (This will get you ahead of the pack)**:

- Active Directory
- Wireless Attacks
- OWASP top 10
- Coding skills, making new tools. Not to be confused with scripting (Python, Bash, etc)

## Soft Skills you need

These are not talked about and need to be practiced

- Strong desire to learn
    - You need keep learning about new skills and tricks.
    - Need to go home and study, its a cat and mouse game
    - You need to stay ahead
- Non-complacency
    - Always want to learn more and move up.
    - You need to be able to move up and learn
- Social/people skills
    - Need to be able to talk with people
- Perseverance
    - Even if you fail you cannot give up, the answer is not always there.
    - You might have a machine that look like it has no exploits (it does)
- Blog/Twitter/Github/etc
    - You need something you contribute back to the community
    - You will get asked where you get your news from
    - Blogs and twitter help a lot
    - It just needs to help you learn