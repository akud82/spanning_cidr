import math

def to_bin(ip):
    octets = list(map(int, ip.split('.')))
    return '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*octets)

def to_addr(bin_ip):
    return '{0}.{1}.{2}.{3}'.format(int(bin_ip[0:8], 2), int(bin_ip[8:16], 2), int(bin_ip[16:24], 2), int(bin_ip[24:32], 2))

def diff(str1, str2):
    return [i for i in range(len(str1)) if str1[i] != str2[i]]

def spanning_cidr(ips):
    ip_addrs = [x for x in ips if x]

    if len(ip_addrs) == 0:
        return None

    if len(ip_addrs) == 1:
        return "{0}/{1}".format(ip_addrs[0], 32)

    sorted_ips = sorted(ip_addrs)
    first_bin = to_bin(sorted_ips[0])
    netmask = 32

    for ip in sorted_ips[1:]:
        ip_bin = to_bin(ip)
        if len(ip_bin) == 32:
          diff_pos = diff(ip_bin, first_bin)
          if len(diff_pos):
              netmask = min(netmask, diff_pos[0])

    net_addr_bin = first_bin[:netmask].ljust(32, '0')
    return "{0}/{1}".format(to_addr(net_addr_bin), netmask)
