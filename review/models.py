from django.db import models

# Create your models here.
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


class Review(models.Model):
    STARS = ((5, '5 stars'),
             (4, '4 stars'),
             (3, '3 stars'),
             (2, '2 stars'),
             (1, '1 star'),
             )
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                 blank=True, verbose_name="Reviewer")
    rating = models.IntegerField(default=0, choices=STARS)
    comment = models.TextField(default='')
    review_time = models.DateTimeField(auto_now_add=True, blank=True)
    subject = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                verbose_name='Rated user')

    class Meta:
        abstract = True
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')

    def __str__(self):
        return "%(user)s reviews %(subject)s" % ({'user': self.reviewer,
                                                  'subject': self.subject})

    def get_absolute_url(self):
        return reverse("review:details", kwargs={'pk': self.pk})


class UserReview(Review):
    subject = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                related_name='%(class)s_user',
                                verbose_name='Reviewed user')

    class Meta:
        verbose_name = _('User Review')
        verbose_name_plural = _('User Reviews')


class Rating(models.Model):
    star_count_1 = models.IntegerField(default=0)
    star_count_2 = models.IntegerField(default=0)
    star_count_3 = models.IntegerField(default=0)
    star_count_4 = models.IntegerField(default=0)
    star_count_5 = models.IntegerField(default=0)
    star_sum = models.IntegerField(default=0)
    review_count = models.IntegerField(default=0)
    current_rating = models.FloatField(default=0)

    class Meta:
        abstract = True
        verbose_name = _('Rating')
        verbose_name_plural = _('Rating')

    def rate(self, stars):
        if stars == 1:
            self.star_count_1 += 1
        if stars == 2:
            self.star_count_2 += 2
        if stars == 3:
            self.star_count_3 += 3
        if stars == 4:
            self.star_count_4 += 4
        if stars == 5:
            self.star_count_5 += 5
        self.star_sum += stars
        self.review_count += 1
        self.current_rating = (self.star_sum/self.review_count)
        self.save()

    def get_absolute_url(self):
        return reverse("rating:details", kwargs={'pk': self.pk})


class UserRating(Rating):
    subject = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                   verbose_name='Rated User')

    class Meta:
        verbose_name = _('User Rating')
        verbose_name_plural = _('User Ratings')

    def __str__(self):
        return "User ratings: %(name)s" % ({'name': self.subject.username, })

