#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def symbol(a, b):
    def stroke(s):
        return s.replace(a, b)
    return stroke
    

if __name__ == "__main__":
    print(symbol("v", "k")("vhvhvhvhvhvhv"))
