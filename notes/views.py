from django.shortcuts import redirect, render

from .models import Note


def note_list(request):
    if request.method == "POST":
        Note.objects.create(text=request.POST["text"])
        return redirect("note_list")

    notes = Note.objects.order_by("-created")
    return render(request, "notes/list.html", {"notes": notes})
