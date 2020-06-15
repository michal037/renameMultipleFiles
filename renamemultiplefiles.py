# MIT License
# Copyright (c) 2020, Michal Kozakiewicz, github.com/michal037

import os, platform # rename()
import argparse     # main()

def rename(path, new_name='', new_extension=None):
	'''
		This function renames multiple files in the directory.

		Input:
		  path          - directory where rename files
		  new_name      - new file name to set
		  new_extension - new extension to set
		
		Return:
		  None
	'''

	# check types
	if type(path) != str:
		raise TypeError('path have to be string')

	if type(new_name) != str:
		raise TypeError('new_name have to be string')

	if type(new_extension) not in [type(None), type('')]:
		raise TypeError('new_extension have to be string or None')

	# check values
	if not os.path.isdir(path):
		raise Exception('directory given in path does not exist')

	# forbidden characters:    \ / : * ? " < > |
	FORBIDDEN_CHARACTERS = '\x5C\x2F\x3A\x2A\x3F\x22\x3C\x3E\x7C'

	for char in new_name:
		if char in FORBIDDEN_CHARACTERS:
			raise ValueError(
				'the file name cannot contain any of the following ' +
				'characters: ' + FORBIDDEN_CHARACTERS)

	if type(new_extension) == str:
		for char in new_extension:
			if char in FORBIDDEN_CHARACTERS:
				raise ValueError(
					'the file extension cannot contain any of the following ' +
					'characters: ' + FORBIDDEN_CHARACTERS)

		# remove dots from beginning and ending
		new_extension = new_extension.strip('.')

	# add slash / backslash at the end of path
	if platform.system() == 'Windows':
		if path[-1] != '\\':
			path += '\\'
	else:
		if path[-1] != '/':
			path += '/'

	count = 1 # count this way because enumerate includes directories etc.

	for file_name in os.listdir(path):
		# skip other than file
		if not os.path.isfile(path + file_name):
			continue

		dst = new_name + str(count)

		# without specified extension try to use default
		# else for non empty new_extension set this extension
		if new_extension == None:
			dst += os.path.splitext(file_name)[1]
		elif new_extension != '':
			dst += '.' + new_extension

		dst = path + dst
		src = path + file_name

		os.rename(src, dst)
		count += 1


def main():
	parser = argparse.ArgumentParser(
		description='This script renames multiple files in the directory.')
	
	parser.add_argument('path', help='directory where rename files')
	parser.add_argument('-n', '--name', default='', help='new file name to set')
	parser.add_argument('-e', '--extension', default=None,
		help='new extension to set')

	args = parser.parse_args()

	try:
		rename(args.path, args.name, args.extension)
	except Exception as e:
		print('Error: {}'.format(e))
	

if __name__ == '__main__':
	main()
