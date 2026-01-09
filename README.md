# Persona 3 Reload Script

---

## Overview 

I wanted to have the script for the game in one place for Angst and Fanfic reasons, and since I couldn't find it anywhere, I did it myself!

It's all a WIP, and the parts that have been organized are organized by what makes sense to my own brain :)

It goes without saying that there are spoilers for the entire game!

## Script Folder Structure

I've extensively consolidated and reorganized all the files I found in the raw game data, since there was a lot of redundant files - 8 files for one event, each with only 20 words in them - blank or "unused" files, etc. I hope it's readable nonetheless!

It's roughly separated into the main game (The Journey) and the Episode Aigis DLC (The Answer). Both of these are separated into multiple subfolders based on the context in which the text shows up:

1. Combat 
2. Friends 
3. Plot
4. School (TJ only)
5. Shops
6. UI (the roughest right now - some files in here will probably ultimately be migrated to Friends or Combat)

## File Parsing

The File Parsing folder is to save myself some headaches down the line - it includes the Python code I wrote to clean up the worst of the script files, and also the notes I took for character numbers, expression numbers, outfit numbers, etc.

Everything I learned about dialogue tags, I learned from <a href="https://gamebanana.com/tuts/17261"> this excellent modding tutorial</a>! (Although for some reason, the structure of the tags in the files I have was slightly different, so I had to improvise a bit - more info to be added in the folder)

---

### Note

The emotion tags on everyone's dialogue should be broadly correct, but a couple of people have niche or unique expressions that seemed to have just been filed under whichever number was free. 

For example, neutral expressions were all tagged as 0 - 1 is happy, 2 is angry, 3 is sad, etc. However, Aigis' glassy-eyed bustup from 11/4, Aigis' injured bustup from 12/2, and Hidetoshi's punched-out bustup from his rank 4 are all mis-labeled in the scripts. There's probably a few more that I can't remember off-hand, also.

Maybe I'll fix them at some point, but for right now I'm just leaving them as-is.

---

### To dos:
- [ ] TJ > Combat > Navis > Misc Tartarus stuff and > Navi text need to be cleaned up  
- [ ] In both Plot and Friends folders, delineating different dialogue depending on your conversation options would be awesome, but a big project...
- [ ] TJ > UI > After school and evening is a mess   
- [ ] TJ > UI > Overworld flavor text is an absolute mess. "General objects" folder hasn't been touched at all
- [ ] Evening chatter docs for party members could get cleaned up... if I get very ambitious
- [ ] Fairly certain there's some raw tag data still in the TA folder - I started with cleaning up TJ first. That'll be a couple of find/replace adventures
- [ ] No promises that Combat, Shops, and UI in TA are TA-exclusive. I pulled everything in that top-level folder from the Astrea directory in the game files, which THEORETICALLY was full of the files for TA, but it seems like there was some overlap because some of the files seem TJ-specific. (For example, I deleted several files that had Navi!Mitsuru lines)
	- However, the Plot and Friends folders for TA should be accurate.
- [ ] Both Combat > Navis folders are still kind of a mess...
- [ ] I'd like to put dates on TJ's Plot folder stuff just for my own sanity. 
- [ ] Maybe also put months on the guys' linked episodes ??
- [ ] Make consistent the "bringing teammates to BBV" setup
- [ ] Adding the rest of the File Parsing stuff

### Expansion...someday:
- [ ] Once I get the 2D assets organized and cleaned up I'd like to have them in here too!
	- [ ] Maybe even with cross-references to the script files - ie, embed visuals for all Minato's Personas in the Persona descriptions and greetings file
	- [ ] Made less necessary by <a href="https://p3rsprites.neocities.org/">this amazing bustup generator</a> made by <a href="https://x.com/MakotoYuki43161/status/2006369098985595161">MakotoYuki43161</a>, but cut-ins, renders, etc would still be cool
- [ ] The 3D models would also be amazing but I think those might be too big?
- [ ] Maybe put a link to Youtube videos for social links and plot events at the top of the file - so both options are in one place
- [ ] Fixing the one-off expressions mentioned in Note