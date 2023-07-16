#!/bin/env python3

from factordb.factordb import FactorDB

N = 510143758735509025530880200653196460532653147

f = FactorDB(N)

f.connect()

print(f.get_factor_list())
