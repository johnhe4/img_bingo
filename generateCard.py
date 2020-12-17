import numpy as np
import os
import sys
import math
import cv2
import random

def processCommandLine( argv ):

   flagsOptions = {
   }
   
   if len( argv ) < 3:
      print( "Usage: <src_img_dir> <out_img_dir>" )
      exit( 0 )

   # Get the command line parameters
   returnValue = {
      "srcImgDir": argv[ 1 ],
      "destImgDir" : argv[ 2 ]
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

def randomize( numImgs, numTiles ):
   
   # Check we have enough images
   if numImgs < numTiles:
      raise Exception( "Not enough images for " + str(numTiles) + " tiles")

   imgSequence = range( 0, numImgs )
   random.seed( None )
   return random.sample( imgSequence, numTiles )

def main():

   # Process the command line arguments
   args = processCommandLine( sys.argv )

   # Hard-code tiles, including middle tile which is always "free"
   tileDimension = 5

   # Hard-code image dimension
   imgDimension = 500

   # Create the middle "free" tile
   freeTileImg = np.zeros( (imgDimension, imgDimension, 3), np.uint8 )
   position = ( int(0.10 * imgDimension), int(0.60 * imgDimension) )
   cv2.putText( freeTileImg,
      "FREE",
      position,
      cv2.FONT_HERSHEY_SIMPLEX,
      int(0.01 * imgDimension),
      (255, 255, 255, 255),
      3 )

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

      # Dimensions
      xDimension,yDimension = img.shape[:2]
      if xDimension != imgDimension or yDimension != imgDimension:
         print( " Image '" + filenames[index] + "' is not " + str(imgDimension) + "x" + str(imgDimension) )
         exit()

   # Remove files that could not be loaded
   index = 0
   while index < len(images):
      if images[index] is None:
         images.pop( index )
      else:
         index += 1

   # Get a random sequence
   try:
      randomSequence = randomize( len(images), (tileDimension ** 2) - 1 )
   except Exception as e:
      print( e )
      exit()

   # Insert the free tile
   freeTileIndex = int(tileDimension ** 2 / 2)
   images.append( freeTileImg )
   randomSequence.insert( freeTileIndex, len(images) - 1 )

   # Create an output image
   outputImg = np.zeros( (imgDimension * tileDimension, imgDimension * tileDimension, 3), np.uint8 )

   # For every output tile
   for i in range( tileDimension ** 2 ):
      x = int( (i % tileDimension) * imgDimension )
      y = int( int(i / tileDimension) * imgDimension )
      outputImg[ x:x+imgDimension, y:y+imgDimension ] = images[ randomSequence[ i ] ]

   # Generate a unique filename based on the random sequence
   filename="bingoCard_"
   for n in randomSequence:
      filename += str(n)
   cv2.imwrite( args[ "destImgDir" ] + "/" + filename + ".png", outputImg )

if __name__ == "__main__":
   main()