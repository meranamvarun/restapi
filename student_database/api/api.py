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
    def get_list(cls, order_by=['registration_no'],page='1',items_per_page=10):

        student_list=student.objects.order_by(*order_by)
        if page == -1:
            return student_list,None

        paginator = Paginator(student_list,items_per_page)
        students = paginator.page(page)
        return students, paginator

    @classmethod
    def get(cls,branch=None):
        try:
            student_list=student.objects.get(branch=branch)
            return student_list
        except student.DoesNotExist:
            print 'branch does not exist'



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
    def update(cls, registration_no,data,**kwargs):



    @classmethod
    def update(cls, field, data, **kwargs):

        try:
            field_list = FieldList.objects.get(field=field)

            field_list.load_from_dict(data)
            field_list.save()
            return field_list

        except FieldList.DoesNotExist:
            print 'Field not found'


class BooksListApi(object):

    @classmethod
    def get_list(cls, order_by=['title'], page='1', items_per_page=10):

        books_list = BookList.objects.order_by(*order_by)
        if page == -1:
            return books_list, None

        paginator = Paginator(books_list, items_per_page)
        books = paginator.page(page)
        return books, paginator

    @classmethod
    def get(cls, title=None):
        try:
            books_list = BookList.objects.filter(title__contains=title)
            return books_list
        except BookList.DoesNotExist:
            print 'books not found'

    @classmethod
    def create(cls, data):

        # check if title is present:
        if 'title' not in data or data['title'] is None:
            print 'Invalid Name'

        books_list = BookList(**data)
        books_list.save()
        return books_list

    @classmethod
    def delete(cls, title=None):
        try:
            book = BookList.objects.get(title=title)
            book.delete()
            return book
        except BookList.DoesNotExist:
            print 'Book not found'

    @classmethod
    def update(cls, title, data, **kwargs):

        try:
            _list = BookList.objects.get(title=title)

            _list.load_from_dict(data)
            _list.save()
            return _list

        except BookList.DoesNotExist:
            print 'Book not found'




