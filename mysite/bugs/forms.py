__author__ = 'eqiihuu'

from time import timezone
from django import forms

STAGE_CHOICES = (('1', 'Ongoing'),
                 ('2', 'Finished')
                 )

class CreateStageForm(forms.Form):
    status = forms.ChoiceField(widget=forms.Select(),
                               choices=STAGE_CHOICES,
                               initial=STAGE_CHOICES[1])
    update_person = forms.CharField(max_length=30)
    note = forms.DateTimeField(required=False,
                               widget=forms.Textarea(attrs={'size': 200, }),
                               label='Note',
                               initial='Detailed information',
                               help_text='500 characters max.')

class CreateBugForm(forms.Form):
    problem = forms.CharField(max_length=30, required=False)
    create_person = forms.CharField(max_length=30, required=False)
    note = forms.CharField(required=False,
                           widget=forms.Textarea(attrs={'size': 200, }),
                           label='Note',
                           initial='Detailed information',
                           help_text='500 characters max.')
# class DeleteeForm(forms.Form):
#     select = forms.CheckboxChoiceInput()