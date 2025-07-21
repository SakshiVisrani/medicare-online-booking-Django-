# forms.py
from .models import Booking

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
