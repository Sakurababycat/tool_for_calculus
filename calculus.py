import sympy as sp
import numpy as np
from functools import reduce
from sympy import cos, sin, tan, exp, log, pi, E, oo, I, symbols
from matplotlib import pyplot as plt

"""
use dict to make more than one equation;
dict([input().spit("=")])
"""

# list_color = ['red', 'black', 'yellow', 'blue', 'green', 'purple', 'pink']
# commands = ["solv", "diff", "integrate",
#            "tylor_series", "show_tylor", "evalf", "draw", "y"]

help = "help:\n\
        value(f, {x: 1, y: 2, ...})\n\
        solve([f, g], [x, y])\n\
        diff(f, x)\n\
        integrate(f, (x, sta, end))\n\
        tylor_series(f, x, x0=0, n=4)\n\
        draw(f, x, dom=(-10,10), dot_num=200)\n\
        limit(f, x, lim, dir=\"+\")\n\
        show_tylor(f, x, dom=(-10,10), x0=0, n=50, dot_num=200, pause_t=0.5)\n\
        set_var\n\
        set_var: x, y = symbols('x, y'); f = x ^ 2; ...\n\
        quit"

x = symbols('x')


# def set_var(str):
#     return exec(input(str).replace("^", "**"))


def limit(y, x, lim, dir="+"):
    return sp.limit(y, x, lim, dir)


def value(y, num_x):
    return y.evalf(subs=num_x)


def solve(y, x):
    return sp.solve(y, x)


def diff(y, x):
    return sp.diff(y, x)


def integrate(y, x):
    return sp.integrate(y, x)


def tylor_series(y, x, x0=0, n=4):
    return sp.series(y, x, x0=x0, n=n)


def draw(y, x, dom=(-10, 10), dot_num=200):
    return show_tylor(y, x, dom, n=0, dot_num=dot_num)


def show_tylor(y, x, dom=(-10, 10), x0=0, n=20, dot_num=200, pause_t=0.5):

    # root = tk.Tk()
    # root.geometry('1000x1000')
    # frame = tk.Frame(root)
    # frame.pack(fill="both")
    # graph = tk.Canvas(frame, width=1000, height=1000)
    # graph.pack(side="left")

    # step = (dom[1] - dom[0]) / dot_num
    x_pos = np.linspace(dom[0], dom[1], dot_num + 1, endpoint=True)[1:]
    plt.ion()
    plt.grid(True)

    lst_lev = np.array([value(y, i) for i in x_pos])
    max_y = min(int((np.max(lst_lev) + 2) * 1.5), 100)
    min_y = max(int((np.min(lst_lev) - 2) * 1.5), -100)
    plt.plot(x_pos, lst_lev, "b-", linewidth=5)

    plt.xlim(dom[0], dom[1])
    # plt.xticks(np.linspace(dom[0], dom[1], 21, endpoint=True))
    plt.ylim(min_y, max_y)
    # plt.yticks(np.linspace(min_y * 3, max_y * 3, 21, endpoint=True))

    lst_lev = np.zeros(dot_num)
    factor = 1
    for lev in range(n):
        if lev:
            y = diff(y, x)
            factor = factor * lev
        y0 = value(y, x0)
        lst_lev = lst_lev + \
            np.array([value(y0 * (x - x0) ** lev / factor,  i) for i in x_pos])
        plt.plot(x_pos, lst_lev)
        plt.pause(pause_t)
        # val = [(i, 500 - lst_lev[i] / step) for i in range(1000)]
        # graph.create_line(val, fill=list_color[lev % len(list_color)])
    plt.ioff()
    plt.show()

    return "successfull!"


# try:
#     y = set_y("(eg:y = x ^ 3 - exp(x) + cos(x) * pi)\ny = ")
#     cmd = input("value(y, 6), solv(y, x), diff(y, x), integrate(y, (x, sta, end)), \n\
# tylor_series(y, x, x0=0, n=4), draw(y, x, dom=(-10,10), dot_num=200), limit(y, x, lim, dir=\"+\"), \n\
# show_tylor(y, x, dom=(-10,10), x0=0, n=50, dot_num=200, pause_t=0.5), quit, resety, y\n\
# command:")
# except Exception:
#     cmd = "err"

# while cmd:
#     if cmd == "quit":
#         break
#     try:
#         if cmd == "resety":
#             y = set_y("y = ")
#         else:
#             print(eval(cmd))

#     except Exception as err:
#         print(err)
#     if 'y' in locals().keys():
#         cmd = input("command:")
#     else:
#         cmd = "resety"

while True:
    cmd = input("(help):").replace("^", "**")
    try:
        if cmd == "quit" or not cmd:
            break
        elif cmd == "help":
            print(help)
        elif cmd == "set_var":
            print("eg: x = symbols(\"x\")")
            print("eg: y = x ^ 3 - exp(x) + cos(x) * pi)")
            while True:
                cmd = input("q or enter to quit:")
                if cmd == "q" or not cmd:
                    break
                else:
                    exec(cmd)
        elif cmd.startswith("set_var:"):
            exec(cmd[cmd.find(":") + 1:])
        else:
            print(eval(cmd))
    except Exception as err:
        print(err)
