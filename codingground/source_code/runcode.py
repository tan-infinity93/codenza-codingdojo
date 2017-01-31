import sys

import commands

if(sys.argv[2] == 'c'):
	
	s, v = commands.getstatusoutput('gcc %s' % sys.argv[1])
	
	if(s==0):

		print "\nProgram compiled successfully"		

		commands.getoutput('chmod +x a.out')
		w = commands.getoutput('./a.out')
		print w

	else:
		
		print "Compilation Errors"
		print v

elif(sys.argv[2] == 'cpp'):

	s, v = commands.getstatusoutput('g++ %s' % sys.argv[1])

	if(s==0):

		print "\nProgram compiled successfully"		

		commands.getoutput('chmod +x a.out')
		w = commands.getoutput('./a.out')
		print w

	else:
		
		print "Compilation Errors"
		print v

elif(sys.argv[2] == 'php'):

	s, v = commands.getstatusoutput('php %s' % sys.argv[1])

	if(s==0):

		print "\nProgram compiled successfully"		

		#commands.getoutput('chmod +x a.out')
		#w = commands.getoutput('./a.out')
		print v

	else:
		
		print "Compilation Errors"
		print v

elif(sys.argv[2] == 'py'):

	s, v = commands.getstatusoutput('python %s' % sys.argv[1])

	if(s==0):

		print "\nProgram compiled successfully"
		print v

	else:
		
		print "Compilation Errors"
		print v

else:

	print "Please provide proper input"