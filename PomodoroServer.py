from flask import Flask, request, redirect, url_for, render_template,send_file
from flask_dynamo import Dynamo
from boto3.dynamodb.conditions import Key, Attr
import boto3
import csv

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('project')
app = Flask(__name__)



'''
I need to decorate the timer and add a break time alert.
I need to let the person know what they have selected
I need to have an instruction page and a delete link
Then I need to get rid of the log comments
'''


app = Flask(__name__)
app.config['DYNAMO_TABLES'] = [
    {
        'TableName':'project',
        'KeySchema':[
        dict(AttributeName='project_name', KeyType='HASH'),
        ],
        'AttributeDefinitions':[
        dict(AttributeName='project_name', AttributeType='S'),
        ],
        'ProvisionedThroughput':dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
    }
]

dynamo = Dynamo(app)

with app.app_context():
    dynamo.create_all()

    @app.route('/pomodoro', methods=['GET', 'POST'])
    def startpage():
            response = table.scan()
            items = response['Items']
            Projects = tuple(item['project_name'] for item in items)

            if len(Projects) == 0:
                return redirect('/instructions')

            return render_template('pomodoroMainPage.html',Tasks = Projects)

    @app.route('/addProject', methods=['GET'])
    def AddProject():
            response = table.scan()
            items = response['Items']
            Projects = tuple(item['project_name'] for item in items)

            return render_template('addProject.html',Tasks = Projects)

    @app.route('/newProject', methods=['POST'] )
    def newProject():
        #This checks for repeats , Im not sure if this is necescary
        response = table.scan()
        items = response['Items']
        projectsFromDB = {item['project_name'] for item in items}

        if request.form['newProject'] not in projectsFromDB:
            dynamo.tables['project'].put_item(
            Item={
                'project_name':request.form['newProject'],
                'completedIntervals':0
            })
        return redirect('/addProject')

    @app.route('/deleteProject', methods=['GET', 'POST'])
    def deleteProject():
        if request.method == 'GET':
            response = table.scan()
            items = response['Items']
            Projects = tuple(item['project_name'] for item in items)
            return  render_template('deleteProject.html',Tasks = Projects)

        elif request.method == 'POST':
            key = request.form['delProject']
            table.delete_item(
                Key = {
                    'project_name':key
                }
            )
        return redirect('/deleteProject')

    @app.route('/instructions', methods=['GET'])
    def NeedGuidanceNow():
        response = table.scan()
        items = response['Items']
        Projects = tuple(item['project_name'] for item in items)
        return  render_template('instructions.html',Tasks = Projects)

    @app.route('/downloadPomodoro',methods=['POST','GET'])
    def downloadFile ():

        path = 'outputs/PomodoroWork.csv'
        response = table.scan()
        items = response['Items']

        with open(path, 'w') as csvfile:
            fieldnames = ['project_name', 'completedIntervals']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(items)
        return send_file(path,mimetype='text/csv',as_attachment=True,attachment_filename='downloadFile.csv')


    @app.route('/finishedPomodoro',methods=['POST'])
    def processPomodoro():
        try:
            key = 'project_name'
            query = request.json['name']

            response = table.get_item(
                Key={
                        key: query,
                    }
            )

            item = response['Item']
            currentIntervals = item['completedIntervals']
            newInterval = currentIntervals + 1

            table.update_item(
                Key={
                    'project_name':query,
                },
                UpdateExpression='SET timer =  :newTime',
                ExpressionAttributeValues={
                ':newTime': newInterval
                }
            )
        except KeyError:
            print('KEY ERROR: something is most likley wrong with the main dictionary')
        else:
            print('Successfully Processed Pomodoro for task:',query)
        return redirect('/pomodoro')
