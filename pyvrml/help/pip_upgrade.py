from subprocess import call

import pip
from pip._internal.utils.misc import get_installed_distributions

# 通过pip更新已安装的库
for dist in get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)
