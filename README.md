# SoftwareEngineering
major project as part of software engineering course

DOC LINK:https://docs.google.com/document/d/1sMVWcJEF0UeHqds890efGLplTVperFOkVTOjcrh5yK4/edit#

## Packages required on system:
1. Python 2.7 or above
2. Python 3 (Note: Both 2 and 3 are necessary)
3. Tkinter GUI library for Python 2.7
4. Netifaces library

For Netifaces : sudo pip3 install netifaces

For Tkinter GUI library: sudo apt-get install python-tk

## How to use :
1. To start the server, run the command :
python3 server.py <port no>
  use port number above 1024
2. To start the client, run the command :
python client.py

The server side runs automatically and selectively keeps showing notifications as the application
goes through various stages. There is nothing to be controlled in the server side once it has started
running.

The client side on running produces a starting window which gives 2 options : 
1)To register in case you are not a part of the chat application
2)To login in case you are.

## Registration :
On clicking the register button, a new screen is displayed which takes in Server IP, Server port,
Username and password to be used for login. After clicking “Register” , if successful, one is
redirected to the Login page.

## Login :
Here, one just needs to enter the Server IP, Server port, Username and password to be used for
login. After clicking Login, if authenticated,(credentials are correct), then you are redirected to the
chat page.

## Chatting :
The list of all online users are displayed on the left side . To send a message to one or more of
them, just select your intended recipients and type in the message. Then press enter key or send
button and the message is sent! The sent and incoming messages are all shown on the chat screen.
To broadcast a message, just don’t select any users and type in your message !

## Multimedia sharing:
First select the intended recipients as usual. Enter the absolute file path,(or if in the same directory,
enter the file name), and then press the ‘Send Multimedia’ button. Please note that max file size for
sharing is 100KB .

## Quitting:
Just click the cross (‘X’) button on the title bar.

## Broadcasting the image:
To send the image or chat to multiple clients we can select the intended recipients and type the text message or mutimedia file by clicking 'Send multimedia'





### Group Members:
SAI ROHITH ARETI(2019201072)
YALLAMANDA RAO MUNDRU(2019201029)
JAYA KRISHNA KURAVA(2019201076)
SHOVAN SWAIN (20161127)
ARUN G (201564134)
AASHISH SHRIVATSAVA (20161111)
