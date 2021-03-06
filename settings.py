# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""
import os
from conf.default import *  # noqa
"""
You can load different configurations depending on yourcurrent environment.

 This can be the following values:

      development
      testing
      production
"""

ENVIRONMENT = os.environ.get("BK_ENV", "development")
# Inherit from environment specifics
conf_module = "conf.settings_%s" % ENVIRONMENT

try:
    module = __import__(conf_module, globals(), locals(), ['*'])
except ImportError, e:
    raise ImportError("Could not import conf '%s' (Is it on sys.path?): %s" % (conf_module, e))

for setting in dir(module):
    if setting == setting.upper():
        locals()[setting] = getattr(module, setting)


# check saas app  settings
try:
    saas_conf_module = "conf.settings_saas"
    saas_module = __import__(saas_conf_module, globals(), locals(), ['*'])
    for saas_setting in dir(saas_module):
        if saas_setting == saas_setting.upper():
            locals()[saas_setting] = getattr(saas_module, saas_setting)
except:
    pass

#cache
CACHES = {
 'default': {
  #'BACKEND': 'django.core.cache.backends.db.DatabaseCache',  # 指定缓存使用的引擎
  #'LOCATION': 'appconfig_cache',         # 写在内存中的变量的唯一值 
  'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
  'LOCATION': '/var/tmp/django_cache',     #/var/tmp/django_cache|c:/foo/bar
  'TIMEOUT':None,             # 缓存超时时间(默认为300秒,None表示永不过期)
  'OPTIONS':{
   'MAX_ENTRIES': 10000,           # 最大缓存记录的数量（默认300）
   'CULL_FREQUENCY': 3,          # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
  }  
 }
}
