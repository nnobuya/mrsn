#! /usr/bin/env python3

import sys

args = sys.argv


if len(args) != 2:
    print('error!')
    print('   usage: ./sum_iso.py abundance-file')

    exit()
else:
    op_file = args[1]
    f_name  = op_file.split('.dat')[0]
    print(f_name)


y_z = [ 0.0 for i1 in range(101) ]
y_n = [ 0.0 for i1 in range(201) ]
y_a = [ 0.0 for i1 in range(251) ]

for line in open(op_file):

    if line[0:1] == '#':
        continue


    dat = line.split()

    z_in = int(float(dat[1]))
    n_in = int(float(dat[2]))
    a_in = int(float(dat[3]))

    x_in = float(dat[4])
    y_in = float(dat[5])

    y_z[z_in] += y_in
    y_n[n_in] += y_in
    y_a[a_in] += y_in


Out_z = open(f_name + '_z.dat', 'w')
Out_n = open(f_name + '_n.dat', 'w')
Out_a = open(f_name + '_a.dat', 'w')

for j in range(len(y_z)):
    Out_z.write('{0:>5}{1:15.7e}\n'.format(j, y_z[j]))

for j in range(len(y_n)):
    Out_n.write('{0:>5}{1:15.7e}\n'.format(j, y_n[j]))

for j in range(len(y_a)):
    Out_a.write('{0:>5}{1:15.7e}\n'.format(j, y_a[j]))


exit()
