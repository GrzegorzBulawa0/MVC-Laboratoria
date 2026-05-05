from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Avg, Count


from .models import Film, Ocena, Rezyser
from .forms import FilmForm, OcenaForm

# Create your views here.
def index(request):
    return render(request, 'wykaz_filmow/index.html')

@login_required
def filmy(request):
    filmy = Film.objects.annotate(
        avg_rating=Avg('ocena__rating'),
        liczba_ocen=Count('ocena')
    ).order_by('date_added')

    query = request.GET.get('q')
    sort = request.GET.get('sort')

    if query:
        filmy = filmy.filter(text__icontains=query)

    if sort == 'best':
        filmy = filmy.order_by('-avg_rating')
    elif sort == 'worst':
        filmy = filmy.order_by('avg_rating')
    elif sort == 'oldest':
        filmy = filmy.order_by('date_added')
    else:
        filmy = filmy.order_by('-date_added')

    paginator = Paginator(filmy, 5)
    page_number = request.GET.get('page')
    filmy = paginator.get_page(page_number)    

    context = {'filmy': filmy}
    return render(request, 'wykaz_filmow/filmy.html', context)

@login_required
def film(request, film_id):
    film = Film.objects.get(id=film_id)

    sort = request.GET.get('sort')

    oceny = film.ocena_set.all()

    if sort == 'best':
        oceny = oceny.order_by('-rating')
    elif sort == 'worst':
        oceny = oceny.order_by('rating')
    elif sort == 'oldest':
        oceny = oceny.order_by('date_added')
    else:
        oceny = oceny.order_by('-date_added')

    paginator = Paginator(oceny, 5)  
    page_number = request.GET.get('page')
    oceny = paginator.get_page(page_number)

    czy_ocenil = False
    if request.user.is_authenticated:
        czy_ocenil = Ocena.objects.filter(
            film=film,
            user=request.user
        ).exists()

    context = {'film': film, 'oceny': oceny, 'czy_ocenil': czy_ocenil,}
    return render(request, 'wykaz_filmow/film.html', context)

@login_required
def nowy_film(request):
    if request.method != 'POST':
        form = FilmForm()
    else:
        form = FilmForm(data=request.POST)

        if form.is_valid():
            film = form.save(commit=False)

            rezyser_nazwa = form.cleaned_data['nowy_rezyser'].title()

            film.rezyser, created = Rezyser.objects.get_or_create(
                name=rezyser_nazwa
            )

            film.save()
            return redirect('wykaz_filmow:filmy')

    return render(request, 'wykaz_filmow/nowy_film.html', {'form': form})

@login_required
def nowa_ocena(request, film_id):
    film = Film.objects.get(id=film_id)

    if Ocena.objects.filter(film=film, user=request.user).exists():
        return redirect('wykaz_filmow:film', film_id=film_id)

    if request.method != 'POST':
        form = OcenaForm()
    else:
        form = OcenaForm(data=request.POST)
        if form.is_valid():
            nowa_ocena = form.save(commit=False)
            nowa_ocena.film = film
            nowa_ocena.user = request.user 
            nowa_ocena.save()
            return redirect('wykaz_filmow:film', film_id=film_id)
    
    context = {'film': film, 'form': form}
    return render(request, 'wykaz_filmow/nowa_ocena.html', context)

@login_required
def edit_ocena(request, ocena_id):
    ocena = Ocena.objects.get(id=ocena_id)
    film = ocena.film

    if ocena.user != request.user:
        return redirect('wykaz_filmow:film', film_id=film.id)

    if request.method != 'POST':
        form = OcenaForm(instance=ocena)
    else:
        form = OcenaForm(instance=ocena, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('wykaz_filmow:film', film_id=film.id)
        
    context = {'ocena': ocena, 'film': film, 'form':form}
    return render(request, 'wykaz_filmow/edit_ocena.html', context)

@login_required
def delete_ocena(request, ocena_id):
    ocena = get_object_or_404(Ocena, id=ocena_id)
    film = ocena.film

    if ocena.user != request.user:
        return redirect('wykaz_filmow:film', film_id=film.id)

    if request.method == "POST":
        ocena.delete()
        return redirect('wykaz_filmow:film', film_id=film.id)

    context = {'ocena': ocena, 'film': film}
    return render(request, 'wykaz_filmow/delete_ocena.html', context)