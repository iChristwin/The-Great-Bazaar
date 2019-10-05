from django.shortcuts import render, redirect


def create_review(request, form_class, subject, rating):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.subject = subject
            review.save()
            stars = int(review.rating)
            rating.rate(stars)
            return redirect('review:details', kwargs={'pk': review.pk})
    else:
        return render(request, 'review/create.html',
                      {'form': form_class()},)

# All tests!!!!
