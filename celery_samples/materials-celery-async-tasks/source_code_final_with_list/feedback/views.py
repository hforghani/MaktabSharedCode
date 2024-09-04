from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from celery.result import AsyncResult

from feedback.forms import FeedbackForm
from feedback.models import Feedback
from django_celery.celery import app as celery_app


class FeedbackFormView(FormView):
    template_name = "feedback/feedback.html"
    form_class = FeedbackForm
    success_url = "/success/"

    def form_valid(self, form):
        task_id = form.send_email()
        Feedback.objects.create(
            email=form.cleaned_data["email"],
            message=form.cleaned_data["message"],
            user_id=self.request.user.id,
            task_id=task_id,
            sent=False)
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "feedback/success.html"


class ShowFeedbacks(ListView):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            feedbacks = Feedback.objects.filter(user=self.request.user)
        else:
            feedbacks = Feedback.objects.filter(user__isnull=True)

        for feedback in feedbacks:
            res = AsyncResult(feedback.task_id)
            feedback.sent = res.ready()
            feedback.save()

        return feedbacks


