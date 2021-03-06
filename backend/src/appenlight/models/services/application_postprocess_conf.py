# -*- coding: utf-8 -*-

# Copyright 2010 - 2017 RhodeCode GmbH and the AppEnlight project authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from appenlight.models import get_db_session
from appenlight.models.application_postprocess_conf import ApplicationPostprocessConf
from appenlight.models.services.base import BaseService


class ApplicationPostprocessConfService(BaseService):
    @classmethod
    def by_pkey(cls, pkey, db_session=None):
        db_session = get_db_session(db_session)
        query = db_session.query(ApplicationPostprocessConf)
        return query.filter(ApplicationPostprocessConf.pkey == pkey).first()

    @classmethod
    def by_pkey_and_resource_id(cls, pkey, resource_id, db_session=None):
        db_session = get_db_session(db_session)
        query = db_session.query(ApplicationPostprocessConf)
        query = query.filter(ApplicationPostprocessConf.resource_id == resource_id)
        return query.filter(ApplicationPostprocessConf.pkey == pkey).first()
