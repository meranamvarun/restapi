from django.db import models

# Create your models here.
from django.utils.translation import pgettext_lazy



class marks(models.Model):
    registration_no=models.IntegerField(
        verbose_name=pgettext_lazy('Registration Number','Registration No'),
    )
    marks_in_x = models.IntegerField(
        verbose_name=pgettext_lazy('marks in class X', 'Marks_In_X'),

    )

    marks_in_xii = models.IntegerField(
        verbose_name=pgettext_lazy('marks in class XII', 'Marks_In_XII'),
    )

    cgpi = models.IntegerField(
        verbose_name=pgettext_lazy('CGPI out of 10', 'CGPI'),
    )


    def to_dict(self):
        dictionary = {
            'id' : self.pk,
            'registration_no':self.registration_no,
            'marks_in_x':self.marks_in_x,
            'marks_in_xii':self.marks_in_xii,
            'cgpi':self.cgpi,
        }

        return dictionary

    def load_from_dict(self,updates):
        for field, value in updates.iteritems():
            if hasattr(self, field):
                self.__setattr__(field, value)

    def __str__(self):
        return self.cgpi

    class Meta:
        app_label='student_database'


class student(models.Model):
    name=models.CharField(
        verbose_name=pgettext_lazy('name of the student','Student Name'),
        max_length=10,
    )

    roll_no=models.IntegerField(
        verbose_name=pgettext_lazy('roll no of student','Roll No'),
    )

    registration_no=models.ForeignKey(
        marks,
        verbose_name=pgettext_lazy('Registration Number','Registration No'),
        related_name='registartion_num_student'
    )

    branch=models.CharField(
        verbose_name=pgettext_lazy('Branch of Student','Branch of Student'),
        max_length=5,
    )

    mobile_no=models.IntegerField(
        verbose_name=pgettext_lazy('mobile number of student','Mobile No'),
    )


    def to_dict(self):
        dictionary= {

            'name':self.name,
            'roll_no':self.roll_no,
            'registration_no':self.registration_no.to_dict(),
            'branch':self.branch,
        }
        return dictionary

    def load_from_dict(self, updates):
        for field, value in updates.iteritems():
            if hasattr(self, field):
                self.__setattr__(field, value)

    def __str__(self):
        return self.name

    class Meta:
        app_label='student_database'


class StudentManager(models.Manager):
    def get_list(self, title):
        results=self.filter(title_contains=title)
        return results.to_dict()

    def update_copies(self, title,copies,add=False):
        result=self.filter(title=title)
        prev_copies = result['copies']
        if add:
            result.update(copies=prev_copies+copies)
        else:
            result.update(copies=prev_copies-copies)
        return self.filter(title=title).to_dict()

    class Meta:
        app_label='student_database'


class StudentContactDetails(models.Model):
    email_id=models.CharField(
        verbose_name=pgettext_lazy('Email Id','Email Id'),
        max_length=256,
    )

    mobile_no=models.ForeignKey(
        student,
        verbose_name=pgettext_lazy('mobile number of student','Mobile No'),
        related_name='mobile_number',
    )

    address=models.CharField(
        verbose_name=pgettext_lazy('Address of Student','Student Address'),
        max_length=200,
    )

    objects=StudentManager


    def to_dict(self):
        dictionary={
            'email':self.email_id,
            'mobile_no':self.mobile_no.to_dict(),
            'address':self.address,
        }

        return dictionary

    def load_from_dict(self, updates):
        for field, value in updates.iteritems():
            if hasattr(self, field):
                self.__setattr__(field, value)

    class Meta:
        app_label='student_database'

