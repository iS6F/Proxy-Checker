import os, requests, pythonping

path = os.path.normpath(os.getcwd())
ipf = open(f'{path}\\proxies.txt', 'r')
ips = ipf.read().splitlines()
base = requests.get('https://ipinfo.io/json')
data = base.json()
main_ip = data['ip']
cw = '\33[37m'
cp = '\33[35m'
cg = '\33[32m'
cr = '\33[31m'
cy = '\33[33m'
ipcount = 0
done = 0
alive = 0
for ip in ips:
    ipcount += 1
    
for ip in ips:
    try:
        done += 1
        os.system(f'title [{done} of {ipcount}] ~ Alive [{alive}]')
        noportip = ip
        proxylist = noportip.split(':')
        noportip = proxylist[0]
        proxy_status = pythonping.ping(noportip, count=1, verbose=False)
        ping = int(proxy_status.rtt_avg_ms)
        if ping <= 200:
            try:
                proxy_base = requests.get('https://ipinfo.io/json', proxies={'http': 'http://' + ip, 'https': 'http://' + ip}, timeout=3.5)
                proxy_data = proxy_base.json()
                proxy_ip = proxy_data['ip']
                proxy_country = proxy_data['country']
            except:
                proxy_ip = main_ip 
            if proxy_ip != main_ip:
                alive += 1
                print(f'{cw}[{cp}{ip}{cw}] {cw}[{cp}{proxy_country}{cw}] {cw}[{cg}Alive{cw}] {cw}[{cy}{ping}{cw}]')
                with open(f'{path}\\output\\alive.txt', 'a') as f:
                    f.write(f'{ip}\n')
                with open(f'{path}\\output\\details.txt', 'a') as f:
                    f.write(f'{ip} | [{proxy_country}] [{ping}]\n')
            else:
                print(f'{cw}[{cp}{ip}{cw}] {cw}[{cr}Dead{cw}] {cw}[{cy}{ping}{cw}]')
        else:
            print(f'{cw}[{cp}{ip}{cw}] {cw}[{cr}Dead{cw}] {cw}[{cy}{ping}{cw}]')
    except Exception:
        pass
input(f'{cw}[{cp}Done]{cw}')
