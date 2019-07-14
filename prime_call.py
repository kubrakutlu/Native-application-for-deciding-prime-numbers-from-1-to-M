import time
import subprocess
import os

print("\t**********************************************")
print("\t*****  Programming Assignment  *****")
print("\t**********************************************")

M = input("Please enter a positive integer number: ")
print("\n")

COUNT_PRIME = 0
COUNT_NONPRIME = 0
EXECUTION_TIME_1 = 0
EXECUTION_TIME_2 = 0
CWD = os.getcwd() #current working directory
#print(cwd)

for pythonMessage in range(1, int(M)+1):
    value = str(pythonMessage).encode("UTF-8")
    timeoutInSeconds = 1 #timeout value
    cmd = [CWD+"/Prime", value] #Prime is the release file of native command application
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    timeStarted = time.time() #start time
    #print(proc.communicate()[0].decode())
    cmdTimer = "sleep "+str(timeoutInSeconds)
    cmdKill = "kill "+str(proc.pid)+" 2>/dev/null"
    cmdTimeout = cmdTimer+" && "+cmdKill              # Combine commands above.
    procTimeout = subprocess.Popen(cmdTimeout, shell=True)      # Start timeout.
    output = proc.communicate()[0].decode()               # End of the process.
    print(output)
    timeDelta = time.time() - timeStarted
    
    if output == str(pythonMessage)+' is a prime number.'+'\n':
        COUNT_PRIME += 1
        EXECUTION_TIME_1 += timeDelta
    elif output == str(pythonMessage)+' is not a prime number.'+'\n':
        COUNT_NONPRIME += 1
        EXECUTION_TIME_2 += timeDelta
print("Number of primes: %d (total execution time: %.10f in seconds)"
      % (COUNT_PRIME, EXECUTION_TIME_1))
print("Number of non-primes: %d (total execution time: %.10f in seconds) \n"
      % (COUNT_NONPRIME, EXECUTION_TIME_2))
