# Minecraft Management Panel
This is a program built in java and flask (Python) made to control your server via a local GUI webpage.

It functions by communicating via sockets between the flask backend and the custom paper plugin to execute events on the server.

# Experimental
This project is still in the early stages and should not be used in production. Use at your own risk!

# How to use
Enter the /backend directory in a terminal using:
```shell
cd /backend
```

Install the required python packages using:
```shell
pip install flask flask_cors
```

Run the flask server using:
```shell
python server.py
```

Run the test server by double pressing "start.bat" in the /test server directory.

This will start a papermc server that automatically connects to the flask backend.

Now head to a browser and go to:
https://localhost:5000/

Now you should have a running panel that is connected to the server.

# Features to add
- [ ] Start BTN, requires rewrite or custom solution
- [ ] Console
- [ ] Login System
- [ ] Permission System
- [ ] Plugin Config File
- [ ] Panel Config File
- [ ] File Editing via Panel
- [ ] File Upload via Panel
- [ ] Statistics (Player Count, TPS, etc)
- [ ] Statuses
