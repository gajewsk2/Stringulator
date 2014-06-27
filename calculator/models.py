from django.db import models
from django.contrib.auth.models import User
# from django.forms import ModelForm
# from django import forms

NOTE_CHOICES = (('A', 'A'), ('A#/Bb', 'A#/Bb'), ('B', 'B'), ('C', 'C'), ('C#/Db', 'C#/Db'), ('D', 'D'),
                ('D#/Eb', 'D#/Eb'), ('E', 'E'), ('F', 'F'), ('F#/Gb', 'F#/Gb'), ('G', 'G'), ('G#/Ab', 'G#/Ab'))
OCTAVE_RANGE = 10
STRING_TYPE = (("CKPLG", "Plain Steel - CK"),
               ("CKWNG", "Nickel/Steel Hybrid - CK"),
               ("CKPLB", "Bass - Plain Steel - CK"),
               ("CKWNB", "Bass - Nickel/Steel Hybrid - CK"),
               ("DAPL", "Plain Steel - DA"),
               ("DAPB", "Phosphore Bronze Wound - DA"),
               ("DANW", "Nickel Wound - DA"),
               ("DAXS", "Stainless Steel Wound - DA"),
               ("DAHR", "Half-Round Wound - DA"),
               ("DACG", "Chromes - Stainless Flat wound - DA"),
               ("DAFT", "Flat Tops - Phosphore Bronze  - DA"),
               ("DABW", "80/20 Brass Round Wound - DA"),
               ("DAZW", "85/15 Great American Bronze - DA"),
               ("DAXB", "Bass - Nickel Plated Round Wound - DA"),
               ("DAHB", "Bass - Pure Nickel Half Round - DA"),
               ("DABC", "Bass - Stainless Steel Flat Wound - DA"),
               ("DABS", "Bass - ProSteel Round Wound - DA"))


class StringSet(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    desc = models.CharField(max_length=1000)
    is_mscale = models.BooleanField()
    number_of_strings = models.IntegerField(max_length=2)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class String(models.Model):
    string_set = models.ForeignKey(StringSet)
    string_number = models.IntegerField(max_length=2)
    scale_length = models.CharField(max_length=30)
    note = models.CharField(max_length=5, choices=NOTE_CHOICES)
    octave = models.IntegerField(max_length=2, choices=[(octave, octave) for octave in range(OCTAVE_RANGE)])
    gauge = models.DecimalField(max_digits=5, decimal_places=5)
    string_type = models.CharField(max_length=30, choices=STRING_TYPE)

    class Meta:
        ordering = ['string_number']

#
# class StringForm(ModelForm):
#     def __init__(self, user, *args, **kwargs):
#         super(StringForm, self).__init__(*args, **kwargs)
#         if user is None:
#             self.fields['string_set'] = forms.CharField()
#         else:
#             string_set_list = []
#             for set in StringSet.objects.all():
#                 if str(set.user) == str(user):
#                     string_set_list.append(str(set.name))
#             set_tuple = zip(string_set_list, string_set_list)
#             set_tuple = tuple(set_tuple)
#             self.fields['string_set'] = forms.ChoiceField(set_tuple)
#
#     class Meta:
#         model = String
#
# class StringSetForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(StringSetForm, self).__init__(*args, **kwargs)
#         self.fields['user'].widget.attrs['hidden'] = True
#
#     class Meta:
#         model = StringSet
#         fields = ['name', 'user', 'desc', 'is_mscale', 'number_of_strings']