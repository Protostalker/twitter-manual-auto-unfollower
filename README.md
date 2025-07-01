Good afternoon,
Some time ago, I had my computer's tokens hijacked, and in the process, some not so kind people went ahead and added around 2000 followers on x, without my permission.

Some of you might be dealing with similar things,
Others might want a more... "Fresh" restart to twitter, but none of us want to pay stupid high costs to gain API access to X.

This simple script utilizes some common Python libraries, to scan your screen for some buttons, and presses them in sequence.
This is to automatically, manually click and have the people that are following you, to be forcibly not following you.

EG: https://x.com/YOURURLHERE/followers

The Py Libraries used:
pyautogui
time
os
math

You will probably need to pip pyautogui.

The script is rather simple, It starts by having a bit of a timer, waiting for you to bring your twitter page onto focus. 
Then utilizing pyautogui, it scans your screen looking for (x dark mode) hamburger menu icons. And in sequence, clicks on the hamburger menu, the unfollow button, and then the "remove" button that pops up, With Confidence values.

None of the script is connected to the internet, and many of the variables are easy to modify.

The script does look for a folder called "pyscripts" under C:\ . You are welcome to change that to your saved directory, or wildcard it or tilda it to be your PWD. 

I mean this code is meant to be friendly for anyone to grab, its already annoying, atleast this could do the manual process automatically for you. 

Have a wonderful time everyone :)
