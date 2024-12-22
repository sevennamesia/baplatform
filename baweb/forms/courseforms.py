from django import forms

from baweb import models
from ..utils.bootstrap import BootStrapModelForm

class CourseForm(BootStrapModelForm):
    class Meta:
        model = models.Course
        fields = ['name', 'course_profile_pic']

class CoursePicForm(BootStrapModelForm):
    class Meta:
        model = models.Course
        fields = ['course_profile_pic']

class CourseFileForm(BootStrapModelForm):
    class Meta:
        model = models.CourseFiles
        fields = ['file', 'file_name', 'resource_intro', 'category_name', 'lesson_id'] # 包含新增字段
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 可以在这里对新增字段进行初始化设置
        self.fields['resource_intro'].widget.attrs.update({'class': 'form-control'})
        self.fields['category_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['lesson_id'].widget.attrs.update({'class': 'form-control'})

class CourseAssignmentForm(BootStrapModelForm):
    class Meta:
        model = models.Assignment
        fields =  ['name', 'ddl', 'is_group']

class CourseStudentImportForm(forms.Form):
    file = forms.FileField(label='学生表')

class CourseCommentForm(BootStrapModelForm):
    class Meta:
        model = models.CourseComment
        fields = ['comment']

#新增排序、筛选
class CourseForm(BootStrapModelForm):
    SORT_CHOICES = (
        ('created_at', '按创建时间排序'),
        ('name', '按课程名称排序'),
    )
    sort_by = forms.ChoiceField(choices=SORT_CHOICES, required=False, label='排序方式')
    category = forms.CharField(max_length=50, required=False, label='筛选类别')


    class Meta:
        model = models.Course
        fields = ['name', 'course_profile_pic','sort_by', 'category']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sort_by'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})