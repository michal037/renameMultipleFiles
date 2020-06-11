# MIT License
# Copyright (c) 2020, Michal Kozakiewicz, github.com/michal037

import os, platform # rename()
import argparse     # main()

def rename(path, newName='', newExtension=None):
	"""
		This function renames files in the directory.

		Input:
		  path         - directory where rename files
		  newName      - new filename to set (optional)
		  newExtension - new extension to set without dot (optional)
		
		Return:
		  None
	"""

	# add slash / backslash at the end of path
	if platform.system() == 'Windows':
		if path[-1] != '\\':
			path += '\\'
	else:
		if path[-1] != '/':
			path += '/'

	count = 0 # count this way because enumerate includes directories etc.

	for fileName in os.listdir(path):
		# skip other than file
		if not os.path.isfile(path + fileName):
			continue

		dst = newName + str(count)

		# use 'newExtension' if not empty, else use 'fileName' extension
		if newExtension != None:
			dst += '.' + newExtension
		else:
			dst += os.path.splitext(fileName)[1]

		dst = path + dst
		src = path + fileName

		os.rename(src, dst)
		count += 1


def main():
	parser = argparse.ArgumentParser(description='This script renames files in the directory.')
	
	parser.add_argument('path', help='directory where rename files')
	parser.add_argument('-n', '--name', default='', help='new filename to set')
	parser.add_argument('-e', '--extension', default=None, help='new extension to set (without dot)')

	args = parser.parse_args()

	if not os.path.isdir(args.path):
		parser.error('directory does not exist')

	rename(args.path, args.name, args.extension)
	

if __name__ == '__main__':
	main()
