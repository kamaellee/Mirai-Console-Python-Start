import os
import subprocess
import hashlib
import yaml


path = r'./config/console/AutoLogin.yml'


def start():
    auto_exist = False
    file_exist = os.path.exists(r'./config')
    cmd = (
              "@echo off &"
              "title Mirai Console &"
              "java -cp %s net.mamoe.mirai.console.terminal.MiraiConsoleTerminalLoader &"
              "pause"
          ) % '"./libs/*"'

    if not file_exist:
        try:
            print('未找到文件，开始创建文件……')
            sub_process = subprocess.Popen(cmd, shell=True)
            sub_process.wait(timeout=2)
        except:
            print('已创建完毕，请重新执行文件。')
            """ 这里有一个bug，创建完结束后没法自动循环下一次进程
                得先关闭再重开
                若有更好办法请留下在issue里谢谢"""
    else:
        auto_exist = auto()
        if not auto_exist:
            bot_list = ins()
            res = load()
            for key in bot_list.values():
                acc = key['acc']
                pwd = key['pwd']
                res['md5Passwords'][acc] = pwd
            write(res)
            print('写入成功，现在开始执行程序')
            sub_process = subprocess.Popen(cmd, shell=True)
            sub_process.wait()
        else:
            print('已有自动登录号，现在开始执行程序')
            sub_process = subprocess.Popen(cmd, shell=True)
            sub_process.wait()


def load():
    with open(path, 'r') as f:
        res = yaml.load(f.read(), Loader=yaml.FullLoader)
    return res


def write(write_value):
    with open(path, 'w') as f:
        yaml.dump(write_value, f)


def auto():
    print('已有文件，开始判别自动登录')
    file_exist = os.path.exists(path)
    file_init = {'plainPasswords': {123456654321: 'example'}, 'md5Passwords': {123456654321: '1A 79 A4 D6 0D E6 71 8E 8E 5B 32 6E 33 8A E5 33'}}
    if file_exist:
        res = load()
        if file_init == res:
            return False
        else:
            return True


def ins():
    bot_num = input('是否要输入多个bot账号？（Y/N）').lower()
    bot_list = {}
    num = 0
    if bot_num == 'y':
        bot_acc = input('请输入多个bot账号，使用"/"号分隔')
        bot_pwd = input('请输入多个密码，使用"/"号分隔\n(请放心输入，密码将会使用md5加密):')
        acc_list = bot_acc.split('/')
        pwd_list = bot_pwd.split('/')
        if len(acc_list) == len(pwd_list):
            for acc, pwd in zip(acc_list, pwd_list):
                num += 1
                pwd_trans = hashlib.md5()
                pwd_trans.update(pwd.encode('utf8'))
                bot_list[str(num)] = {}
                bot_list[str(num)]['acc'] = int(acc)
                bot_list[str(num)]['pwd'] = pwd_trans.hexdigest()
    elif bot_num == 'n':
        bot_list['1'] = {}
        bot_acc = int(input('请输入账号:'))
        bot_pwd = input('请输入密码(请放心输入，密码将会使用md5加密):')
        pwd_trans = hashlib.md5()
        pwd_trans.update(bot_pwd.encode('utf8'))
        bot_list['1']['acc'] = bot_acc
        bot_list['1']['pwd'] = pwd_trans.hexdigest()
    return bot_list


def main():
    start()


if __name__ == '__main__':
    main()
