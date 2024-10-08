from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
# Create your views here.

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

# Add a new item
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

# Edit an existing item
def edit_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form})