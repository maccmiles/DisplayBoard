##
 #  @filename   :   runBoard.py
 #  @brief      :   7.5inch e-paper display board
 #  @author     :   Maccmiles
 #
 #  Copyright (C) Maccmiles Complete Solutions     October 28 2018
 #
 # Permission is hereby granted, free of charge, to any person obtaining a copy
 # of this software and associated documnetation files (the "Software"), to deal
 # in the Software without restriction, including without limitation the rights
 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # copies of the Software, and to permit persons to  whom the Software is
 # furished to do so, subject to the following conditions:
 #
 # The above copyright notice and this permission notice shall be included in
 # all copies or substantial portions of the Software.
 #
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.
 ##
import MySQLdb
import time
import epd7in5b
import Image
# WxH
EPD_WIDTH = 640
EPD_HEIGHT = 384
# Display Placeholders
displayCurrent = 0
displayUpdate = 0
while True:
	def DB():
		# Connect to SQL
		connection = MySQLdb.connect (host = "db_Host",
								user = "db_User",
								passwd = "db_Pass",
								db = "db")
	
		cursor = connection.cursor()# Create Cursor
		print("Querying")
		cursor.execute ("SELECT * FROM `Status` WHERE `Request` = 'Current'")# Get Current Display
		row = cursor.fetchone()
		displayCurrent = row[1]
		cursor.execute ("SELECT * FROM `Status` WHERE `Request` = 'Update'")# Get Update Display
		row = cursor.fetchone()
		global displayUpdate # Ensure my hair doesn't fall out
		displayUpdate = row[1]
		if (displayCurrent != displayUpdate):
			print("Updating Database")
			cursor.execute ("UPDATE Status SET Mode = %s WHERE Request = 'Current'" % displayUpdate)# SET current status to update status
			print("Rewriting Screen ...")
			Draw()
			print("Update OK")
		else:
			print("No Update")
	
		cursor.close()
		connection.close()
		print("Sleeping ...")
		time.sleep(60)
	
	def getPath(argument):
		switcher = {
		0: "onDuty",
		1: "inClass",
		2: "out",
		3: "working",
		4: "here",
		5: "sleep",
		6: "event",
		7: "offCampus",
		8: "meeting",
		9: "brb"
		}
		return switcher.get(argument)
	
	def Draw():
		# Init
		board = epd7in5b.EPD()
		board.init()
		# Write Display
		frame_black = board.get_frame_buffer(Image.open('Images/template.pbm'))
		frame_red = board.get_frame_buffer(Image.open('Images/%s.pbm' % getPath(displayUpdate)))
		board.display_frame(frame_black, frame_red) # Write to screen

	if __name__ == '__main__':
		DB()