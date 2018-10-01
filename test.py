a = """[  3]  0.0- 0.5 sec   428 MBytes  7.18 Gbits/sec
[  3]  0.5- 1.0 sec   107 MBytes  1.79 Gbits/sec
[  3]  1.0- 1.5 sec   213 MBytes  3.57 Gbits/sec
[  3]  1.5- 2.0 sec   213 MBytes  3.58 Gbits/sec
[  3]  2.0- 2.5 sec   106 MBytes  1.79 Gbits/sec
[  3]  2.5- 3.0 sec   213 MBytes  3.57 Gbits/sec
[  3]  3.0- 3.5 sec   213 MBytes  3.58 Gbits/sec
[  3]  3.5- 4.0 sec   106 MBytes  1.79 Gbits/sec
[  3]  4.0- 4.5 sec   213 MBytes  3.58 Gbits/sec
[  3]  4.5- 5.0 sec   106 MBytes  1.79 Gbits/sec
[  3]  5.0- 5.5 sec   213 MBytes  3.57 Gbits/sec
[  3]  5.5- 6.0 sec   213 MBytes  3.58 Gbits/sec
[  3]  6.0- 6.5 sec   106 MBytes  1.79 Gbits/sec
[  3]  6.5- 7.0 sec   213 MBytes  3.57 Gbits/sec
[  3]  7.0- 7.5 sec   107 MBytes  1.79 Gbits/sec
[  3]  7.5- 8.0 sec   213 MBytes  3.57 Gbits/sec
[  3]  8.0- 8.5 sec   213 MBytes  3.58 Gbits/sec
[  3]  8.5- 9.0 sec   106 MBytes  1.79 Gbits/sec
[  3]  9.0- 9.5 sec   213 MBytes  3.57 Gbits/sec
[  3]  9.5-10.0 sec   107 MBytes  1.79 Gbits/sec
[  3]  0.0- 0.5 sec   428 MBytes  7.18 Gbits/sec
[  3]  0.5- 1.0 sec   107 MBytes  1.79 Gbits/sec
[  3]  1.0- 1.5 sec   213 MBytes  3.57 Gbits/sec
[  3]  1.5- 2.0 sec   213 MBytes  3.58 Gbits/sec
[  3]  2.0- 2.5 sec   106 MBytes  1.79 Gbits/sec
[  3]  2.5- 3.0 sec   213 MBytes  3.57 Gbits/sec
[  3]  3.0- 3.5 sec   213 MBytes  3.58 Gbits/sec
[  3]  3.5- 4.0 sec   106 MBytes  1.79 Gbits/sec
[  3]  4.0- 4.5 sec   213 MBytes  3.58 Gbits/sec
[  3]  4.5- 5.0 sec   106 MBytes  1.79 Gbits/sec
[  3]  5.0- 5.5 sec   213 MBytes  3.57 Gbits/sec
[  3]  5.5- 6.0 sec   213 MBytes  3.58 Gbits/sec
[  3]  6.0- 6.5 sec   106 MBytes  1.79 Gbits/sec
[  3]  6.5- 7.0 sec   213 MBytes  3.57 Gbits/sec
[  3]  7.0- 7.5 sec   107 MBytes  1.79 Gbits/sec
[  3]  7.5- 8.0 sec   213 MBytes  3.57 Gbits/sec
[  3]  8.0- 8.5 sec   213 MBytes  3.58 Gbits/sec
[  3]  8.5- 9.0 sec   106 MBytes  1.79 Gbits/sec
[  3]  9.0- 9.5 sec   213 MBytes  3.57 Gbits/sec
[  3]  9.5-10.0 sec   107 MBytes  1.79 Gbits/sec
[  3] 10.0-10.5 sec   213 MBytes  3.57 Gbits/sec
[  3] 10.5-11.0 sec   213 MBytes  3.57 Gbits/sec
[  3] 11.0-11.5 sec   107 MBytes  1.79 Gbits/sec
[  3] 11.5-12.0 sec   213 MBytes  3.57 Gbits/sec
[  3] 12.0-12.5 sec   110 MBytes  1.85 Gbits/sec
[  3] 12.5-13.0 sec   107 MBytes  1.80 Gbits/sec"""
data = 0
for line in a.split("\n"):
    # data += line.split(" ")
    # print data
    # print line.split(" ")[9]

    if line.split(" ")[9] == "MBytes":
        tmp = float(line.split(" ")[8])
        data += tmp
    elif line.split(" ")[8] == "MBytes":
        tmp = float(line.split(" ")[7])
        data += tmp
    else:
        tmp = float(line.split(" ")[9])
        data += tmp

    print tmp

print data/13 * 8 / 1024
print 107.0 * 8 / 1024 * 2