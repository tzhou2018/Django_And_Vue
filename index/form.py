from django import forms
from .models import *
from django.core.exceptions import ValidationError


# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=20, label='名字',)
#     weight = forms.CharField(max_length=50, label='重量')
#     size = forms.CharField(max_length=50, label='尺寸')
#     choices_list = [(i+1, v['type_name']) for i,v in enumerate(Type.objects.values('type_name'))]
#     type = forms.ChoiceField(choices=choices_list, label='产品类型')


#自定义验证函数
def weight_validate(value):
    if not str(value).isdigit():
        raise ValidationError("请输入正确的质量")


class ProductModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductModelForm, self).__init__(*args, **kwargs)
        type_obj = Type.objects.values('type_name')
        choices_list = [(i+1, v['type_name']) for i, v in enumerate(type_obj)]
        self.fields['type'].choices = choices_list
        self.fields['name'].initial  = '我的手机'

    productId = forms.CharField(max_length=20, label='产品序号')

    class Meta:
        model = Product
        fields = ['name', 'weight', 'size', 'type']
        exclude = []
        labels = {
            'name': '产品名称',
            'weight': '重量',
            'size': '尺寸',
            'type': '产品类型',
         }
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'cl'}),

        }
        field_classes = {
            'name': forms.CharField
        }
        help_texts = {
            'name': ''
        }
        #自定义错误
        error_messages = {
            '__all__': {'required': '请输入内容',
                        'invalid': '检查输入内容'},
            'weight': {'required': '请输入重量数值',
                       'invalid': '请检查数值是否正确'}
        }
    print("zheli")
    def clean_weight(self):
        data = self.cleaned_data['weight']
        print("zhere2")
        return data+'kg'











class ProductForm(forms.Form):
    name = forms.CharField(max_length=20, label='名字',
                           widget=forms.widgets.TextInput(attrs={'class': 'cl'}),
                           error_messages={'required': '名字信息不能为空'},)
    weight = forms.CharField(max_length=40, label='重量', validators=[weight_validate])
    choices_list = [(i+1, v['type_name']) for i, v in enumerate(Type.objects.values('type_name'))]
    type = forms.ChoiceField(widget=forms.widgets.Select(attrs={'class': 'type','size':'4'}),
                             choices=choices_list, label="产品类型")