#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filename = "text.txt"

infile = open(filename, 'a')

infile.write("lisattyä dataa")
infile.write("\n")

infile.close()
