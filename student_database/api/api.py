from django.core.paginator import Paginator
from ..models import marks,student,StudentContactDetails


class MarksPerStudentApi(object):
    @classmethod
    def get_list(cls, order_by=['registration_no'],page='1',items_per_page=10):

        student_marks=marks.objects.order_by(*order_by)
        if page == 1:
            return student_marks,None
        paginator = Paginator(student_marks, items_per_page)
        marks = paginator.page(page)
        return marks, paginator

    @classmethod
    def get(cls, registration_no=None):

        try:
            registration_no_list= marks.objects.get(registration_no=registration_no)
            return registration_no

        except marks.DoesNotExist as e:
            raise e

    @classmethod
    def create(cls, data):

        # check if registration number is present;
        if 'registration_no' not in data or data['registration_no'] is None:
            print 'Invalid Registration Number'

        registration_no_list=marks(**data)
        registration_no_list.save()
        return registration_no_list


    @classmethod
    def delete(cls,registration_no=None):
        try:
            enrolled_student=marks.objects.get(registration_no=registration_no)
            enrolled_student.delete()
            return enrolled_student
        except marks.DoesNotExist as e:
            raise e


    @classmethod
    def update(cls,registration_no,data,**kwargs):
        try:
            marks_of_student = marks.objects.get(registration_no=registration_no)
            marks_of_student.load.save()
            return marks_of_student
        except marks.DoesNotExist as e:
            raise e


class studentApi(object):

    @classmethod
    def get_list(cls, order_by=['name'],page='1',items_per_page=10):

        student_list=student.objects.order_by(*order_by)
        if page == -1:
            return student_list,None

        paginator = Paginator(student_list,items_per_page)
        students = paginator.page(page)
        return students, paginator

    @classmethod
    def get(cls,name=None):
        try:
            student_list=student.objects.get(name=name)
            return student_list
        except student.DoesNotExist:
            print 'student does not exist'



    @classmethod
    def create(cls,data):
        if 'registration_no' not in data or data['registration_no'] is None:
            print 'Registration number not mentioned'

        student_data=student(**data)
        student_data.save()
        return student_data

    @classmethod
    def delete(cls,registration_no,data,**kwargs):
        try:
            student_data = student.objects.get(registration_no=registration_no)
            student_data.delete()
            return  student_data
        except student.DoesNotExist:
            print 'student not found '

    @classmethod
    def update(cls, branch,data,**kwargs):
        try:
            student_data = student.objects.get(branch=branch)
            student_data.load_from_dict(data)
            student_data.save()
            return student_data
        except student.DoesNotExist:
            print 'somthings fishy'




class StudentContactDetailsApi(object):

    @classmethod
    def get_list(cls, order_by=['mobile_no'],page='1',items_per_page=10):
        student_data = StudentContactDetails.objects.order_by(*order_by)
        if page == -1:
            return student_data, None
        paginator = Paginator(student_data,items_per_page)
        student_contacts=paginator.page(page)
        return student_contacts, paginator

    @classmethod
    def get(cls,title=None):
        try:



    