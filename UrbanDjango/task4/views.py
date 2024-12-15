from django.shortcuts import render


def review_temp(request):
    return render(request, 'fourth_task/review.html')

def main_temp(request):
    return render(request, 'fourth_task/main_page.html')

def watchlist_temp(request):
    context = {'movies': ['Крёстный отец','Список Шиндлера','Хороший, плохой, злой']}

    return render(request, 'fourth_task/watchlist.html', context)

