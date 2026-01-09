1. Create a new empty folder wherever you'd like your project to live, label it something descriptive
2. Within this folder, create a folder called 'answer' and a folder called 'journey' (case sensitive, unless you go in and edit this code)
3. Follow the Gamebanana tutorial linked in the Readme to decompile the game files
4. Go into the top level of the two below folders in file explorer and search for all .msg files. Copy those into their respective new folders from 2
  - (the search will take a while. I had almost 3,000 files between the two folders)
  - Journey filepath: L10N/en/Xrd777/
  - Answer filepath: L10N/en/Astrea/
  - At this point, the files are all .msg files, which are basically just .txt in disguise!
5. Put this Python file into the folder you created in 1
File names at this point read something like 'BMD_CmmuNPC_016_100_unwrapped.bmd.msg', and dialogue lines look like this in the raw files:

[msg MSG_028_0_0 [Mutatsu]]
[f 2 1][bup 114 0 65535 65535 0 0][vp 3 0 65535 12201 0 0]Huh, you're here again...[n][w][e]

The goal of this code is to remove the extra stuff in the file names, and clean up the dialogue lines to make them more readable.

Things this code does NOT do:

Things that are fixed with a folder-wide find/replace:
- Remove the MSG_... tag from the end of each speaker line (I used the tags to separate out conversations in big documents)
- Prob some other stuff idk