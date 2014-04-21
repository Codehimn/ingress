from subprocess import *
# from os import  communicate

# find_process1 = Popen(['cmd'], stdout=PIPE,stdin=PIPE,stderr=PIPE)
# find_process1.stdin.write(b'cd C:\\Users\\Codehimn\\Dropbox\\ingress\n')
# find_process1.stdin.flush()
# find_process1.stdin.write(b'adb shell\n')
# find_process1.stdin.flush()
# find_process1.stdin.write(b'ls\n')
# find_process1.stdin.flush()
# find_process1.stdin.write(b'\n')
# find_process1.stdin.flush()

# find_process1.stdin.write(b'exit\n')
# find_process1.stdin.flush()
# out, err = find_process1.communicate()

# print(out)

find_process1 = Popen(['cmd'], stdout=PIPE,stdin=PIPE,stderr=PIPE,universal_newlines=True)
find_process1.stdin.write('cd C:\\Users\\Codehimn\\Dropbox\\ingress\n')
# find_process1.stdin.flush()
find_process1.stdin.write('adb shell\n')
# find_process1.stdin.flush()
find_process1.stdin.write('ls\n')
# find_process1.stdin.flush()
find_process1.stdin.write('\n')
# find_process1.stdin.flush()

find_process1.stdin.write('exit\n')
find_process1.stdin.flush()
out, err = find_process1.communicate()

print(out)