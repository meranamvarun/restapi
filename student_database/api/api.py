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




