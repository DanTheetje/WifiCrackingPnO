TO DO's

Keep the page limit as required in Toledo. [TO BE DONE]

Have an abstract [TO BE DONE]

More discussion in the introduction, like general description of everything, introducing the topic [TO BE DONE]

Explain more the issue with reuse of the same IV. This is the main issue with WEP. [BUSY]

In Section 1.1 you don’t talk about the sniffing. Add it. [TO BE DONE]

Remove 6.4.1 FMS method and 6.4.2 The PTW method or make it much smaller. You don’t need to know all this. [SHORTENED]

To be done: MitM and sniffing [TO BE DONE]

Put code snippets of everything to appendix (so you have more space for writing) [TO BE DONE]

Write the capabilities of the adversary shortly (like ale to capture packets, has the password (after cracking)...) [TO BE DONE]

Detailed description of the attack, step by step [TO BE DONE]

Also maybe a discussion on how to avoid the attack -- think about what was easy when you executed the attack, and propose something that makes it challenging for the adversary (countermeasures) [TO BE DONE]

Conclusion - discuss and evaluate your work [TO BE DONE]

I would remove this : “A related key attack is searching for any types of mathematical relations in a cipher e.g., the letter ”E” is statistically the most used letter in English, so the combination of bits that is used the most in the ciphertext, is therefore probably the ”E”. The WEP key is hexadecimal, this limits the key only to the letters A to F and the numbers zero to nine, this makes it easier to crack because fewer characters have to be decrypted.” There are others weaknesses to mention if you want.[DONE]

“The explicit method of decryption of WEP encrypted data is not mentioned because the goal in this paper is to decrypt WEP packages by exploiting vulnerabilities. “ What do you mean? Still explain [TO BE DONE]

Remove Figure 2: SSH connection. Not needed [PUT IN ATTACHMENTS?]

Remove listing 1. “ set up a SSH-server on the Raspberry Pi”[PUT IN ATTACHMENTS?]

“it is explained “,”it is discussed “ change it to “we explain” [TO BE DONE]

Section 3.2.2: explain simply the concept of the website and the credit system.[TO BE DONE]


Project 
1.   a. [DONE] Install Kali on one of the Raspberry Pi.
     b. [DONE] Setup one of the router to create a LAN (LAN1).
     c. Demonstrate that it works by ssh from one of your own laptop to one of the pi.
2.   a. [DONE] Use the aircrack suite to crack the password of the router (setup in WEP).
     b. Implement a simple sniffer suff module
3. Setup the second router (LAN2) and a pi which hosts a website (that has a database managed using SQL). Access the website hosted in LAN2 from LAN1.
4. Implement the man in the middle attack using ARP poisoning.
5. Modify the website "on the fly" to demonstrate the MITM attack works.
