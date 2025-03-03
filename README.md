# CSCE465 Project: Security of TCP & Flask Server Vs Common Cyberattacks

This project was born due to our Spring 2025 Peer Learning Activity in which we have to show implementations of network defense mechanisms against common cyberattacks such as Distributed Denial of Service (DDoS). Hence as a team we decided to simulate common attacks, and design particular defense mechanism in our simple flask website.

## Project Requirements

In order for this project to work on your system you will need a few things installed and these are:

- Python (Lastest Version)
- Flask Framework 
- Scapy Library ($ pip install scapy)
- Wireshark

## How to run the project?

To run the project follow these steps:

1. Modify the basic-flask-app.conf and set an IP for the aplication
2. Open the flask app.py
3. Open Wireshark and apply the filter to your wifi to track the packets send to the website.
4. Run any demo attacks, this should slow the website and not let you accesss it.

This is the demonstration of the attack, but how then how to defend against it? Well depends on the attack. You may try:

- Setting up a firewall to stop large packets being sent, or block packets that trigger too often.
- Setup a Capcha on the website so that bots can't send package unless they successfully pass it.

## What we learn

This activity was a small introduction to the topic of Computer Network Security and in reality systems nowadays are more complex, aka defenders and attackers run their configurations with a combination of attacks or protection layers to achieve the desire objective. Exploring this gave our team a great idea of how to create safe environments and explore into attacks to engineer a solution.
