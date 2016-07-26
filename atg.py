# We are legion.

print('Attack Technique Guide (ATG) v1.0')
print('- Coded by aseed9 irc.anonops.com:6697 | github.com/aseed9')
main = True
sub = False
sub2 = False
sub3 = False 
print("A good resource combining all of this step by step : http://pastebin.com/raw/cRYvK4jb")

while main:

    print ("""
  - Menu Selection -
  1. Information Gathering 
  2. Network Intrusion
  3. Post Exploitation
  4. Exit
           """)

    main = input('Select Option : ')

    if main == "1":
        sub = True
        while sub == True:
                try :
                    print ("""
                    - Information Gathering -
                    1. Google Hacking
                    2. Subdomain Enumeration
                    3. WhoIS and Reverse Lookups
                    4. Port Scanning and Fingerprinting
                    5. Social Information
                    6. Go back
                    """)
                    sub = input('Select Option : ')

                    if sub == "1":
                        print("Google Hacking can unveil a massive amount of information.")
                        print("Bible for Google Hacking - https://www.blackhat.com/presentations/bh-europe-05/BH_EU_05-Long.pdf")
                        sub = True

                    if sub == "2":
                        print("Subdomain Enumeration, uncover the network's subdomains. Mapping the network is essential.")
                        print("Tools for this - Fierce | theharvester | recon-ng")     
                        sub = True

                    if sub == "3":
                        print("WhoIS and Reverse Lookups can be used to find other/further domains or IP ranges. This can be done using google.")
                        print("Dork example : via della moscova 13 site:domaintools.com")
                        sub = True

                    if sub == "4":
                        print("Port scanning and Fingerprinting to find running services and open ports.")
                        print("Use nmap for normal scans. For large IP ranges use masscan or zmap.")
                        sub = True

                    if sub == "5":
                        print("Gathering publicly available information is mandatory when (spear)-phishing.") 
                        print(" Use google, theharvester, Social network profiles, data.com, and file metadata using FOCA to gather as much info as possible.")
                        print("A key to a good lie lies in the details.")
                        sub = True

                    if sub == "6":
                        main = True

                except : 
                        print("Select a valid option!")
                        sub = True

    if main == "2":
        sub2 = True
        while sub2 == True:
                try:
                    print ("""
                    - Network Intrusion -
                    1. Social Engineering
                    2. Technical Exploitation
                    3. Go back
                    """)
                    sub2 = input("Select an Option : ")

                    if sub2 == "1":
                        print("The key to social engineering success is how believable your crafted scenario appears.")
                        print("The more believable it is, the higher chance of getting your target to do your bidding.")
                        print("http://www.social-engineer.org/framework/general-discussion/")
                        print("http://blog.cobaltstrike.com/2015/09/30/advanced-threat-tactics-course-and-notes/")
                        print("NOTE: WHEN SE-ing. Use your imagination.")
                        sub2 = True

                    if sub2 == "2":
                        print("This depends on what services and systems are running on the target network. Requires good info-gathering.")
                        print("Guide with ton of info - http://pastebin.com/raw/cRYvK4jb")
                        sub2 = True

                    if sub2 == "3":
                        main = True  
                
                except:
                    print("Select a valid option!")
                    sub2 = True              

    if main == "3":
        sub3 = True
        while sub3 == True:
                try:
                    print("Press 9 to move to parent menu.")
                    print("During this stage, you want to establish a strong foothold inside the network and analyze everything internal.")
                    print("For example, run sniffers to see traffic, open multiple remote entrances, plant a rootkit :).")
                    print("Here will be a list of tools.")
                    print(""" https://www.busybox.net/
                         https://nmap.org/
                         https://github.com/SpiderLabs/Responder
                         https://github.com/bendmorris/static-python
                         http://www.tcpdump.org/
                         http://www.monkey.org/~dugsong/dsniff/
                         http://www.dest-unreach.org/socat/
                         https://www.gnu.org/software/screen/
                         http://average-coder.blogspot.com/2011/09/simple-socks5-server-in-c.html
                         http://tgcd.sourceforge.net/
                         """)
                    sub3 = input("Press 9 to move to parent menu : ")   
                    
                    if sub3 == "9":
                        main = True

                except:
                    print("Select a valid option!")
                    sub3 = True

    if main == "4":
        quit()

    else:
        print("Select a valid option!")
        main = True 

#Expect US           









                        







