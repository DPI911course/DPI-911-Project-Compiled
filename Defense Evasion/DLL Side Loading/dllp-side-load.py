import ctypes, sys, os, re, filecmp, hashlib

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def baseline():
    if is_admin():
        os.system("listdlls64.exe -a > dll-load.txt")
        print("Done! List-dlls in a file")
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        
def dll_sideload():
    if is_admin():
        # Code of your program here
        os.system("listdlls64.exe -a > dll-side-load.txt")
        print("Done! List-dlls in a file")
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    
def open_file(file_name):
    file_exists = False
    while not file_exists:
        try :
            file_object = open(file_name,"r")
            file_exists = True
            break
        except FileNotFoundError:
            print("The specified file could not be found/accessed. Try again.")
            break
        
    lines = file_object.readlines()       
    file_object.close()
    return lines


def store_fun(lines, fileout):
    
    empty_list = []
    for line in lines:
        line.strip()
        line = line.split()
        empty_list.append(line)
        
    r = re.compile(r'.*[\.dll]')
    file_open = open(fileout,"w")
    
    for element in empty_list:
        if "pid:" in element:
            file_open.write(str(element)+'\n')
            file_open.write(str(empty_list[empty_list.index(element)+4])+'\n')
        for ele in element:
            if re.match(r'.*\.dll', ele):
                file_open.write(str(element)+'\n')
                
    file_open.close()


def search_fun(lines, search, filename):
    
    empty_list = []
    for line in lines:
        line.strip()
        line = line.split()
        empty_list.append(line)
        
    r = re.compile(r'.*[\.dll]')
  
    wl = True 
    count = True
   
    print(filename)
    
    file_open = open(filename,"w")
    while(wl == True):
        for element in empty_list:
            if "pid:" in element and search in element:
                file_open.write(str(element)+"\n")
                file_open.write(str(empty_list[empty_list.index(element)+4])+'\n')
                count = False
                continue 
            if count == False:
                for ele in element:
                    if re.match(r'.*\.dll', ele) and re.match(r'.*C:\\', ele):
                        file_open.write(str(element)+'\n')
            #if "pid:" in element and count== False:                
            #break 
        wl = False
    file_open.close()
    

#############
#Create a baseline uncomment the baseline function. 
#############

#baseline()

#############
# To collect the dlls for all running process uncomment dll_sideload() function.
#############
#dll_sideload()

file_name = "dll-load.txt"

def parse_file(baseline_file_name, sideload_file_name, search, compare):
    baseline_P = open_file(baseline_file_name)
    sideload_P = open_file(sideload_file_name)
    store_fun(baseline_P,"baseline.txt")
    store_fun(sideload_P,"sideload-dll.txt")

sideload_P = open_file("dll-load.txt")
load_P = open_file("baseline.txt")
search_fun(sideload_P,"POWERPNT.EXE","POWERPNT1.txt") # powerpnt.exe is an example program that we analyse the dlls for.
search_fun(load_P,"POWERPNT.EXE","POWERPNT2.txt")

print(filecmp.cmp('POWERPNT2.txt','POWERPNT1.txt'))


digests = []
for filename in ['POWERPNT2.txt', 'POWERPNT1.txt']:
    hasher = hashlib.md5()
    with open(filename, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
        a = hasher.hexdigest()
        digests.append(a)
        print(a)

print(digests[0] == digests[1])
