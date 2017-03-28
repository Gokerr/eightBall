from django.shortcuts import render
import string
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def all(request):
    r.sadd('antwoorden','It is certain')
    r.sadd('antwoorden', 'It is decidedly so')
    r.sadd('antwoorden', 'Without a doubt')
    r.sadd('antwoorden', 'Yes definitely')
    r.sadd('antwoorden', 'You may rely on it')
    r.sadd('antwoorden', 'As I see it, yes')
    r.sadd('antwoorden', 'Most likely')
    author_list = r.srandmember('antwoorden')

    if request.method == 'POST':
        values = request.POST.get('values')


        return render(request, 'ball/ok.html', {'author_list': author_list})
    else:
        return render(request, 'ball/vragen.html')
