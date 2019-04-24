# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from autoproofreader.control import (
    compute_server,
    floodfilling,
    is_installed,
    floodfill_model,
    volume_config,
)

app_name = "autoproofreader"

urlpatterns = [url(r"^is-installed$", is_installed)]

# Skeleton flood filling
urlpatterns += [
    url(r"^(?P<project_id>\d+)/flood-fill$", floodfilling.FloodfillTaskAPI.as_view())
]

# Compute Servers
urlpatterns += [
    url(
        r"^(?P<project_id>\d+)/compute-servers$",
        compute_server.ComputeServerAPI.as_view(),
    ),
    url(r"^(?P<project_id>\d+)/gpu-util$", compute_server.GPUUtilAPI.as_view()),
]

# Floodfilling Models
urlpatterns += [
    url(
        r"^(?P<project_id>\d+)/floodfill-models$",
        floodfill_model.FloodfillModelAPI.as_view(),
    )
]

# Floodfilling Results
urlpatterns += [
    url(
        r"^(?P<project_id>\d+)/floodfill-results$",
        floodfilling.FloodfillResultAPI.as_view(),
    )
]

# Volume Configs
urlpatterns += [
    url(r"^(?P<project_id>\d+)/volume-configs$", volume_config.VolumeConfigAPI.as_view())
]