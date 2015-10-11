# OSX 10.10.x Instructions

###Dagobah
We're using Dagobah for cronjob type functionality that's editable in a web interface along with tree based dependencies for more complex jobs.

Check out Dagobah on Github:  https://github.com/thieman/dagobah

You should install dagobah and it's requirements using pip:
```pip install dagobah```

Rather than running dagobahd in the Terminal every time we start up, we've made a file called dagobah-startup.plist to take care of that on startup.
Copy the file into /Library/LaunchDaemons:
```sudo cp dagobah-startup.plist /Library/LaunchDaemons/```

Change the line that contains the path to dagobahd. In this example it points to the the dagobahd installed through boxen and pip. ```<string>/opt/boxen/homebrew/bin/dagobahd</string>```

This will run dagobahd as root user on startup, so make sure that a .bashrc file is in place to pick up any needed environment variables and change the password so that your users don't have root access to your machine through the browser.
