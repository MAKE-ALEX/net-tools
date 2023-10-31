# 写一个方法，ping给出的地址，如果成功返回true，否则返回false。
# 使用ping3这个库。
import ping3


def ping(ip):
    try:
        ping3.ping(ip)
        return True
    except:
        return False
