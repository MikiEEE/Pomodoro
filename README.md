# Pomodoro
Pomodoro Method Web App
<H3>TASK:</H3>

<p>Your client is a freelance designer who needs to track their time. They would like to use the Pomodoro Technique to track
working time on projects in real-time, to increase productivity. Times tracked must be assigned to a project, and the data
must be exportable via CSV for reporting purposes.</p>

https://en.wikipedia.org/wiki/Pomodoro_Technique

<H4>Requirements:</H4>
<ul>
<li>Support the Pomodoro Technique in real-time</li>
<li>Data should be persistent</li>
<li>Application should be publicly available</li>
<li>Application should be production-ready, whatever that means to you</li>
<li>Please submit your code as a PR so we can easily comment on it</li>
<li>During the code review, you are free to make code changes in response to feedback if you feel it is waranted</li>
</ul>

<H3>My Solution So Far:</H3>

<p>I decided to tackle this problem from the direction of a small Flask web app.
The mainpage will be a menu that tasks can be added to. The tasks are selected and the timer is run.
At the end of the timer interval, the task selected is updated on the server.
The user can then download a CSV with fieldName[Task, Time(minutes)]</p>

<H3>Things to do:</H3>
<ul>
<li>Add use/installation instructions to readme</li>
<li>Comment all functions</li>
</ul>

<H3>QuickStart</H3>
<ul>
<li>Create Virtual Environment python3 -m venv venv</li>
<li>Activate Virtual Environment . venv/bin/activate</li>
<li>pip install flask flask_dynamo</li>
<li>AWS credentials needed for dynamo_db message me for these</li>
</ul>
