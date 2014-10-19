from os import walk
from sys import argv
from subprocess import call

def main():
	for root, dirs, files in walk("projects/{0}/src".format(argv[1])):
		[call(['subl', '{0}/{1}'.format(root, filename)]) for filename in files]

if __name__ == '__main__':
	main()