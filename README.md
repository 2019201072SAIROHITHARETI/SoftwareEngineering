# SoftwareEngineering
major project as part of software engineering course

### Group Members:
1. SAI ROHITH ARETI(2019201072)
2. YALLAMANDA RAO MUNDRU(2019201029)
3. JAYA KRISHNA KURAVA(2019201076)
4. SHOVAN SWAIN (20161127)
5. ARUN G (201564134)
6. AASHISH SHRIVATSAVA (20161111)

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

# Additional Features Added 
Now through chat we could get image to our pc now if we need to transfer our files from our pc to any device(ie mobiles,tabs,..).

# qr-filetransfer-universal
📁 Send files from your Computer to your Phone through WiFi with a QR code

## About
This is a handy little python 3 program that allows you to send files or folders through your Local Area Network (inside your WiFi) by simply scanning a QR Code through your phone! The code is based off sdushantha's amazing work with some added stuff that I found useful plus compatibility with Windows aside from macOS and Linux.

*Note that on Windows, the QR Code won't appear inside the powershell/cmd window but instead through an image viewer.*
## Installation

Windows:

Just download and run the latest executable from the releases page above. Alternatively you can do it with the Python script:

1. Install Python 3 if you don't have it.
2. Open powershell and execute:
    pip install pyqrcode
3. Download the qr-filetransfer-universal.py file from here
4. Run it!


Linux / macOS:
```bash
# clone the repo
> git clone https://github.com/CedArctic/qr-filetransfer-universal.git

# install the requirements
> pip3 install -r requirements.txt
```


## Usage
Just double click the .py file and drag and drop inside whatever you want to send! Alternatively you can also use the program this way through the command line:

```
qr-filetransfer-universal.py [-h] -f FILE
```

**Note:** Both devices needs to be connected to the same network

**Exiting**

To exit the program, just press ```CTRL+C```. **Dont** press ```CTRL+Z```.

---

Transfer a single file
```bash
python3 qr-filetransfer-universal.py -f /path/to/file.txt
```


Transfer a full directory. **Note:** the directory gets zipped before being transferred
```bash
python3 qr-filetransfer-universal.py -f /path/to/directory/
```
