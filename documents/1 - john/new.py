import os
from sys import argv
from subprocess import call

def main():
	project_directory = 'projects/{}'.format(argv[1])
	if not os.path.exists(project_directory):
		os.makedirs(project_directory)
		os.makedirs('{}/bin'.format(project_directory))
		os.makedirs('{}/src'.format(project_directory))
		with open('{}/src/{}.cpp'.format(project_directory, argv[1]), 'w') as f:
			f.write('\n')
			f.write('\n')
			f.write('int main() {\n')
			f.write('\n')
			f.write('\treturn 0;\n')
			f.write('}')
		call(['subl', '{}/src/{}.cpp'.format(project_directory, argv[1])])
		print("Project {} created.".format(argv[1]))
	else:
		print("Project {} already exists!".format(argv[1]))
	
if __name__ == '__main__':
	main()