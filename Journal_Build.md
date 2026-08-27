# KnowledgeBoard Build Journal

## August 22
 I got the Hackpad kit and the PCB delivered. The PCB was great, it was funny to me to see the digital version I designed beeing so accurately beeing manufactured. It was like it came straight out of my screen. And after giving everything a look I wanted to assemble and solder everything. Before soldering though I tried wheather the XIAO would work and it did. So I started soldering with the diodes and LEDs (ik it's Light-Emitting-Diode) and then soldered the XIAO to try again. And it did't work, so my approach was to solder the switches and rotary encoders and try it fully soldered but it still didn't work. It gave me an "Power Surge on USB port" error. 

Time: ca. 3h
 
## August 23
 I tried to fix this problem using another USB port but it still didn't work. I also double checked everything that could cause a shortcircuit and I also checked the directions of all the diodes and LEDs. But nothing fixed my issue. So I asked for help in #help and #electronics and some very nice people tried to help me but unfortunately they could not fix my problem (or at least not the power surge problem). I tried to desolder everything to try it on another PCB but I only could get the switches removed the rest I will do when I get access to a heat gun.

Time: ca. 1h

## August 25, 26
### Desoldering parts
 With access to a heat gun I got the XIAO off the PCB and tried it and ot worked completely fine. Great so I could go on. I desoldered some of the diodes and LEDs, enough that with the ones I had not used, I could build the MacoBoard again. I reused the switches too. But unfortunately the rotary encoders stopped working after the attempt of getting them off. 

### Second attempt
 Too start my second try I took a second of my PCBs and soldered the XIAO onto it. It still worked great. After that I added the diodes for the key matrix. Worked! I went on with the switches. Worked! Next I tried the LEDs and solderd two of them on and checked if it still would work but it didn't. So I desoldered them again and tried if I could get the keys to actually function. And I tried some simple code to check if they work and they did. Great!

### First SK6812 MINI-E Problem
 After a closer look on my PCB design and the datasheet of the SK6812 MINI-E I found what caused the problem and how to fix it. I had used the Footprint Library of the Hackpad tutorial for the SK6812 MINI-E and the little triangle marking that showed how to solder the LED was on the opposite corner than it should be according to the datasheet. So I roated the SK6812 MINI-E 180° and this solved the first problem. I would not get the power surge error anymore. Great!

### Second SK6812 MINI-E Problem
 After the first problem was solved but the LEDs still would not light up, I searched for the origin of this problem and there the nice people in #help and #electronics helped me. The noticed that I powered the LEDs with 5V but the logic would be send at 3.3V and because the LEDs would first recognise an logic "1" or "on" above 3.5V the LEDs wouldn't light up. My solution for this was to destroy the 5V power line for the LEDs and creating a new one using a thin wire from 3.3V to the LEDs-power line. And as a result the LEDs worked. Great! I was soo happy!

 I will order new EC11 rotary encoders and try to complete my KnowledgeBoard.

Time ca. 4h 30min