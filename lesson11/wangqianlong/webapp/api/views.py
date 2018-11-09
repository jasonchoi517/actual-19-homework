
import os
import subprocess
from django.shortcuts import render,HttpResponse

# Create your views here.


sum_html = '''
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title>Python19 Platform</title>

		<link href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
		<link href="/static/css/main.css" rel="stylesheet">
		<link href="/static/css/extend.css" rel="stylesheet">
	</head>

	<body>

		<nav class="navbar top-bg-color navbar-fixed-top">
			<div class="container-fluid">
				<div class="navbar-header">
					<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
						<span class="sr-only">Toggle navigation</span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
				   </button>
				   <a class="navbar-brand" href="#"><font color="#F0F8FF">Python19 Platform</font></a>
				</div>
				<div id="navbar" class="navbar-collapse collapse">
					<ul class="nav navbar-nav navbar-right">
						<li><a href="#"><font color="#F0F8FF">退出</font></a></li>
					</ul>
				</div>
			</div>
		</nav>

    <div class="container-fluid">
		<div class="row">
			<div class="col-sm-3 col-md-2 sidebar">
				<ul class="nav nav-sidebar">
					<li class="active"><a href="/dashboard">仪表盘</a></li>
					<li><a href="/command">命令执行</a></li>
					<li><a href="/sum">求和</a></li>
				</ul>
			</div>
			<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
				<h1 class="page-header">Dashboard</h1>
						
                <h3 >{} + {} = {}</h3>
                               
			</div>
		</div>
    </div>

	</body>
</html>


'''


def hello(requets):
	return HttpResponse('hello world')

def command_v1(request):
	cmd_exec_response = '''
	1233
	
	'''
	return HttpResponse(cmd_exec_response)

def command_v2(request):
	cmd = request.GET.get('cmd')
	cmd_exec_response = os.popen(cmd).read()
	return HttpResponse(cmd_exec_response)





def command_v3(request):
    cmd = request.GET.get('cmd')
    pipe = subprocess.Popen(cmd,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE,close_fds=True)
    pipe.wait()
    stdout = pipe.stdout.read().decode('utf-8')
    stderr = pipe.stderr.read().decode('utf-8')
    if stdout:
        # s = '''
        # <h1 style = 'background-color:green;'>{}</h1>
        # '''.format(stdout)
        return HttpResponse(stdout)
    if stderr:
        # s = '''
        #       <h1 style = 'background-color:red;'>{}</h1>
        #       '''.format(stderr)
        return HttpResponse(stderr)
    return HttpResponse('unknow except')



def ssum(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    if num1 and num2:
        try:
            cmd = int(num1) + int(num2)
            ssum_html = sum_html.format(num1, num2, cmd)
            return HttpResponse(ssum_html)
        except Exception as e:
            return e.args
    else:
        return 'num1 and num2 are all required'


def pageSum(request):
    htmlStr='''
    <!DOCTYPE html>
   
    <html>
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
	<body>
		<form method="get" action="http://127.0.0.1:8000/ssum/">
			num1:<input type="text" name="num1" />
			num2:<input type="text" name="num2" />
			<input  type="submit" value="求和"/>
			
		</form>>
	</body>
    </html>
    '''
    return HttpResponse(htmlStr)



def file(request):
    cmd = request.GET.get('file')
    pipe = subprocess.Popen(cmd,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE,close_fds=True)
    pipe.wait()
    stdout = pipe.stdout.read().decode('utf-8')
    stderr = pipe.stderr.read().decode('utf-8')
    if stdout:
        s = '''
        <h1 style = 'background-color:green;'>{}</h1>
        '''.format(stdout)
        return HttpResponse(s)
    if stderr:
        s = '''
              <h1 style = 'background-color:red;'>{}</h1>
              '''.format(stderr)
        return HttpResponse(s)
    return HttpResponse('unknow except')

def pageSum_v2(request):
    cmd = 'cat templates/form_sum.html'
    pipe = subprocess.Popen(cmd,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE,close_fds=True)
    # pipe.wait()
    htmlstr = pipe.stdout.read().decode('utf-8')
    return HttpResponse(htmlstr)

def pageSum_v3(request):

    return render(request,'form_sum.html')

