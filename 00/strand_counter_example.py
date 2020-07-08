#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Xiaofei Zeng
# Email: xiaofei_zeng@whu.edu.cn
# Created Time: 2020-07-03 16:19

from __future__ import print_function
import sys

def read_gtf1(gtf_file):
    gtf_dict = {}
    with open(gtf_file) as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            ls = line.split()
            chrom, typ, start, end, strand = ls[0], ls[2], ls[3], ls[4], ls[6]
            if typ == 'transcript':
                gtf_dict['_'.join([chrom, start, end])] = strand
    return gtf_dict

def read_gtf2(gtf_file, gtf_dict):
    same, diff = 0, 0
    with open(gtf_file) as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            ls = line.split()
            chrom, typ, start, end, strand = ls[0], ls[2], ls[3], ls[4], ls[6]
            if '_'.join([chrom, start, end]) in gtf_dict:
                if strand == gtf_dict['_'.join([chrom, start, end])]:
                    same += 1
                else:
                    diff += 1
    print(same, diff)

def main():
    gtf_dict = read_gtf1(sys.argv[1])
    read_gtf2(sys.argv[2], gtf_dict)

if __name__ == '__main__':
    main()
