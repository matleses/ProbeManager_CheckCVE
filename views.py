import importlib
import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.safestring import mark_safe

from checkcve.tasks import check_cve as task_cve
from core.models import Probe

logger = logging.getLogger(__name__)


@login_required
def check_cve(request, pk):
    """
    Check CVE for an instance.
    """
    probe = Probe.get_by_id(pk)
    my_class = getattr(importlib.import_module(probe.type.lower() + ".models"), probe.type)
    probe = my_class.get_by_id(pk)
    if probe is None:  # pragma: no cover
        return HttpResponseNotFound
    else:
        try:
            task_cve.delay(probe.name)
            messages.add_message(request, messages.SUCCESS, mark_safe("Check CVE launched with succeed. " +
                                 "<a href='/admin/core/job/'>View Job</a>"))
        except Exception as e:  # pragma: no cover
            logger.exception('Check CVE failed ! ' + str(e))
            messages.add_message(request, messages.ERROR, "Check CVE failed ! " + str(e))
    return render(request, probe.type.lower() + '/index.html', {'probe': probe})
