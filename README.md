# russian-troll
## What is a russian-troll?
A russian troll is a bot that will post to a victim's social media account.
## How does it work?
This program will attempt to hijack a chosen victim's social media account and then post a message from their account, as if they were the one to post it. 

## The Trolling Procedure
1. Identify a target either through nmap on the network or using a already known IP.
    
   For simplicity of this design we will be using a known IP. 
   
2. Once a target has been selected, we will then use python and scapy to perform arp poisoning on the target machine to spoof the dns. The domains we will be spoofing will consist of social media login sites such as Facebook, Twitter, Instagram, etc... so that we can redirect the dns request to our fake login page.

3. Once the target reaches our fake login page we will steal their sign in credentials and use them to access their social media account. 

## In-Depth Analysis
#### _Identifying the target_
 
 