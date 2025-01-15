from django  import  forms
from .models import Student

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields =("name", "email","roll")
        widgets ={
            'name':forms.TextInput(attrs={'class':'form.control', 'placeholder': 'Enter your name'}),
            'email':forms.EmailInput(attrs={'class':'form.control', 'placeholder': 'Enter your email'}),
            'roll':forms.NumberInput(attrs={'class':'form.control', 'placeholder': 'Enter your roll number'}),

        }
