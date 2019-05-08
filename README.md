# russian-troll
## What is a russian-troll?
A russian troll is a bot that will post to a victim's social media account.
## How does it work?
This program will attempt to hijack a chosen victim's social media account and then post a message from their account, as if they were the one to post it. 

## The Trolling Procedure
1. Identify a target either through nmap on the network or using a already known IP.
    
   For simplicity of this design we will be using a known IP. 
   
2. Once a target has been selected, we will then use python and scapy to perform ARP poisoning on the target machine to spoof the DNS. The domains we will be spoofing will consist of social media login sites such as Facebook, Twitter, Instagram, etc... so that we can redirect the DNS request to our fake login page.

3. Once the target reaches our fake login page we will steal their sign in credentials and use them to access their social media account. 

## In-Depth Analysis
The In-Depth Analysis section will consist of an example and analysis of this example to demonstrate the procedure.
#### _Identifying the Target_
This example will use two Kali Linux machines ran from a VirtualBox virtual machine on my host machine running MacOS. One Kali machine will be the attacker and the other Kali machine will be the target.

First, we will get the IP addresses of both of our machines on the network. 
<p align="center">
<img src="img/ip_2.png?raw=true" width="500">
<img src="img/ip_1.png?raw=true" width="500">
</p>
From the above screenshots, we see that the Attackers IP on the network is 10.0.2.15
and the Target's IP is 10.0.2.4

#### _ARP Poisoning_
In order to redirect the target's DNS request we need to insert our machine between the target machine and the gateway router. 

Using Wireshark, I started sniffing my own connection and loaded a web browser. Doing so allows me to see that the gateway router is located at IP address 192.168.87.1 as displayed in the below screenshot.

<p align="center">
<img src="img/gateway.png?raw=true" width="500">
</p>

