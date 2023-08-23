from typing import Any, Dict
from django.shortcuts import render,redirect
from .models import Publisher
from games.models import Game
from .forms import PublisherForm
from django.views.generic import ListView,DetailView

from hitcount.views import HitCountDetailView

class AllPublishersView(ListView):
    model = Publisher
    template_name = 'publisher/publishers_list.html'
    # queryset = 
    paginate_by = 4
    context_object_name = 'publishers'
    
class PublisherView(HitCountDetailView):
    model = Publisher
    template_name = 'publisher/publisher_detail.html'
    context_object_name = 'publisher'
    count_hit = True
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        games_list = Game.objects.filter(publisher = context['publisher'].pk)
        context['games_list'] = games_list
        context.update({
            'recommended': Publisher.objects.filter(is_active = True).exclude(pk = context['publisher'].pk).order_by('-hit_count_generic__hits')[:3]
        })
        return context
# def publishers_list(request):
#     publishers = Publisher.objects.all()
#     for i in range(len(publishers)):
#         publishers[i].games_list = Game.objects.filter(publisher = publishers[i].pk).all()
#     return render(request, "publisher/publishers_list.html", {"publishers":publishers})

    
# def publisher_detail(request,pk):
#     publisher = get_object_or_404(Publisher, pk=pk)
#     games_list = Game.objects.filter(publisher = publisher.pk).all()
#     return render(request, 'publisher/publisher_detail.html',{'publisher':publisher, 'games_list':games_list})

def publisher_new(request):
    if request.method == "POST":    
        form = PublisherForm(request.POST, request.FILES)
        if form.is_valid():
            publisher = form.save(commit=False)
            publisher.save()
            return redirect('publisher_detail', pk=publisher.pk)
    else:
        form = PublisherForm()
    return render(request, 'publisher/publisher_new.html', {'form':form})

def publisher_edit(request, pk):
    publisher = Publisher.objects.get(pk=pk)
    if request.method == "POST":
        form = PublisherForm(request.POST, request.FILES, instance=publisher)
        if form.is_valid():
            publisher = form.save(commit=False)
            publisher.save()
            return redirect('publisher_detail', pk=publisher.pk)
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'publisher/publisher_new.html', {'form':form})