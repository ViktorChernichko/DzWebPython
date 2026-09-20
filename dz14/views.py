from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book, Reader
from .forms import BookForm, ReaderForm


@login_required
@permission_required('dz14.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'dz14/book_list.html', {'books': books})


@login_required
@permission_required('dz14.add_book', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dz14:book_list')
    else:
        form = BookForm()

    return render(request, 'dz14/book_form.html', {'form': form})


@login_required
@permission_required('dz14.change_book', raise_exception=True)
def book_update(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('dz14:book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'dz14/book_form.html', {'form': form, 'book': book})


@login_required
@permission_required('dz14.delete_book', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('dz14:book_list')

    return render(request, 'dz14/book_confirm_delete.html', {'book': book})


@login_required
@permission_required('dz14.view_reader', raise_exception=True)
def reader_list(request):
    readers = Reader.objects.all().order_by('full_name')
    return render(request, 'dz14/reader_list.html', {'readers': readers})


@login_required
@permission_required('dz14.add_reader', raise_exception=True)
def reader_create(request):
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dz14:reader_list')
    else:
        form = ReaderForm()

    return render(request, 'dz14/reader_form.html', {'form': form})


@login_required
@permission_required('dz14.change_reader', raise_exception=True)
def reader_update(request, reader_id):
    reader = get_object_or_404(Reader, id=reader_id)

    if request.method == 'POST':
        form = ReaderForm(request.POST, instance=reader)
        if form.is_valid():
            form.save()
            return redirect('dz14:reader_list')
    else:
        form = ReaderForm(instance=reader)

    return render(request, 'dz14/reader_form.html', {'form': form, 'reader': reader})


@login_required
@permission_required('dz14.delete_reader', raise_exception=True)
def reader_delete(request, reader_id):
    reader = get_object_or_404(Reader, id=reader_id)

    if request.method == 'POST':
        reader.delete()
        return redirect('dz14:reader_list')

    return render(request, 'dz14/reader_confirm_delete.html', {'reader': reader})
