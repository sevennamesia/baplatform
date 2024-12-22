from genericpath import exists
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from baweb import models
from baweb.forms.userforms import UserChangePasswordForm
from ..forms.courseforms import CourseFileForm
import os

def file_list(request, id):
    course = models.Course.objects.filter(id=id).first()
    file_list = models.CourseFiles.objects.filter(course=course).all()
    info_dict = request.session.get('info')
    username = info_dict['name']
    user_id = info_dict['id']
    changepwd_form = UserChangePasswordForm
    user = models.User.objects.filter(id=info_dict['id']).first()
    coursefileform = CourseFileForm
    if user.type == 2:
        is_teacher = 1
        if course.teacher.user != user:
            return redirect("/")
    else:
        is_teacher = 0
        student = models.StudentInfo.objects.filter(user=user).first()
        exists = models.StudentCourse.objects.filter(student=student,course=course)
        if not exists:
            return redirect("/")
    content = {
        "username": username,
        "id": user_id,
        "changepwd_form": changepwd_form,
        "course": course,
        "is_teacher": is_teacher,
        "file_list": file_list,
        "coursefileform": coursefileform
    }
    return render(request, 'file_list.html', content)

@csrf_exempt
def file_add(request, id):
    '''上传课件'''
    course = models.Course.objects.filter(id=id).first()
    info_dict = request.session.get('info')
    user = models.User.objects.filter(id=info_dict['id']).first()
    if user.type == 2:
        if course.teacher.user != user:
            return JsonResponse({"status":False})
    else:
        student = models.StudentInfo.objects.filter(user=user).first()
        exists = models.StudentCourse.objects.filter(student=student,course=course)
        if not exists:
            return JsonResponse({"status":False})
    form = CourseFileForm(request.POST, request.FILES)
    if form.is_valid():
        names = request.POST.getlist("file_name")
        files = request.FILES.getlist("file")
        resource_intros = request.POST.getlist("resource_intro")  # 获取资源简介列表
        category_names = request.POST.getlist("category_name")  # 获取文件类别列表
        course = models.Course.objects.filter(id=id).first()
        for i in range(len(files)):
            try:
                models.CourseFiles.objects.create(
                    file_name=names[i], 
                    file=files[i], 
                    course=course,
                    resource_intro=resource_intros[i],  # 保存资源简介
                    category_name=category_names[i]  # 保存文件类别
                )
            except Exception as e:
                return JsonResponse({"status": False, "error": str(e)})  # 处理异常
        return JsonResponse({"status":True})
    return JsonResponse({"status":False})


def file_update(request, id, fid):
    '''更新课件'''
    title = "更新课件"
    if request.method == 'GET':
        form = CourseFileForm
        context = {
            'form': form,
            'title': title,
        }
        return render(request, "change.html", context)
    old_obj = models.CourseFiles.objects.filter(id=fid).first()
    form = CourseFileForm(request.POST, request.FILES, instance=old_obj)
    if form.is_valid():
        obj = form.save(commit=False)
        course = models.Course.objects.filter(id=id).first()
        obj.course = course
        # 保存资源简介和文件类别
        obj.resource_intro = form.cleaned_data.get('resource_intro')
        obj.category_name = form.cleaned_data.get('category_name')
        obj.save()
    return redirect('/course/{}/file/list'.format(id))


def file_add_batch(request, id):
    '''上传课件'''
    title = "上传课件"
    if request.method == 'GET':
        form = CourseFileForm
        number = int(request.GET['q', 0]) # 获取数量，处理可能的键不存在情况
        context = {
            'form': form,
            'title': title,
            'number_list': range(number)
        }
        return render(request, "change_in_batch.html", context)
    form = CourseFileForm(request.POST, request.FILES)
    if form.is_valid():
        file_name_list = request.POST
        file_list = request.FILES
        resource_intro_list = request.POST.getlist("resource_intro")  # 获取资源简介列表
        category_name_list = request.POST.getlist("category_name")  # 获取文件类别列表
        #print(file_name, file_list)
        course = models.Course.objects.filter(id=id).first()
        for i in range(number):
            #file_name = file_name_list[i]
            #file = file_list[i]
            #models.CourseFiles.objects.create(
                #file_name=file_name, course=course, file=file)
            try:
                models.CourseFiles.objects.create(
                    file_name=file_name_list[i],
                    file=file_list[i],
                    course=course,
                    resource_intro=resource_intro_list[i],  # 保存资源简介
                    category_name=category_name_list[i]  # 保存文件类别
                )
                print(file_list)
            except Exception as e:
                return JsonResponse({"status": False, "error": str(e)})  # 处理异常
        print(file_list)
    return redirect('/course/{}/file/list'.format(id))


def file_delete(request, id, fid):
    '''删除课件'''
    dir = "media/"
    deletefile = models.CourseFiles.objects.filter(id=fid)
    for i in deletefile:
        ##print(dir+'{}'.format(i.file.name))
        os.remove(dir+'{}'.format(i.file.name))
    models.CourseFiles.objects.filter(id=fid).delete()
    return redirect('/course/{}/file/list'.format(id))
