from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import errors


class ClassroomSnippets(object):
    def __init__(self, service):
        self.service = service

    def add_student(self, course_id):
        """ Adds a student to a course. """
        service = self.service
        # [START classroom_add_student]
        enrollment_code = 'grc4obp'
        student = {
            'userId': 'tertuserr@gmail.com'
        }
        try:
            student = service.courses().students().create(
                courseId=course_id,
                enrollmentCode=enrollment_code,
                body=student).execute()
            print(
                '''User {%s} was enrolled as a student in
                   the course with ID "{%s}"'''
                % (student.get('profile').get('name').get('fullName'),
                   course_id))
        except errors.HttpError as error:
            print('You are already a member of this course.')
        # [END classroom_add_student]
            return error
        return student

if __name__ == '__main__':
    ClassroomSnippets.add_student('233667426861', '233667426861')