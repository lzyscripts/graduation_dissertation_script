# -*- coding: utf-8 -*
import sys
import os
import re

listofall = []
tmplist = []
line_distance = 100

#指定一个阈值
threshold = 10
#指定输入文件的文件夹
input_path = '/path/to/histogram.list(s)'
#指定输出文件的文件夹
output_path ='/path/to/output/files'

print type(output_path)

#遍历文件夹
for root, dirs, files in os.walk(input_path):
    # 遍历文件
    for file in files:
        with open(os.path.join(root, file), 'r') as f:
            for line in f:
                strLine = line.strip()
                listofall.append(strLine)
        filename = file.split(".list")[0]
        fileObject = open(output_path+'/'+filename+'_100bp_bigger_'+str(threshold)+'.list', 'w')
        idx = -1
        for each in listofall:
            idx += 1
            if (re.match("100,", each)):
                if (int(each.split(',')[1]) >= threshold):
                    fileObject.write(listofall[idx - line_distance]+ "\n")
        listofall = []



union_of_all = []
	for root, dirs, files in os.walk(output_path):
	    for file in files:
	        union_of_all = list(set(union_of_all).union(set(open(os.path.join(root, file), 'r').readlines())))

	# 按照STR长度由短到长排序
    union_of_all.sort(key=lambda i: len(i), reverse=False)  
	print(union_of_all)
	fileObject = open('case_bp100_bigger'+str(threshold)+'_union.list', 'w')
	for i in union_of_all:
	    fileObject.write(i)
	fileObject.close()
