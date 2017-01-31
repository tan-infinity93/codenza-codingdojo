from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import TemplateView

# Code Compilation Modules ##########################

import sys
import commands
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT

######################################################

# Create your views here.

def home_page(request):
    return render(request, 'codingground/index.html', {})

def about_page(request):
    return render(request, 'codingground/about.html', {})

def form_page(request):
    return render(request, 'codingground/form.html', {})

#Form Processing View are Here:-

#disabling csrf (cross site request forgery)
@csrf_exempt

def get_data(request):
    
    #if post request came 
    if request.method == 'POST':
    
        #getting values from post
        extension = request.POST.get('extension')
        code = request.POST.get('code')
        user_input = request.POST.get('user_input')

        print "########################"
        print "#                      #"
        print "     Extension: %s      " % extension
        print "#                      #" 
        print "     Code: %s           " % code
        print "#                      #"
        print "     User Input: %s     " % user_input
        print "########################"

        if(extension == 'c'):

            fo = open('codingground/source_code/C/c_file.c','w+')
            fo.write(code);
            fo.close()

            s, v = commands.getstatusoutput('/usr/bin/gcc -o codingground/source_code/C/a.out codingground/source_code/C/c_file.c')
            
            if(s == 0):
                print "\nCode Compiled Successfully"
                commands.getoutput('chmod +x codingground/source_code/C/a.out')
                output = commands.getoutput('codingground/source_code/C/./a.out')
                print output
                return render(request, 'codingground/index.html', { 'extension': extension, 'code': code, 'output': output })

            else:
                print "\nCompilation Errors"
                print v
                output = v
                return render(request, 'codingground/index.html', { 'extension': extension, 'code': code, 'output': output })

        ############################################################

        if(extension == 'cpp'):

            fo = open('codingground/source_code/C++/cpp_file.cpp','w+')
            fo.write(code)
            fo.close()

            s, v = commands.getstatusoutput('/usr/bin/g++ -o codingground/source_code/C++/a.out codingground/source_code/C++/cpp_file.cpp')

            if(s == 0):
                print "\nCompiled Successfully"
                commands.getstatusoutput('chmod +x codingground/source_code/C++/a.out')
                output = commands.getoutput('codingground/source_code/C++/./a.out')
                print output
                return render(request, 'codingground/index.html', { 'extension': extension, 'code': code, 'output': output })

            else:
                print "\nCompilation Errors"
                print v
                output = v
                return render(request, 'codingground/index.html', { 'extension': extension, 'code': code, 'output': output })

        ######################################################################

        if(extension == 'java'):

            fo = open('codingground/source_code/Java/%s.java' % user_input,'w+')
            fo.write(code)
            fo.close()

            s, v = commands.getstatusoutput('/user/bin/javac codingground/source_code/Java/%s.java' % user_input)

            if(s == 0):

                commands.getstatusoutput('chmod +x codingground/source_code/Java/%s.java' % user_input)
                w = commands.getstatusoutput('/user/bin/java codingground/source_code/Java/%s.class' % user_input)

            return redirect('/')

        ##########################################################################

        if(extension == 'php'):

            fo = open('codingground/source_code/Php/php_file.php','w+')
            fo.write(code)
            fo.close()

            s, v = commands.getstatusoutput('/usr/bin/php codingground/source_code/Php/php_file.php')

            if(s == 0):
                print "\nCompiled Successfully"
                print v
                output = v
                return render(request, 'codingground/index.html', { 'extension': extension, 'code': code, 'output': output })

            else:
                print "\nCompilation Errors"
                print v
                output = v
                return render(request, 'codingground/index.html', { 'extension': extension, 'code': code, 'output': output })

        ##########################################################################

        if(extension == 'py'):

            fo = open('codingground/source_code/Python/python_file.py','w+')
            fo.write(code)
            fo.close()
            """s, v = commands.getstatusoutput('/usr/bin/python /home/tan/Desktop/codingdojo/codingground/source_code/Python/python_file.py')
            if(s == 0):
                print "\nCompiled Successfully"
                print v
                output = v
                return render(request, 'codingground/index.html', { 'extension': extension, 'code': code, 'output': output })
            else:
                print "Compilation Errors"
                print v
                output = v
                return render(request, 'codingground/index.html', { 'extension': extension, 'code': code, 'output': output })
            #return redirect('/')"""
            # First check compilation errors:-
            """
            s, v = commands.getstatusoutput('/usr/bin/python /home/tan/Desktop/codingdojo/codingground/source_code/Python/python_file.py')
            if(s == 0): # Compilation is a Success
                p = Popen(['/usr/bin/python','/home/tan/Desktop/codingdojo/codingground/source_code/Python/python_file.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
                stdout,stderr = p.communicate(input=user_input)
                output = stdout
                print p
                return render(request, 'codingground/index.html', { 'extension': extension, 'code': code, 'output': output })
            else: # Error in Compilation
                print "Compilation Errors"
                print v
                output = v
                return render(request, 'codingground/index.html', { 'extension': extension, 'code': code, 'output': output })
                """

            if(user_input):

                p = Popen(['/usr/bin/python','codingground/source_code/Python/python_file.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
                stdout,stderr = p.communicate(input=user_input)
                output = stdout
                print output
                return render(request, 'codingground/index.html', { 'extension': extension, 'code': code, 'output': output })


            else:
            
                s, v = commands.getstatusoutput('/usr/bin/python codingground/source_code/Python/python_file.py')
                
                if(s == 0):

                    print "\nCompiled Successfully"
                    print v
                    output = v
                    return render(request, 'codingground/index.html', { 'extension': extension, 'code': code, 'output': output })
            
                else:

                    print "Compilation Errors"
                    print v
                    output = v
                    return render(request, 'codingground/index.html', { 'extension': extension, 'code': code, 'output': output })

    else:
        return render(request, 'codingground/index.html', {})

@csrf_exempt

def clear_data(request):

    return redirect('/')