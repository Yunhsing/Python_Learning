# -*- coding: utf-8 -*-

import subprocess
import re


def ReadIP():
    with open(r'C:\Users\admin\Desktop\ip.txt','r') as f:
        return f.readlines()

def get_ping_result(ip_address):
    p = subprocess.Popen(["ping.exe", ip_address,'-n','5'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    out = p.stdout.read().decode('gbk')
    # print(out)
    reg_receive = '已接收 = \d'
    match_receive = re.search(reg_receive, out)
   
    receive_count = -1

    if match_receive:
        receive_count = int(match_receive.group()[6:])

    if receive_count > 0:    #接受到的反馈大于0，表示网络通
        reg_min_time = '最短 = \d+ms'
        reg_max_time = '最长 = \d+ms'
        reg_avg_time = '平均 = \d+ms'

        match_min_time = re.search(reg_min_time, out)
        min_time = int(match_min_time.group()[5:-2])

        match_max_time = re.search(reg_max_time, out)
        max_time = int(match_max_time.group()[5:-2])

        match_avg_time = re.search(reg_avg_time, out)
        avg_time = int(match_avg_time.group()[5:-2])

        return [receive_count, min_time, max_time, avg_time]
    else:
        print('网络不通，目标服务器不可达！')
        return [0, 9999, 9999, 9999]

def GetAllIPResult(ip_list):
    for i in range(0,len(ip_list)):
        res = get_ping_result(ip_list[i].replace('\n', ''))
        print(res)
        # print(ip_list[i].replace('\n', ''))


if __name__ == '__main__':
    # ping_result = get_ping_result('143.92.120.162')
    # print(ping_result)
    ip_list=ReadIP()
    GetAllIPResult(ip_list)