# Proxy Checker
*Minimal, Customizable and Powerful CLI-Based proxy checker in 50 lines of code*

The requirements are [``os``, ``requests`` , ``pythonping``]
Installing them is pretty straight foward
```
pip install requests
pip install pythonping
```
os is already pre-installed with python.

This checker is made within 2 stages as explained here.

**Stage 1**
Pinging the proxy via ``pythonping`` to check if the proxy is alive and checking the ms between our main ip and our proxy as shown here :
```py
proxy_status = pythonping.ping(noportip, count=1, verbose=False)
```
You can filter the proxies to the maximum ms/ping you want as shown
```py
if ping <= 200: # 200 is the maximum ping/ms by default, change it however you like it to be.
```

**Stage 2**
Checking if the proxies can be accessible via the requests module and *https://ipinfo.io* as shown here
```py
proxy_base = requests.get('https://ipinfo.io/json', proxies={'http': 'http://' + ip, 'https': 'http://' + ip}, timeout=3.5) # you can change the timeout to make the program faster, 3.5s is the default
```

After that filtered working proxies will be stored in the ``/output/alive.txt`` file, and extra details like country and ms/ping will be stored at ``/output/details.txt`` file.
Feel free to edit the file however you like and modify it if you wan't to.

i might add the blocklist filter from my old repo to this file but i need to improve it first :)
