from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant
from .forms import RestaurantForm, RestaurantSearchForm


def restaurant_list(request):
    restaurants = Restaurant.objects.all().order_by('name')
    search_form = RestaurantSearchForm(request.GET or None)

    if search_form.is_valid() and search_form.cleaned_data['specialization']:
        query = search_form.cleaned_data['specialization']
        restaurants = restaurants.filter(specialization__icontains=query)

    return render(request, 'dz13/restaurant_list.html', {
        'restaurants': restaurants,
        'search_form': search_form,
    })


def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dz13:restaurant_list')
    else:
        form = RestaurantForm()

    return render(request, 'dz13/restaurant_form.html', {'form': form})


def restaurant_update(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('dz13:restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)

    return render(request, 'dz13/restaurant_form.html', {'form': form, 'restaurant': restaurant})


def restaurant_delete(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        restaurant.delete()
        return redirect('dz13:restaurant_list')

    return render(request, 'dz13/restaurant_confirm_delete.html', {'restaurant': restaurant})
