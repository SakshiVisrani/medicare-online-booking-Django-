# forms.py
from .models import Booking
from .models import Review 
from django import forms
from .models import AppointmentSlot

class SlotBookingForm(forms.Form):
    slot = forms.ModelChoiceField(
        queryset=AppointmentSlot.objects.none(),
        widget=forms.RadioSelect,
        empty_label=None,
        label="Choose a Time Slot"
    )

    def __init__(self, doctor, date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slot'].queryset = AppointmentSlot.objects.filter(
            doctor=doctor,
            date=date,
            is_booked=False
        ).order_by('time')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['slot']  


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        widget=forms.HiddenInput() # This makes it a hidden field
    )
    comment = forms.CharField(
        label="Your Comments (Optional)",
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share your experience...'}),
        required=False
    )

    class Meta:
        model = Review
        fields = ['rating', 'comment']

