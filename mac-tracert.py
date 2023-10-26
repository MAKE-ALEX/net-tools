from netaddr import *

import re

#输入要转换的MAC
def mac_address_input():
    in_mac_sour = input('输入要转换的MAC：')
    return in_mac_sour


# mac地址转换 EUI to 华为
def mac_address_format_conversion__eui_to_huawei(souer_mac):
    try:
        # 如果错误则退出程序
        mac = EUI(in_mac_sour)
    except:
        print('输入的MAC地址有误！')
        exit()

    mac = str(mac).replace('.', '-')  # 直接用字符串处理！

    return mac


if __name__ == '__main__':
    # 输出后不要退出，输入任意键后退出
    in_mac_sour = mac_address_input()
    out_mac = mac_address_format_conversion__eui_to_huawei(in_mac_sour)
    print(out_mac)
    input('按任意键退出...')
