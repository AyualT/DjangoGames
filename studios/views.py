from typing import Any, Dict
from django.shortcuts import render,redirect
from .models import Studio
from games.models import Game
from .forms import StudioForm
from django.views.generic import ListView,DetailView

from hitcount.views import HitCountDetailView

class AllStudiosView(ListView):
    model = Studio
    paginate_by = 5
    # queryset = Game.objects.filter()
    template_name = 'studios/studios_list.html'
    context_object_name = 'studios'

class StudioView(HitCountDetailView):
    model = Studio
    template_name = 'studios/studio_detail.html'
    context_object_name = 'studio'
    count_hit = True

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        games_list = Game.objects.filter(studio = context['studio'].pk, is_active = True)
        context['games_list'] = games_list
        context.update({
            'recommended': Studio.objects.filter(is_active = True).exclude(pk = context['studio'].pk).order_by('-hit_count_generic__hits')[:3]
        })
        return context
    
def studio_new(request):
    if request.method == "POST":    
        form = StudioForm(request.POST, request.FILES)
        if form.is_valid():
            studio = form.save(commit=False)
            studio.save()
            return redirect('studio_detail', pk=studio.pk)
    else:
        form = StudioForm()
    return render(request, 'studios/studio_new.html', {'form':form})

def studio_edit(request, pk):
    studio = Studio.objects.get(pk=pk)
    if request.method == "POST":
        form = StudioForm(request.POST, request.FILES, instance=studio)
        if form.is_valid():
            studio = form.save(commit=False)
            studio.save()
            return redirect('studio_detail', pk=studio.pk)
    else:
        form = StudioForm(instance=studio)
    return render(request, 'studios/studio_new.html', {'form':form})