# MyHackpad Journal

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
  So it's like a key getting pressed or not and i found no reason why this shouldn't work.

### PCB Editing
  First I rotated every switch so I could place the LEDs behind each switch not infront.
  Secondly I placed the three rotary encoders beside the 3x3 key "panel".
  After that I arranged every diode to it's optimal place (rearranged it later to make space for the XIAO). 
  I tried multiple times wiring the row and col sections first and then the LEDs but it got each time to messy so I tried again.
  My next approach was to wire the LEDs first but that wasn't optimal. Afterwards I discovered that vias exist so I tried again and it worked like a charm.
