__author__ = 'pointschan'

import getopt
from StringIO import StringIO
import sys
import os
# from __future__ import print_function

list_of_files = []
list_of_result = []

def main(argv):

    tmp_directory = ''
    USAGE = 'usage: traverse.py -d <directory>'
    try:
        opts, args = getopt.getopt(argv,"hd:",["directory="])
    except getopt.GetoptError:
        print USAGE
        return USAGE
        # sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print USAGE
            return USAGE
            # sys.exit(0)
        elif opt in ('-d', '--directory'):
            tmp_directory = arg

    if not tmp_directory:
        print USAGE
        return USAGE
        # sys.exit(0)
    elif tmp_directory == '.':
        tmp_directory = os.getcwd()

    old_stdout = sys.stdout
    test_result = StringIO()
    sys.stdout = test_result

    print 'Directory is', tmp_directory

    #if directory argument
    list_of_files = get_list_of_files(tmp_directory)
    if list_of_files:
        scan_files(list_of_files)
    else:
        print "There are no files to scan"

    sys.stdout = old_stdout
    result_string = test_result.getvalue()
    if result_string:
        print result_string

    return result_string


def get_list_of_files(directory_):
    tmp_list_of_files = []
    extension = ['.txt', '.doc']
    for root, dirs, files in os.walk(directory_): #("/home/vagrant/workspaces/"):
        for file in files:
            for member in extension:
                if file.endswith(member):
                    tmp_list_of_files.append(os.path.join(root, file))
                    # print(os.path.join(root, file))
    return tmp_list_of_files

def scan_files(list_of_files_):
    total = []

    for file in list_of_files_:
        a = ''
        b = []
        c = []

        try:
            f = open(file, "r")
        except IOError:
            print "Cannot open %s permission denied" % file
        else:
            for line in f:
                if a == '':
                    a = ' '.join(line.split())
                else:
                    a = a.strip()+' '+' '.join(line.split())
            b = a.split(' ')
            f.close()

        for i in range(len(b)):
            if b[i].lower() == 'can':
                if i >= 2 and i <= (len(b)-3): #skip if the first two words or last two words are 'can', example 'can can'
                    d = str(b[i-2]).strip()+' '+\
                        str(b[i-1]).strip()+' '+\
                        str(b[i+1]).strip()+' '+\
                        str(b[i+2]).strip()
                    c.append(d)
                    total.append(d)

        # output occurrences for individual file
        if c:
            tmp_li = list(set(c))
            print file
            for i in range(len(tmp_li)):
                print tmp_li[i]+' '+str(c.count(tmp_li[i]))

    #output total occurrences from all files
    if total:
        tmp_li = list(set(total))
        print "******************************************"
        print "    Total occurrences from all files"
        print "******************************************"
        for i in range(len(tmp_li)):
            print tmp_li[i]+' '+str(total.count(tmp_li[i]))

if __name__ == "__main__":
   main(sys.argv[1:])



