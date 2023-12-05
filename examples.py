#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mul(a):
    def helper(b):
        return a * b
    return helper

def fun1(a):
    x = a * 3
    def fun2(b):
        nonlocal x
        return b + x
    return fun2



if __name__ == "__main__":
    print(mul(5)(2))
    new_mul5 = mul(5)
    print(new_mul5(3))

    test_fun = fun1(4)
    print(test_fun(7))
    print(fun1(2)(4)) # x = 6 => 10
    