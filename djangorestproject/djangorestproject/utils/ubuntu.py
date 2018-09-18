import socket, subprocess


def getlocaliplist():
    hostname = socket.gethostname()
    hnip = socket.gethostbyname(hostname)

    shell_cmd = "ip addr | grep inet | grep -v inet6 | grep -Po 'inet \K[\d.]+'"
    proc = subprocess.Popen([shell_cmd], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

    ip_list = set(filter(None, out.decode().split('\n')))
    localip = ".".join(["0" for _ in range(4)])
    ip_list.update([hnip, localip, "localhost"])

    return ip_list
