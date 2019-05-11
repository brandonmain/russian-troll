# russian-troll
## What is a russian-troll?
A russian troll is a bot that will post to a victim's social media account.
## How does it work?
This program will attempt to hijack a chosen victim's social media account and then post a message from their account, as if they were the one to post it. 

## The Trolling Procedure
1. Identify a target either through nmap on the network or using a already known IP.
    
   For simplicity of this design we will be using a known IP. 
   
2. Once a target has been selected, we will then use _arpspoof_ to spoof our MAC address to be the MAC address of the gateway router. This will allow us to capture all traffic from the target machine and then we can use _dnsspoof_ to reroute it. The domains we will be spoofing will consist of social media login sites such as Facebook, Twitter, Instagram, etc... so that we can redirect the DNS request to our fake login page.

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
From the above screenshots, we see that the Attackers IP on the network is 192.168.87.35
and the Target's IP is 192.168.87.34

#### _arpspoof_
In order to redirect the target's DNS request we need to insert our machine between the target machine and the gateway router. 

Using the `arp -a` command we can identify IP addresses on the network as well as the gateway. From the below screnshot we see that the gateway is located at IP address 192.168.87.1

<p align="center">
<img src="img/gateway.png?raw=true" width="500">
</p>

Before we initiate the arpspoof, we first must set our connection to allow packets to be forwarded using the command ` echo 1 > /proc/sys/net/ipv4/ip_forward` Without setting this packets will get stopped at our machine and not be forwarded.

<p align="center">
<img src="img/forward.png?raw=true" width="500">
</p>

Now that we are ready to begin capturing ARP packets and forwarding requests, we will execute _arpspoof_.
We use -i to specify the network interface, -t to specify the target machine to spoof replys to, and -r to specify the router we are spoofing as. 
<p align="center">
<img src="img/arpspoof.png?raw=true" width="500">
</p>

#### _dnsspoof_
Before we can spoof the DNS we must configure the /etc/hosts file to route replys to a site like "www.twitter.com" to our machines IP instead. We can do this by adding the line `<OUR_IP>  www.twitter.com` into then /etc/hosts file.
<p align="center">
<img src="img/etc_hosts.png?raw=true" width="500">
</p>

<p align="center">
<img src="img/etc_hosts_edit.png?raw=true" width="500">
</p>

 Next we need a fake site to use to phish the targets credentials from. The github repository [shellphish](https://github.com/thelinuxchoice/shellphish/tree/master/sites) contains a miriad of great popular social media site mock ups. First we'll clone this repo to our attacking machine and then place the contents of the _twitter_ file into the /var/www/html/ directory and replace index.html with the login.html file from the fake twitter site files. 
 
<p align="center">
<img src="img/fake-dir.png?raw=true" width="500">
</p>

Next we need to edit the php file index.php to pint to the index.html file.

<p align="center">
<img src="img/index_php.png?raw=true" width="500">
</p>

Now that we have our phishing login ready to go we will start an apache webserver to host the site for us when a DNS request to www.twitter.com is made.

<p align="center">
<img src="img/server.png?raw=true" width="500">
</p>

Finally we will initiate the _dnsspoof_ and begin redirecting twitter traffic to phish logins. We see in the below screenshot that when the target asks for www.twitter.com we are intercepting its traffic.  

<p align="center">
<img src="img/dnsspoof.png?raw=true" width="500">
</p>

And here we see the fake login page displayed when the users trys to sign in.

<p align="center">
<img src="img/phish.png?raw=true" width="500">
</p>

