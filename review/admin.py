from django.contrib import admin

# Register your models here.
from .models import UserReview, UserRating


class UserReviewAdmin(admin.ModelAdmin):
    search_fields = ('reviewer__{0}'.format('username'),)
    model = UserReview
    list_display = ('reviewer', 'subject', 'rating', 'comment', 'review_time')


class UserRatingAdmin(admin.ModelAdmin):
    model = UserRating
    list_display = ('subject', 'current_rating', 'review_count')


admin.site.register(UserReview, UserReviewAdmin)
admin.site.register(UserRating, UserRatingAdmin)
