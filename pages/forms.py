from django import forms
from .models import Profile, FamilyMember, Leave

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ()

class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = "__all__"
        exclude = ()


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = "__all__"




FamilyMemberFormSet = forms.inlineformset_factory(Profile, FamilyMember, form=FamilyMemberForm, extra=1)
