import glob
import os
import shutil
import sys
import termios

import cuitools.subp


def Input(text, normal=False, textcolor="\033[38;5;10m", dotcolor="\033[38;5;7m", usercolor="\033[38;5;12m", dot=True):
    """ \033[0m	指定をリセットし未指定状態に戻す（0は省略可）
        \033[1m	太字
        \033[2m	薄く表示
        \033[3m	イタリック
        \033[4m	アンダーライン
        \033[5m	ブリンク
        \033[6m	高速ブリンク
        \033[7m	文字色と背景色の反転
        \033[8m	表示を隠す（コピペ可能）
        \033[9m	取り消し
        """
    if not normal:
        normal = "\033[1m"
    else:
        normal = "\033[0m"
    if dot:
        inp = input(normal + textcolor + text + dotcolor + ":\033[0m" + usercolor)
    else:
        inp = input(normal + textcolor + text + usercolor)
    return inp


def Key():
    fd = sys.stdin.fileno()

    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)

    new[3] &= ~termios.ICANON
    new[3] &= ~termios.ECHO

    try:
        termios.tcsetattr(fd, termios.TCSANOW, new)
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSANOW, old)

    return ch


def Inputfile(text, textcolor="\033[38;5;10m"):
    k = ""
    pk = ""
    terminal_size = shutil.get_terminal_size()
    while k != "\n":
        print(textcolor + text + ":" + pk + "\033[H")
        k = Key()
        print("\033[2J")
        if k == "\x7f":
            pk = pk[0:len(pk) - 1]
        elif k == "\n":
            pass
        elif k == "\t":
            pass
        elif k[0] != chr(92):
            pk += k
        if len(pk) != 0:
            fl = glob.glob(pk + "*")
            tfl = fl
            fl = []
            for i in tfl:
                if os.path.isdir(i):
                    fl.append(os.path.basename(i) + "/")
                else:
                    fl.append(os.path.basename(i))
            if k == "\t":
                if len(fl) != 0:
                    fi = 1
                    j = 1
                    while fi != 0 and len(tfl[0]) > len(pk) + j:
                        for i in tfl:
                            # print(j)
                            if i.find(tfl[0][0:len(pk) + j]) == -1:
                                fi = 0
                                j = 0
                            elif len(tfl[0]) < len(pk) + j:
                                fi = 0
                                j = 0
                        j += 1

                    if len(fl) == 1:
                        pk = tfl[0]
                    elif j != 1:
                        pk = tfl[0][0:len(pk) + j]

            print("\033[" + str(int(terminal_size[1] / 2)) + ";1H" + "-" * terminal_size[0])
            if len(fl) == 0:
                fl.append("empty")
            fll = []
            for i in fl:
                fll.append(len(i))
            # print(fll)
            ps = int(terminal_size[0] / (max(fll) + 1))
            for i in range(int(terminal_size[1] / 2) - 1):
                for j in range(ps):
                    try:
                        print(fl[i * ps + j] + " " * (max(fll) + 1 - len(fl[i * ps + j])), end="")
                    except:
                        pass
                print("")
            print("\033[1H")
    return pk


def box(title="", printtext=None, reset=False):
    if printtext is None:
        printtext = []
    if reset:
        subp.reset()
    printtext.insert(0, title)
    printtext.append("")
    terminal_size = shutil.get_terminal_size()
    lentext = max(map(subp.width_kana, printtext))
    for i in range(len(printtext)):
        if i == 0:
            print("\033[" + str(int(terminal_size[1] / 2 - len(printtext) / 2 + i)) + ";" + str(
                int(terminal_size[0] / 2 - lentext / 2)) + "H┏" + subp.center_kana(printtext[i], lentext, "━") + "┓")
        elif i == len(printtext) - 1:
            print("\033[" + str(int(terminal_size[1] / 2 - len(printtext) / 2 + i)) + ";" + str(
                int(terminal_size[0] / 2 - lentext / 2)) + "H┗" + subp.center_kana(printtext[i], lentext, "━") + "┛")
        else:
            print("\033[" + str(int(terminal_size[1] / 2 - len(printtext) / 2 + i)) + ";" + str(
                int(terminal_size[0] / 2 - lentext / 2)) + "H┃" + subp.center_kana(printtext[i], lentext, " ") + "┃")
