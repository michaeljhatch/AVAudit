import os, hashlib

# Location of md5 for each piece of malware we'll be looking for
locations = [r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\ZeusGameover_Feb2014\ZeusGameover_Feb2014.md5",
             r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\ZeroAccess\ZeroAccess.md5",
             r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\Win32.Sality\Win32.Sality.md5",
             r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\Keylogger.Ardamax\Keylogger.Ardamax.md5",
             r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\Ransomware.Matsnu\Ransomware.Matsnu.md5",
             r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\Rustock\Rustock.md5",
             r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\BlackEnergy2.1\BlackEnergy2.1.md5",
             r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\Trojan.Bladabindi\Trojan.Bladabindi.md5",
             r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\Trojan.Regin\Trojan.Regin.md5",
             r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\Trojan.Stabuniq\Trojan.Stabuniq.md5"]

# location of the actual malware
zip_locations = [r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\ZeusGameover_Feb2014\ZeusGameover_Feb2014.zip",
                 r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\ZeroAccess\ZeroAccess.zip",
                 r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\Win32.Sality\Win32.Sality.zip",
                 r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\Keylogger.Ardamax\Keylogger.Ardamax.zip",
                 r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\Ransomware.Matsnu\Ransomware.Matsnu.zip",
                 r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\Rustock\Rustock.zip",
                 r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\BlackEnergy2.1\BlackEnergy2.1.rar",
                 r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\Trojan.Bladabindi\Trojan.Bladabindi.zip",
                 r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\Trojan.Regin\Trojan.Regin.zip",
                 r"C:\Users\ACMS Tech\Desktop\theZoo\malwares\Binaries\Trojan.Stabuniq\Trojan.Stabuniq.zip"]


locations_list = [open(filename, 'r') for filename in locations]

# Locations of files with the same md5 as mw
paths_found = []

# Actual md5 for each mw
hashes = []

#Calculates hashes
for locs in locations_list:
        loc_tuple = locs.read().split()
        loc_hash = loc_tuple[0]
        hashes.append(loc_hash)


 
folder = 'C:\\'

print("Working...")

# Scan C drive for md5s belonging to mw
for (root, dirs, files) in os.walk(folder):
        for file in files:
                try:
                        this_file = os.path.join(root, file)
                        this_md5 = hashlib.md5()

                        with open(this_file, 'rb') as FIN:
                                this_md5.update(FIN.read())

                        for x in hashes:
                                if (this_md5.hexdigest() in hashes):
                                        paths_found.append(this_file)

                # Currently not interfering with anything we care about
                # Add print statements if losing files
                except (FileNotFoundError, PermissionError):
                        pass

# Eliminates duplicate entries
found_paths = list(set(paths_found))


#if not found_paths:
#        print("No matches")
#else:
#        print(found_paths)

# Removes entries from known sources
# If working, found_paths should have the locations of MW after execution
for location in zip_locations:
        for file in found_paths:
                if (os.path.samefile(file, location)):
                        found_paths.remove(file)




if not found_paths:
        print("locations as expected")
else:
        print("Spacing")
        print(found_paths)
