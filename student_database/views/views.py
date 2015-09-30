from django.shortcuts import render
from django.views.generic import View
from ..api.api import MarksApi,studentApi,StudentContactDetailsApi
import json

from django.http import JsonResponse
from django.http import HttpResponse

class MarksView(View):
    http_method_names = ['get', 'put', 'post', 'delete']
    def get(self,request,**kwargs):
        if kwargs.get('registration_no',None) is not None:
            registration_no=kwargs.get('registration_no')
            try:
                student_data=MarksApi.get(registration_no)
                response=student_data.to_dict()
                return JsonResponse(response,safe=False)
            except Exception as e:
                return HttpResponse(e)

        else:
            order_by = request.GET.get('orderBy','branch').split(',')
            items_per_page = 10

            try:
                page=int(request.GET.get('page',1))
            except ValueError:
                page=1
            try:
                _list,paginator = MarksApi.get(order_by=order_by,items_per_page=items_per_page,page=page)


                if paginator is None:
                    _list = [student_data.to_dict() for student_data in _list]
                    response={'registration_no':_list}

                else:
                    _list = [student_data.to_dict() for student_data in _list.object_list]
                    response = _list

                return JsonResponse(response, safe=False)
            except Exception as e:
                raise e

    def post(self, request):
        try:
            data = json.loads(request.body)
        except Exception as e:
            raise e

        try:
            student_data = MarksApi.create(data)
            response = student_data.to_dict()
            return JsonResponse(response, safe=False)
        except Exception as e:
            raise e

    def put(self, request, **kwargs):

        if kwargs.get('registration_no', None) is not None:
            registration_no = kwargs.get('registration_no')
            try:
                data = json.loads(request.body)
            except Exception as e:
                raise e

            try:
                student_data = MarksApi.update(registration_no, data)
                response = student_data.to_dict()
                return JsonResponse(response, safe=False)
            except Exception as e:
                raise e
        else:
            return HttpResponse('null')

    def delete(self, request, **kwargs):

        if kwargs.get('registration_no', None) is not None:
            registration_no = kwargs.get('registration_no')
            print registration_no

            try:
                student_data = MarksApi.delete(registration_no)
                response = student_data.to_dict()
                return JsonResponse(response, safe=True)
            except Exception as e:
                return e
        else:
            pass


class studentView(View):
    http_method_names = ['get', 'put', 'post', 'delete']

    def get(self, request, **kwargs):
        if kwargs.get('name', None) is not None:
            field = kwargs.get('name')
            try:
                student_data = studentApi.get(field)
                response = student_data.to_dict()
                return JsonResponse(response, safe=True)
            except Exception as e:
                raise e

        else:
            order_by = request.GET.get('orderBy', 'name').split(',')
            items_per_page = 10
            try:
                page = int(request.GET.get('page', 1))
            except ValueError:
                page = 1

            try:
                _list, paginator = studentApi.get_list(order_by=order_by, items_per_page=items_per_page, page=page)
                if paginator is None:
                    _list = [student_data.to_dict() for student_data in _list]
                    response = {'name_data': _list}
                else:
                    _list = [student_data.to_dict() for student_data in _list.object_list]
                    response = _list

                return JsonResponse(response, safe=False)
            except Exception as e:
                raise e

    def post(self, request, **kwargs):
        try:
            data = json.loads(request.body)
        except Exception as e:
            raise e

        try:
            name_data = studentApi.create(data)
            response = name_data.to_dict()
            return JsonResponse(response, safe=False)
        except Exception as e:
            raise e

    def put(self, request, **kwargs):

        if kwargs.get('name', None) is not None:
            branch = kwargs.get('name')

            try:
                data = json.loads(request.body)
            except Exception as e:
                raise e

            try:
                student_data = studentApi.update(branch, data)
                response = student_data.to_dict()
                return JsonResponse(response, safe=False)
            except Exception as e:
                raise e
        else:
            pass

    def delete(self, request,  **kwargs):

        if kwargs.get('name', None) is not None:
            field = kwargs.get('name')

            try:
                student_data = studentApi.delete(field)
                response = student_data.to_dict()
                return JsonResponse(response, safe=True)
            except Exception as e:
                return e
        else:
            pass