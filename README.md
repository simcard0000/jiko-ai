![active development](https://img.shields.io/badge/active%20dev-on%20hold-yellow.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/simcard0000/jiko-ai.svg)
# jiko-ai
🐈 A creative final project for SE101 (cohort 2024) - the first-year concepts course for Software Engineering @ the University of Waterloo. jiko-ai is a virtual pet, styled after Tamagotchi™, in which the user is encouraged to not only look after their creatures, but after themselves too. Through activities like medition and affirmations, both the pet and the user can grow together!
### Credits
The audio processing of this project relies heavily on [IBM's Speech-To-Text Service](https://www.ibm.com/ca-en/marketplace/speech-to-text), and a majority of the game code was written using the pygame library (see Dependencies/Imports). For helping format the request to the API and keeping track of what requests we wanted to make, the [Postman](https://www.getpostman.com/) tool was used.

Other sites and resources that were integral to the building of the project include:

#### Dependencies/Imports
* [pygame](https://pypi.org/project/pygame/) - for building multimedia applications like games
* [pillow](https://pypi.org/project/Pillow/) - an imaging library
* [requests](https://pypi.org/project/requests/) - for being able to make API calls to IBM Watson
* json - part of the standard Python library for dealing with this format
* [pyaudio](https://pypi.org/project/PyAudio/) - for handling audio I/O
* wave - part of the standard Python library to interface with the WAV format

#### Useful Links
Some links we accessed for the project include: 
* for helping set up the wifi on the Raspberry Pi from Adafruit: [Setting up Wifi by Hand](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-occidentalis); a .conf file that we used that we made from this is made available at [@simcard0000's gists](https://gist.github.com/simcard0000)
* this [Stack Overflow question: How to make buttons in python pygame](https://stackoverflow.com/questions/10168447/how-to-make-buttons-in-python-pygame/10169083) was accessed to help us make our code for creating buttons
* the code for recording and storing the .wav file produced from the audio input is from this [Real Python Tutorial for Playing and Recording Sound in Python](https://realpython.com/playing-and-recording-sound-python/#pyaudio_1)
* the [Text to Speech - IBM Cloud API Docs](https://cloud.ibm.com/apidocs/text-to-speech/text-to-speech) were accessed to learn more about the functions of the API
* python file i/o knowledge was pieced together from tutorials such as this: [File Handling in Python](https://www.geeksforgeeks.org/file-handling-python/)
* for learning how to open a program automatically on startup: [Stack Overflow: Open chromium full screen on startup](https://raspberrypi.stackexchange.com/questions/69204/open-chromium-full-screen-on-start-up)
* the gifImage class used to split a gif into multiple images for reanimation is from this Stack Overflow question as well: [How to Extract Frame From GIF, and Reconstruct the Details of each Frame?](https://stackoverflow.com/questions/47483375/how-to-extract-frame-from-gif-and-reconstruct-the-details-of-each-frame/48670390#48670390)
* the script used to shutdown the Pi is based off of this: [shutdown.py](https://github.com/halofx/rpi-shutdown/blob/master/shutdown.py)
* for finding what the current OS is on Python: [Stack Overflow: How can I find the current OS in Python?](https://stackoverflow.com/questions/110362/how-can-i-find-the-current-os-in-python)
* for learning more about what pins to use on the Raspberry Pi for GPIO: the [GPIO Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/usage/gpio/) and a [Raspberry Pi GPIO Pinout](https://pinout.xyz/) schematic
* debugging the API call with a specific error code involved looking at this [post](
https://developer.ibm.com/answers/questions/203041/speech-to-text-with-python-error-500/)

#### Assets
The theme music for the game is "An opener" by Bitbasic; accessed through [Free Music Archive](https://freemusicarchive.org/music/Bitbasic/Pixel_Mixel). The art used in the game are as follows; note that all images used do not imply endorsement by the artists and we used the images as placeholders; if you don't want your art here let us know!

Other assets used in the game are as follows:
* For the box in which the Raspberry Pi is housed in, the clip art of the monster on the back was accessed from this [site](https://publicdomainvectors.org/en/free-clipart/Cute-toothless-monster/81416.html)
* On the start screen, the pink cityscape is from this [site](https://steamcommunity.com/sharedfiles/filedetails/?id=1655529628)
* The new game and load game button graphics are from [here](http://pixelartmaker.com/art/1a3c1597f19b5ff)
* The forest and water background for the Q&A section of the game is from [here](https://imgur.com/gallery/g6XDZ)
* The sprites for the different creatures are from this [site](https://www.megupets.com/)
* The rainy city scene background on the main screen is from [here](https://www.pinterest.ca/pin/70650287887104685/)
* The cherry blossom city scene background on the food screen is from [here](http://www.webdesignertrends.com/2017/03/waneella-pixel-art/)
* The lake city scene background on the water screen is from this [site](https://www.pinterest.ca/pin/345510602639604879/)
* The city-at-night scene background on the sleep screen is from this [site](https://weheartit.com/entry/312959754)
* The pink/brown forest scene background on the play screen is from [here](https://weheartit.com/entry/324981803)
* The clip art used for the cleaning your pet activity are from this [site](https://clipground.com/bath-rooms-clipart.html)

Font used is [VT323](https://fonts.google.com/specimen/VT323) from Google Fonts.

~

Authors: Simran Thind (@simcard0000), Cole MacPhail (@colemacphail), Zhengmao Ouyang (@ZhengmaoOuyang), Wenyi Hu (@wenyihu3)
