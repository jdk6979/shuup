# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2016, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext_lazy as _

from shuup.admin.modules.users.views.password import UserResetPasswordView
from shuup.admin.utils.urls import get_model_url
from shuup.core.models import Contact
from shuup.utils.excs import Problem


class ContactResetPasswordView(UserResetPasswordView):
    def get_contact(self):
        return Contact.objects.get(pk=self.kwargs[self.pk_url_kwarg])

    def get_object(self, queryset=None):
        contact = self.get_contact()
        user = getattr(contact, "user", None)
        if not user:
            raise Problem(_(u"The contact does not have an associated user."))
        return user

    def get_success_url(self):
        return get_model_url(self.get_contact())
