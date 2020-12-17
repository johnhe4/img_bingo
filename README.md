# Image Bingo
Create Bingo cards using images instead of text. Then use the interactive card selector during game play. Uses python3 and local files in a directory, super-simple.

# Setup
## Dependencies
Fairly standard python3 kit, many of you won't need to install anything extra
- Python3
- OpenCV
  (`pip3 install opencv-python`)
- NumPy
  (`pip3 install numpy`)

# Getting started
Nothing needs to be built since everything is python script
```
git clone https://github.com/johnhe4/img_bingo.git
cd img_bingo
```
## Generate bingo cards
`python3 generateCard.py img .`
This will generate a single `.png` file in the current directory. Calling this a second time will generate a _unique_ card that differs from the first. Calling again will create a third, and so-on.
Cards are named using fairly unique numbers, though overwriting is certainly possible with large numbers of cards.

You can use your own images by replacing the images in the `img` directory or specifying a different directory.

# Play BINGO!
`python3 selectCardInteractive.py img`
Every game of bingo needs exactly one "Caller". This application allows a caller to randomly cycle through each image once.
You can even go back and forwards and the sequence is persistant.

This sequence is reset next time you start, so be careful not to quit in the middle of the game! In case you accidentally do, the filenames are printed to the console output just in case.

Key controls:
 - NEXT (right-arrow, enter, down-arrow)
 - PREV (left-arrow, up-arrow)
 - QUIT (escape key)
 
 # Important image disclaimer
 I've uploaded images into the repository with the sole intent of making testing easier - no ownership is claimed for the test images.

Enjoy!
-John

