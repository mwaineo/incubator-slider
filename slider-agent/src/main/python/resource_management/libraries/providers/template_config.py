#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Slider Agent

"""

import os
from resource_management import *

class TemplateConfigProvider(Provider):
  def action_create(self):
    template_tag = self.resource.template_tag
    qualified_file_name = self.resource.name
    file_name = os.path.basename(qualified_file_name)

    if not template_tag:
      template_name = format("{file_name}.j2")
    else:
      template_name = format("{file_name}-{template_tag}.j2")

    with Environment.get_instance_copy() as env:
      File( qualified_file_name,
       owner   = self.resource.owner,
       group   = self.resource.group,
       mode    = self.resource.mode,
       content = Template(template_name, extra_imports=self.resource.extra_imports)
      )
