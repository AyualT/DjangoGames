from typing import Any, Dict
from django.shortcuts import render, redirect
from .models import Game, Review, ReviewLike
from .forms import GameForm, ReviewForm
# from django.views.generic import ListView,DetailView
from django_filters.views import FilterView
from .filter import GameFilter

from hitcount.views import HitCountDetailView

class AllGamesView(FilterView):
    model = Game
    paginate_by = 2
    template_name = 'games/games_list.html'
    queryset = Game.objects.filter(is_active = True).order_by('-release_date')
    filterset_class = GameFilter
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        # context['form'] = GameSearch(self.request.get)
        return context
        # if query is not None:
            
# def create_review(gid,uid):

from django.db.models import Sum

class GameView(HitCountDetailView):
    model = Game
    count_hit = True
   
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        if context['game'].trailer_url is not None:
            context['game'].trailer_url = context['game'].trailer_url[context['game'].trailer_url.rfind('/'):]
        revs = Review.objects.filter(game_id = context['game'].pk)
        context.update({
            'recommended': Game.objects.filter(is_active = True).exclude(pk = context['game'].pk).order_by('-hit_count_generic__hits')[:3],
            'reviews': revs,
            'review_count': revs.count(),
        })
        if revs.count() != 0:
            context.update({
                'average_rating':revs.aggregate(Sum('rating'))['rating__sum']/revs.count(),
            })
        else:
            context.update({
                'average_rating': 'No reviews'
            })

        for review in context['reviews']:
            review.likes = ReviewLike.objects.filter(review_id = review.pk, value = 1).count()
            review.dislikes = ReviewLike.objects.filter(review_id = review.pk, value = 0).count()

            try:
                review.is_liked = ReviewLike.objects.get(user_id = self.request.user.pk, review_id = review.pk, value = 1)
                review.is_liked = True
            except:
                review.is_liked = False
            try:
                review.is_disliked = ReviewLike.objects.get(user_id = self.request.user.pk,review_id = review.pk, value = 0)
                review.is_disliked = True
            except:
                review.is_disliked = False
        
        # print(context['reviews'][0].likes)
        return context
    
# def review_like(request, rid, uid):

# def review_

def create_review(request, gid,uid):
    game = Game.objects.get(pk=gid)
    if request.method != 'POST':
        form = ReviewForm()
    else:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author_id = uid
            review.game_id = gid
            review.save()
            return redirect('game_detail', pk=gid)
    return render(request, 'games/game_review.html', {'form':form, 'game':game})

def like_review(request,gid, rid, uid):
    try:
        like = ReviewLike.objects.get(user_id=uid, review_id = rid, value = 1).delete()
    except:
        like = ReviewLike.objects.create(user_id=uid, review_id = rid, value = 1)      
        try:
            like = ReviewLike.objects.get(user_id=uid, review_id = rid, value = 0).delete()
        except:
            pass
    return redirect('game_detail', pk=gid)

def dislike_review(request,gid, rid, uid):
    try:
        dislike = ReviewLike.objects.get(user_id=uid, review_id = rid, value = 0).delete()
    except:
        dislike = ReviewLike.objects.create(user_id=uid, review_id = rid, value = 0)      
        try:
            like = ReviewLike.objects.get(user_id=uid, review_id = rid, value = 1).delete()
        except:
            pass
    return redirect('game_detail', pk=gid)

def game_new(request):
    if request.method == "POST":    
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            return redirect('game_detail', pk=game.pk)
    else:
        form = GameForm()
    return render(request, 'games/game_new.html', {'form':form})

def game_edit(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            return redirect('game_detail', pk=game.pk)
    else:
        form = GameForm(instance=game)
    return render(request, 'games/game_new.html', {'form':form})