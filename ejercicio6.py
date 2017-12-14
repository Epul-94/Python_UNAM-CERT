#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
dic={i:(bin(i),hex(i)) for i in range(51) if bin(i).count('1')%2!=0}
print dic

