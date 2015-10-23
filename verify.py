import os, hashlib, stat, winreg

# Total number of times the loop executes
final_count = 111551

#Rounding to get clean percentages
count_percent = 1116

current_count = 0

# Location of md5 for each piece of malware we'll be looking for
locations = [r"C:\Users\ACMS Tech\AppData\Roaming\AcroIEHelper Module\acroiehelper.exe",
             r"C:\Users\ACMS Tech\AppData\Roaming\GrooveMonitor Utility\groovemonitor.exe",
             r"C:\Users\ACMS Tech\AppData\Roaming\InstallShield Update Service Scheduler\issch.exe",
             r"C:\Users\ACMS Tech\AppData\Roaming\Java Quick Starter\jqs.exe",
             r"C:\Users\ACMS Tech\AppData\Roaming\SoundMAX service agent\smagent.exe",
             r"C:\Users\ACMS Tech\AppData\Roaming\ntkrnl",
             r"C:\Users\ACMS Tech\AppData\Local\userdata.dat",
             r"C:\Users\ACMS Tech\AppData\Local\cmd.exe",
             r"C:\Users\ACMS Tech\AppData\Local\googleupdaterr.exe",
             r"C:\Program Files (x86)\BenFit14\BChelp.exe",
             r"C:\ProgramData\bytedraft\bpvttlpxh.exe"]

reg_keys = {'HKEY_CURRENT_USER': (r"Software\Microsoft\Windows\CurrentVersion\Run", r"Software\Stability Software", r"Software\Win7zip"),
            'HKEY_USERS': r".DEFAULT\Software\Microsoft\Windows\CurrentVersion\Run",
            'HKEY_LOCAL_MACHINE': r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"}




# Locations of files with the same md5 as mw
paths_found = []

keys_found = []

 
folder = 'C:\\'

print("Working...")

# Scan C drive for md5s belonging to mw
for (root, dirs, files) in os.walk(folder):
        for file in files:
                try:
        
                        this_file = os.path.join(root, file)

                        # print(this_file)
                        
                        if this_file in locations:
                              print(this_file)
                              paths_found.append(this_file)

                                        
                # 
                except PermissionError:
                        print("Permission issue at %s" % this_file)

                except (FileNotFoundError):
                        pass

                percent_tracker = current_count % count_percent
                
                current_percent = current_count/count_percent
        
                if(percent_tracker == 0):
                        print("%d percent complete" % current_percent)

                current_count += 1


hkey = list(reg_keys.items())

#print(hkey)

subvals = [] 

keys = []

# COMPLETE THIS  
for i in hkey:
        try:

        
                if i[0] == 'HKEY_LOCAL_MACHINE':
                
                        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, i[1])
                        subvals.append(key)

                elif i[0] == 'HKEY_USERS':
                
                        key = winreg.OpenKey(winreg.HKEY_USERS, i[1])
                        subvals.append(key)

                elif i[0] == 'HKEY_CURRENT_USER':
                        for index in i[1]:
                        
                                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, index)

                        
                                try:
                                        (winreg.EnumValue(key, 0))
                                        keys_found.append(index)

                                except:
                                        continue

        except:
                continue  


#print(keys_found)

# Eliminates duplicate entries
found_paths = list(set(paths_found))

found_keys = list(set(keys_found))




##
if not found_paths:
        print("No malicious executables")
else:
        print(found_paths)

if not found_keys:
        print("Registry keys are clear")
else:
        print(found_keys)

#print(paths_found)

input("Press enter to continue")


