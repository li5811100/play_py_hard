import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--int",type=int, default=10, help = "it is a test of int")
parser.add_argument("--str",type=str, default='10', help = "it is a test of str")
args = parser.parse_args()
print(args)

# # -*- coding: utf-8-*-

# import os, os.path, sys
# import win32process, win32event

# exe_path = sys.argv[1]
# exe_file = sys.argv[2]

# #os.chdir(exe_path)

# try :
        # handle = win32process.CreateProcess(os.path.join(exe_path, exe_file),
                # '', None, None, 0,
                # win32process.CREATE_NO_WINDOW,
                # None ,
                # exe_path,
                # win32process.STARTUPINFO())
        # running = True       
# except Exception, e:
        # print "Create Error!"
        # handle = None
        # running = False

# while running :
        # rc = win32event.WaitForSingleObject(handle[0], 1000)
        # if rc == win32event.WAIT_OBJECT_0:
                # running = False
# #end while
# print "GoodBye"