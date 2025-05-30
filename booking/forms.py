from django import forms


SAUNA_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,11)]


class BookingAddSaunaForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=SAUNA_QUANTITY_CHOICES,
        coerce = int
    )
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)