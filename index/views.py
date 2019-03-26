from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# from django.contrib.sessions import serializers
from django.core import serializers
from django.views.decorators.http import require_http_methods
from .form import *
from .models import Product
from .models import Book
import json
import csv
import requests

#這是之前用來練習用的，不用管
# def model_index(request, id):
#     if request.method == "GET":
#         instance = Product.objects.filter(id = id)
#         if instance:
#             product = ProductModelForm(instance=instance[0])
#         else:
#             product = ProductModelForm()
#         return render(request, 'data_form.html', locals())
#     else:
#         print("准备实例化")
#         product = ProductModelForm(request.POST)
#         print("开始判断")
#         if product.is_valid():
#             print("开始打印")
#             weight = product.cleaned_data['weight']
#             print("zhixingzheli1")
#             product_db = product.save(commit=False)
#             product_db.name = '我的ipython'
#             product_db.save()
#             return HttpResponse('提交成功'+ weight)
#         else:
#             error_msg = product.errors.as_json()
#             print(error_msg)
#             return render(request, 'data_form.html', locals())
# # Create your views here.
#
# def download(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
#     writer = csv.writer(response)
#     writer.writerow(['First row', 'A', 'B', 'C'])
#     return response
#
#
# def index(request):
#     '''
#     type_list = Product.objects.values('type').distinct()
#     name_list = Product.objects.values('name', 'type')
#     context = {'title': '首页', 'type_list': type_list, 'name_list': name_list}
#     return render(request, 'index.html', context=context, status=200)
#     '''
#     # GET请求
#     if request.method == 'GET':
#         product = ProductForm()
#         return render(request, 'data_form.html', locals())
#     #Post请求
#     else:
#         product = ProductForm(request.POST)
#         if product.is_valid():
#             name = product['name']
#             cname = product.cleaned_data['name']
#             return HttpResponse("提交成功")
#         else:
#             error_msg = product.errors.as_json()
#             print(error_msg)
#             return render(request, 'data_form.html',locals())
#     # product = ProductForm()
#     # return render(request, 'data_form.html', locals())
#
# # locals()使用技巧
# # def index(request):
# #     type_list = Product.objects.values('type').distinct()
# #     name_list = Product.objects.values('name','type')
# #     title = '首页'
# #     return render(request, 'index.html',context=locals(), status=200)
#
# def login(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         # 相对路径，代表首页地址
#         return redirect('/')
#         # 绝对路径，完整的地址信息
#         # return redirect('http://127.0.0.1:8000/')
#     else:
#         if request.GET.get('name'):
#             name = request.GET.get('name')
#         else:
#             name = 'Everyone'
#         return HttpResponse('username is ' + name)
#
#
# # 通用视图
# from django.views.generic import ListView
#
#
# class ProductList(ListView):
#     # context_object_name设置Html模版的变量名称
#     context_object_name = 'type_list'
#     # 设定HTML模版
#     template_name = 'index.html'
#     # 查询数据
#     queryset = Product.objects.values('type').distinct()
#
#     # 重写 get_queryset 方法，对模型product进行数据筛选。
#     def get_queryset(self):
#     #     获取URL的变量id
#         print(self.kwargs['id'])
#         # 获取URL的参数name
#         print(self.kwargs['name'])
#         # 获取请求方式
#         print(self.request.method)
#         type_list = Product.objects.values('type').distinct()
#         return type_list
#
#     # 添加其他变量
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['name_list'] = Product.objects.values('name', 'type')
#         return context

# Create your views here.
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list']  = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)