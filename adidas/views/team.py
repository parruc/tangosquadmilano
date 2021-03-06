from adidas.forms import JoinTeamForm
from adidas.models import Team
from adidas.views.mixins import CaptainRequiredMixin
from adidas.views.mixins import LoginRequiredMixin
from adidas.views.mixins import TeamObjectMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView


class TeamLeaveView(LoginRequiredMixin, View):
    success_url = reverse_lazy("team_view")

    def dispatch(self, *args, **kwargs):
        self.request.user.team = None
        self.request.user.save()
        messages.add_message(self.request, messages.INFO,
                             'Hai abbandonato la squadra')
        return redirect(self.success_url)


class TeamDetailView(LoginRequiredMixin, TeamObjectMixin, DetailView):
    template_name = "adidas/team.html"

    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        context["join_team_form"] = JoinTeamForm()
        return context


class TeamUpdateView(LoginRequiredMixin, CaptainRequiredMixin,
                     TeamObjectMixin, UpdateView):
    success_url = reverse_lazy("team_view")
    fields = ["name", ]


class TeamRemoveView(LoginRequiredMixin, CaptainRequiredMixin,
                     TeamObjectMixin, FormView):
    success_url = reverse_lazy("team_view")


class TeamJoinByHashView(LoginRequiredMixin, View):
    success_url = reverse_lazy("team_view")

    def dispatch(self, *args, **kwargs):
        hash = self.kwargs.get('hash', "")
        team = Team.objects.filter(hash=hash).first()
        player = self.request.user
        if player.is_authenticated:
            if team:
                player.team = team
                player.save()
                messages.add_message(self.request, messages.INFO,
                                     'Ti sei unito alla squadra')
            else:
                messages.add_message(self.request, messages.ERROR,
                                     'Non è possibile aggiungerti alla squadra.\
                                     Verifica il codice inserito.')
        else:
            messages.add_message(self.request, messages.ERROR,
                                 'Puoi visitare questa pagina solo dopo\
                                 esserti autenticato.')
            return redirect(self.login_url)
        return redirect(self.success_url)


class TeamJoinView(LoginRequiredMixin, FormView):
    form_class = JoinTeamForm
    success_url = reverse_lazy("team_view")

    def form_valid(self, form):
        hash = form.cleaned_data.get('hash', "")
        team = Team.objects.filter(hash=hash).first()
        player = self.request.user
        if player.is_authenticated:
            if team:

                player.team = team
                player.save()
                messages.add_message(self.request, messages.INFO,
                                     'Ti sei unito alla squadra')
            else:
                messages.add_message(self.request, messages.ERROR,
                                     'Non è possibile aggiungerti alla squadra.\
                                     Verifica il codice inserito.')
        else:
            messages.add_message(self.request, messages.ERROR,
                                 'Non è possibile aggiungerti alla squadra.\
                                 Verifica il codice inserito.')
        return redirect(reverse("team_view"))

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             'Non hai inserito un codice valido')
        return redirect(self.success_url)

