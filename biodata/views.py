from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Member, UserPreference

ALLOWED_EMAILS = [
    'saffana.firsta@gmail.com',
    'nadiaaiiisyahf@gmail.com',
    'sahila.kh01@gmail.com',
    'keishavnia@gmail.com',
    'alyanabila486@gmail.com',
]


def get_user_preference(user):
    if user.is_authenticated:
        pref, _ = UserPreference.objects.get_or_create(user=user)
        return pref
    return None


def home(request):
    members = Member.objects.all()
    pref = get_user_preference(request.user)
    is_member = (
        request.user.is_authenticated and
        request.user.email in ALLOWED_EMAILS
    )
    return render(request, 'biodata/home.html', {
        'members': members,
        'pref': pref,
        'is_member': is_member,
    })


@login_required
def customize(request):
    if request.user.email not in ALLOWED_EMAILS:
        return redirect('home')

    pref, _ = UserPreference.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        pref.bg_color = request.POST.get('bg_color', pref.bg_color)
        pref.card_color = request.POST.get('card_color', pref.card_color)
        pref.accent_color = request.POST.get('accent_color', pref.accent_color)
        pref.font_family = request.POST.get('font_family', pref.font_family)
        pref.text_color = request.POST.get('text_color', pref.text_color)
        pref.save()
        return redirect('home')

    return render(request, 'biodata/customize.html', {'pref': pref})