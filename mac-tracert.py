from netaddr import EUI,mac_cisco

#输入要转换的MAC
def mac_address_input():
    in_mac_sour = input('输入要转换的MAC：')
    return in_mac_sour


# mac地址转换 EUI to 华为
def mac_address_format_conversion__eui_to_huawei(souer_mac):
    mac = EUI(in_mac_sour)
    mac.dialect = mac_cisco
    mac = str(mac).replace('.', '-')  # 直接用字符串处理！

    return mac


if __name__ == '__main__':
    # 输出后不要退出，输入任意键后退出
    in_mac_sour = mac_address_input()
    out_mac = mac_address_format_conversion__eui_to_huawei(in_mac_sour)
    print(f'转换后的MAC:',out_mac)
    input('按任意键退出...')

