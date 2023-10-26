from netaddr import *


# mac地址转换 EUI to 华为
def mac_address_format_conversion__eui_to_huawei(souer_mac):
    mac = EUI(in_mac_sour)

    mac.dialect = mac_cisco

    mac = str(mac).replace('.', '-')  # 直接用字符串处理！

    return mac


in_mac_sour = input('输入要转换的MAC：')
out_mac = mac_address_format_conversion__eui_to_huawei(in_mac_sour)
print(out_mac)
