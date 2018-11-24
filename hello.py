from flask import Flask, request, redirect, url_for, render_template
from Task import Task

taskDict = dict()
app = Flask(__name__)

'''
So Far I have a method that can add tasks and print them to the html page
What I need to do is hook up the timer to be able to update the tasks
then I need to be able to print it all to a csv and download it.
the timer is client side
I need to make the post method its own /ADD
'''

@app.route('/', methods=['GET', 'POST'])
def startpage():
        return render_template('hello.html',Tasks = taskDict.keys())

@app.route('/newTask', methods=['POST'] )
def newTask():
    if request.form['newTask'] not in taskDict:
        taskDict[request.form['newTask']] = Task(request.form['newTask'])
    return redirect('/')

@app.route('/finishedPomodoro',methods=['POST'])
def processPomodoro():
    try:
        key = request.json['name']
        print(key)
        taskDict[key].completedInterval()
        print(taskDict[key].numOfIntervals)
    except KeyError:
        print('KEY ERROR: something is most likley wrong with the main dictionary')
    else:
        print('Successfully Processed Pomodoro for task:', key)
    return redirect('/')
