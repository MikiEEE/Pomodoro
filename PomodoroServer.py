from flask import Flask, request, redirect, url_for, render_template,send_file
from Task import Task
taskDict = dict()
app = Flask(__name__)

'''
So Far I have a method that can add tasks and print them to the html page
What I need to do is hook up the timer to be able to update the tasks
then I need to be able to print it all to a csv and download it.
the timer is client side
I need to add csv functionallity and bring the drop down menu back with athe tasks in a scroll bar
'''

@app.route('/pomodoro', methods=['GET', 'POST'])
def startpage():
        return render_template('PomodoroMainpage.html',Tasks = taskDict.keys())


@app.route('/newTask', methods=['POST'] )
def newTask():
    if request.form['newTask'] not in taskDict:
        taskDict[request.form['newTask']] = Task(request.form['newTask'])
    return redirect('/pomodoro')


@app.route('/downloadPomodoro',methods=['POST','GET'])
def downloadFile ():
    path = 'outputs/PomodoroWork.csv'
    with open(path, 'w') as CSVfile:
        CSVfile.write('Task,Time(mins),\n')
        for key, value in taskDict.items():
            CSVfile.write(value.toCSV() + '\n')
            print(value.toCSV() )
    return send_file(path,mimetype='text/csv',as_attachment=True,attachment_filename='downloadFile.csv')


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
    return redirect('/pomodoro')
