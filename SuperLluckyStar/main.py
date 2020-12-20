'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-15 13:40:09
LastEditTime: 2020-12-15 16:08:10
'''
import sys
import os
import random

catalog = """
*************************************
*        超 级 幸 运 星              *
*          1.开始游戏                *  
*          2.退出游戏                *  
*          3.显示人数                *  
*************************************
"""
#


def genData():
    tmp_list = []
    tmp = ["张", "李", "王", "孙", "诸葛"]
    for i in range(1, 51):
        name = random.choice(tmp) + str(random.randint(1, 100))
        tmp_list.append("{}:{}\n".format(str(i).zfill(6), name))
    return tmp_list

def startGame(num, data):
    lucky = []
    for _ in range(int(num)):
        index = random.randint(0, len(data))
        a = data.pop(index-1)
        lucky.append(a)
    return lucky

def showData(data, show_type=1):
    if show_type == 1:
        print("***************************")
        print( "幸运用户产生了！")
        for i in data:
            number, username = i.strip().split(":")
            print("编号为：{}".format(number))
            print("用户名为：{}".format(username))
            print()
        print("恭喜这{}位用户！".format(len(data)))
        print("***************************")
    elif show_type == 2:
        print("***************************")
        print( "展示现有用户信息！")
        for i in data:
            print(i.strip())
            print()
        print("***************************")
    else:
        print("未知的格式方式！")

def main():
    global data
    data = genData()
    while True:
        print(catalog)
        chose = input("请输入你的选择：")
        if chose == 1 or chose == "1":
            num = input("请输入幸运星数量：")

            if int(num) > len(data):
                print("你输入的幸运星数量大于总人数了！")
            else:
                showData(startGame(num, data))
        elif chose == 2 or chose == "2":
            break
        elif chose == 3 or chose == "3":
            showData(data, 2)
        else:
            print("未知的输入信息，请重新输入！")

if __name__ == "__main__":
    main()
