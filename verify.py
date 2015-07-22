import os, hashlib

fullpath = r"C:\Users\ACMS Tech\Desktop\AVAudit\test\test1.txt"
realpath = os.path.realpath(fullpath)

das_hash = hashlib.md5(open(realpath, 'rb').read()).hexdigest()
 
folder = 'C:\\'

for (root, dirs, files) in os.walk(folder):
	for file in files:
		try:
			this_file = os.path.join(root, file)
			this_md5 = hashlib.md5()

			with open(this_file, 'rb') as FIN:
				this_md5.update(FIN.read())

			if (this_md5.hexdigest() == das_hash):
				print("Found it at %s" % this_file)
			else:
				print(this_md5.hexdigest())

		except FileNotFoundError:
			print("File not found. Y U do dis Windows?")

		except PermissionError:
			pass