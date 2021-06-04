from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "This is January",
    "february": "This is february",
    "march": "This is march",
    "april": "This is april",
    "may": "This is may",
    "jun": "This is jun",
    "july": "This is july",
    "august": "This is august",
    "september": "This is september",
    "october": "This is october",
    "november": "This is november",
    "december": None,
}


# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/monthly_challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})
