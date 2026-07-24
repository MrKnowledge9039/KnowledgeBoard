# KnowledgeBoard Journal

# June 28
## First Exploration of KiCAD
Made the basic 3 key Hackpad exmaple to get a feeling for KiCAD, Schematic and PCB Editing
I was very supprised to see how easy designing a PCB is and that you dont need any previous knowledge.

## Schematic Editing
  Added every all Parts including their footprints (I hope I chose the right one for the rotary encoder) I needed for my favoured design.
  Through inspiration by other Hackpads i made the Matrix (also QMK Matrix Explanation) and the backlighting daisy chain.
  After adding the rotary encoders I discovered that i had to few pins on the XIOA to add 3 rotary encoders and lighting and the rotary encoder switches.
  My idea was to add the rotary encoders also to the matrix to have less pin usage (2 columns more instead of 2 (A/B) per rotary encoder),
  because I found a youtube video where rotary encoders were explained as having offsetted binary signals to determine the rotation.
  So it's like a key getting pressed or not and i found no reason why this shouldn't work. *later I found one

## PCB Editing
  First I rotated every switch so I could place the LEDs behind each switch not infront.
  Secondly I placed the three rotary encoders beside the 3x3 key "panel".
  After that I arranged every diode to it's optimal place (rearranged it later to make space for the XIAO).
  I tried multiple times wiring the row and col sections first and then the LEDs but it got each time to messy so I tried again.
  My next approach was to wire the LEDs first but that wasn't optimal. Afterwards I discovered that vias exist so I tried again and it worked like a charm.

Research: How to work with LED, Rotary-Encoders for Schematic and PCB editing and stuff.

Time: ca. 7h

# June 29
  Although the rewiring helped and after I changed the pin assignment on the XIAO the wiring got quite good and I thought I was nearly ready, I discovered two other issues.
### Issue 1:
  I cramed the XIAO, the LED and the Switch on the exact point on the PCB which obiously does not work. so I needed to move the LED and XIAO.
  (I thought the XIAO could go on the bottom side and the switch was designed so the LED would fit on the same side as the switch, I have never done this)
### Issue 2:
  The trick with adding the rotation pins to the matrix does not work, because the code checks the matrix each row at a time,
  but the rotation pins need to be checked all the time to work.

Research: Why these things don't work and how to fix them.


# June 30 / July 1,2,3
  I startet all over again and changed my design to have two rotary encoders and placed them on the top, not on the side as before.
  And made my design the design symetrical with the XIAO at the top between the rotary-encoders.
  I finished the design made the schematic, used a better way to align the items then the auto clamp when dragging,
  paid attention to put everything on the side it should be wired everything. And thought again I could go on with making the 3D-CAD, but no.
  I ran the DRC and I got multiple issues. 36 of them were the same. Every footprint of the LEDs had the same 4 issues. The pads were to close to the Edge.cuts layer.
  So I first looked on other projekts and how they solved the problem. They had smaler pads, so i thought ok good where do I find this library.
  I didn't find it so I thought good, then I'll try to make a footprint similar to the one that worked for the other projekt.
  And it worked. But because of this and because I wanted the rotation knobs on the side and not on the top it wanted it to remake it again.

Time ca. 5h

# July 5
 Starting all over again I chose to just make the design upright and just use a angled cable if needed.
 I first changed the schematic slightly and fixed two Input/Output Power Issue, using PWR-Flags. After that I again placed, wired and fixed all the issues left. Then I made the final Form of the PCB in the edge.cuts layer. And there I was ready with my PCB and on to the next part.

Time ca. 3h

# July 11,12,18,19
 Designing the 3D case for the PCB. First importing the PCB, then making a 3mm margin around it and adding a part to hold the pcb while still having enough space for the PCB parts on the bottom. Additionally adding a simple integrated plate to clip in the switches. After the first design I made two more. One with a bigger body and a seperate integrated plate and another one with a smaller body, which is at the same time the plate the swtiches clip to. Very helpful for this was the [Hackpad design of Devin Myers](https://cad.onshape.com/documents/fadd4340fdcb2f9894b9d56e/w/4e9dbccf657b58782bca758e/e/4c2b640b6a0422cb6de851e2?renderMode=0&uiState=6a6238705d1f8fdad3a81a58). I thought I wil use so I completed the bigger and left the smaller version unfinished.

 Time ca. 7h

# July 21,22
 For the firmware I chose KMK because it's esier and more simpel then QMK and I needed to install just Python. After downloading the release of CircuitPython for the XIAO I looked at the firmware of my inspiration and then used the very good documentation on github(the website documentation is gone) to complete it with the rotary encoders, the keys and the LEDs.

 Time ca. 2h

# July 23
 After reviewing everything I discovered that the smaller case I chose to use had no holes for the heat insets. So I added that (also had also to change the Edge.Cuts Layer on the PCB). It was nice to be so quick with everything after the first attempt took so long.

 Time ca. 30min
