import os
import sys
import math
import cv2
import random

def processCommandLine( argv ):

   flagsOptions = {
   }
   
   if len( argv ) < 2:
      print( "Usage: <src_img_dir>" )
      exit( 0 )

   # Get the command line parameters
   returnValue = {
      "srcImgDir": argv[ 1 ]
   }
   counter = 1
   while ( len( argv ) > counter ):
      if argv[ counter ] in flagsOptions:
         try:
            # If this is a boolean flag, meaning the next argument is unrelated
            if returnValue[ flagsOptions[ argv[ counter ] ] ] == False:
               returnValue[ flagsOptions[ argv[ counter ] ] ] = True
               counter += 1
            else:
               returnValue[ flagsOptions[ argv[ counter ] ] ] = argv[ counter + 1 ]
               counter += 2
         except:
            counter += 1
            pass
      else:
         counter += 1

   return returnValue

def randomize( numImgs ):

   imgSequence = range( 0, numImgs )
   random.seed( None )
   return random.sample( imgSequence, numImgs )

def main():

   # Process the command line arguments
   args = processCommandLine( sys.argv )

   # Get the list if input images
   filenames = [ args[ "srcImgDir" ] + '/' + fileame for fileame in os.listdir( args[ "srcImgDir" ] ) ]

   # Load the images into memory
   images = [ cv2.imread( filename ) for filename in filenames ]

   # Validate
   for index, img in enumerate(images):

      # None
      if img is None:
         print( " Skipping '" + filenames[index] + "' because it failed to load" )
         continue

   # Remove files that could not be loaded
   index = 0
   while index < len(images):
      if images[index] is None:
         images.pop( index )
         filenames.pop( index )
      else:
         index += 1

   # Get a random sequence
   try:
      randomSequence = randomize( len(images) )
   except Exception as e:
      print( e )
      exit()

   # Create a single window for display
   windowName = "BINGO"
   cv2.namedWindow( windowName )

   # For every randomly-selected image index
   i = 0
   while i < len(randomSequence):

      index = randomSequence[ i ]

      # Output the filename in case something happens
      print( filenames[ index ] )

      # Show the image
      cv2.imshow( windowName, images[ index ] )
      cv2.setWindowTitle( windowName, "Bingo card " + str(i) )

      # Handle user input
      iPrev = i
      while i == iPrev:
         
         # Wait for keyboard input
         keyPressed = cv2.waitKey( 0 )

         # enter, right-arrow, down-arrow
         if keyPressed == 13 or keyPressed == 3 or keyPressed == 1:
            i += 1
         # left-arrow up-arrow
         elif keyPressed == 2 or keyPressed == 0:
            i = max(0, i-1)
         # escape
         elif keyPressed == 27:
            i = 1000000000

   # Clean up
   cv2.destroyAllWindows()

if __name__ == "__main__":
   main()