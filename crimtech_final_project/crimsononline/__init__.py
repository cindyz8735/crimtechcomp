from __future__ import absolute_import

# This will make sure the celery app is always imported when
# Django starts so that shared_task will use this app.

from .content.generators import app as celery_app  # noqa
