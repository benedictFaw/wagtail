from django.urls import path

from wagtail.snippets.views import chooser, snippets

app_name = "wagtailsnippets"
urlpatterns = [
    path("", snippets.Index.as_view(), name="index"),
    path(
        "choose/<slug:app_label>/<slug:model_name>/",
        chooser.ChooseView.as_view(),
        name="choose",
    ),
    path(
        "choose/<slug:app_label>/<slug:model_name>/results/",
        chooser.ChooseResultsView.as_view(),
        name="choose_results",
    ),
    path(
        "choose/<slug:app_label>/<slug:model_name>/chosen/<str:pk>/",
        chooser.ChosenView.as_view(),
        name="chosen",
    ),
    path("<slug:app_label>/<slug:model_name>/", snippets.List.as_view(), name="list"),
    path(
        "<slug:app_label>/<slug:model_name>/results/",
        snippets.List.as_view(results_only=True),
        name="list_results",
    ),
    path(
        "<slug:app_label>/<slug:model_name>/add/",
        snippets.Create.as_view(),
        name="add",
    ),
    path(
        "<slug:app_label>/<slug:model_name>/edit/<str:pk>/",
        snippets.Edit.as_view(),
        name="edit",
    ),
    path(
        "<slug:app_label>/<slug:model_name>/multiple/delete/",
        snippets.Delete.as_view(),
        name="delete-multiple",
    ),
    path(
        "<slug:app_label>/<slug:model_name>/delete/<str:pk>/",
        snippets.Delete.as_view(),
        name="delete",
    ),
    path(
        "<slug:app_label>/<slug:model_name>/usage/<str:pk>/",
        snippets.Usage.as_view(),
        name="usage",
    ),
    path(
        "<slug:app_label>/<slug:model_name>/history/<str:pk>/",
        snippets.HistoryView.as_view(),
        name="history",
    ),
    # legacy URLs that could potentially collide if the pk matches one of the reserved names above
    # ('add', 'edit' etc) - redirect to the unambiguous version
    path("<slug:app_label>/<slug:model_name>/<str:pk>/", snippets.redirect_to_edit),
    path(
        "<slug:app_label>/<slug:model_name>/<str:pk>/delete/",
        snippets.redirect_to_delete,
    ),
    path(
        "<slug:app_label>/<slug:model_name>/<str:pk>/usage/", snippets.redirect_to_usage
    ),
]
