#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def func():
    def form_str(lst):
        res = "<ol>\n"
        for i in lst:
            res += f"<li>{i}</li>\n"
        res += "</ol>"
        return res

    return form_str


# def func(lst):
#     def form_str():
#         res = "<ol>\n"
#         for i in lst:
#             res += f"<li>{i}</li>\n"
#         res += "</ol>"
#         return res
#
#     return form_str


if __name__ == "__main__":
    lst = ["str1", "str2", "str3"]
    a = func()
    print(a(lst))
    # print(func()(lst))
