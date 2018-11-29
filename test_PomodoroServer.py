from PomodoroServer import app
import unittest
import json
class FlaskTestCase(unittest.TestCase):
    #test to see if app is set up correctly
    def test_PomodoroServer(self):
        tester = app.test_client(self)
        response = tester.get('/Pomodoro', content_type='html/text')
        self.assertEqual(response.status_code,200)

    #Testing to see if add project get '/AddProject'
    def test_AddProject(self):
        tester = app.test_client(self)
        response = tester.get('/AddProject',content_type='html/text')
        self.assertEqual(response.status_code,200)

    #Test to see if '/Delete' Loads right page
    def test_DeleteProject(self):
        tester = app.test_client(self)
        response = tester.get('/DeleteProject',content_type='html/text')
        self.assertEqual(response.status_code,200)

    #Test to see if Instructions Loads
    def test_Instructions(self):
        tester = app.test_client(self)
        response = tester.get('/Instructions',content_type='html/text')
        self.assertEqual(response.status_code,200)

    #test to see if Mainpage is set up correctly
    def test_MainPage(self):
        tester = app.test_client(self)
        response = tester.get('/Pomodoro', content_type='html/text')
        self.assertTrue(b'Project Selected' in response.data)

    #test adding new project to Project queue
    def test_newProject(self):
        tester = app.test_client(self)
        response = tester.post('/newProject',data=dict(newProject='saliva'), follow_redirects=True)
        self.assertIn(b'saliva',response.data)

    #test updating of Project List
    def test_AddProjectListUpdate(self):
        tester = app.test_client(self)
        response = tester.post('/newProject',data=dict(newProject='saliva'), follow_redirects=True)
        self.assertIn(b'Projects en Queue', response.data)

    #test addition and deletion of item
    def test_AddDelete(self):
        tester = app.test_client(self)
        response = tester.post('/newProject',data=dict(newProject='saliva'), follow_redirects=True)
        self.assertIn(b'saliva',response.data)
        response = tester.post('/DeleteProject',data=dict(delProject='saliva'), follow_redirects=True)
        self.assertFalse(b'saliva' in response.data)

    #Test downloadCSV
    def test_DownloadCSV(self):
        tester = app.test_client(self)
        response = tester.get('/downloadPomodoro', content_type='csv/text')
        self.assertEqual(response.status_code, 200)

    #Test Timer
    def test_finishedPomodoro(self):
        tester = app.test_client(self)
        response = tester.post('/finishedPomodoro',headers={contentType: "application/json"}, follow_redirects=True)
        self.assertEqual(302,response.status_code)
        assert response.request.path == url_for('/Pomodoro')


    #Test Instructions for content

if __name__ == '__main__':
    unittest.main()
