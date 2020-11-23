# class chat
# author: Evan Davis

README:::

IGNORE: FILES: ServerRudimentary.py && ClientRudimentary.py

These are implementations of Pt. 1 and are essentially identical to the second
lab that was assigned. That lab layed the basis of socket programming for the
class. 

RUNNING THE SYSTEM: 
1. Download the file package.
2. Open a terminal window.
	a. You will need at least 2 and prefereably more.
3. Ensure that python3 is installed on your system.
4. CD into the classchat directory.
5. Run ~$python3 Server.py
6. Run ~$python3 Client.py
	a. Repeat steps 2, 4, & 6 for as many clients you require
7. The system is now ready to go.

NAVIGATING THE SYSTEM:

SERVER: The server requires no input and supplies no output other than a "Server Running" notification. The server can be minimized to save screen space.

CLIENTS: 
1. The client will prompt for a username, provide input.
2. Send group messages simply by typing and pressing ENTER.
3. Send private message by adding a "-" symbol before the message,
	a. No quotations marks, just the symbol.
	b. Immediately after the symbol add a user to send it to.
		i. Example: "-peter 'some message text'"
	c. If the user exists, that message will be forwarded to only that user.
	d. If the user does not exist, a "Does not exist" response will be sent 		back to the sender. 

Obligatory Sob Story: 
I did not have time to generate a makefile in bash. My apologies. I hope that is okay and that you all understand. 
