from django.shortcuts import render, get_object_or_404

# Create your views here.
from journal.models import Entry


def entry_list(request):
    entries = Entry.objects.all().order_by("-date")
    return render(request, 'journal/entry_list.html', {'entries': entries})


def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'journal/entry_detail.html', {'entry': entry})