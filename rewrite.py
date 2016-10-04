#!/usr/bin/env python2
import sys

def rewrite(in_string, parameters):
    for param in parameters:
        if '\\'+param+'\\' not in in_string:
            print "WARNING : parameter "+param+" not used."
        in_string = in_string.replace('\\'+param+'\\', parameters[param])
    if '\\' in in_string:
        print 'WARNING : string may not be fully specified'
    return in_string

def parse(paramstring):
    pdict = {}
    for line in paramstring.split('\n'):
        try:
            k, v = [v.strip() for v in line.split(':')]
            pdict[k] = v
        except:
            pass
    return pdict

def rewrite_file(in_fn, param_fn, out_fn):
    f = open(in_fn, 'r')
    p = open(param_fn, 'r')
    o = open(out_fn, 'w')
    output = rewrite(f.read(), parse(p.read()))
    o.write(output)
    f.close()
    p.close()
    o.close()

rewrite_file(*sys.argv[1:])

