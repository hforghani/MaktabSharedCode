from django.urls import path

from feedback.views import FeedbackFormView, SuccessView, ShowFeedbacks

app_name = "feedback"

urlpatterns = [
    path("", FeedbackFormView.as_view(), name="feedback"),
    path("success/", SuccessView.as_view(), name="success"),
    path("list/", ShowFeedbacks.as_view(), name="list"),
]
