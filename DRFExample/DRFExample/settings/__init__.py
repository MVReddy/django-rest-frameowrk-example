"""
DRFExample local settings package

App-specific settings go here instead of clouding up your project settings.

Environment-dependent settings should go into the appropriate
sub-module (settings.local, settings.dev, etc.).  Shared settings
should go into the settings.shared module.  To use these settings,
import the app_settings variable exposed here.  app_settings must
be imported as shown (`from DRFExample.settings.app_settings import MY_VAR`
will not work).

E.g.
>>> from DRFExample.settings import app_settings
>>> print app_settings.MY_VAR

The app_settings module is dynamic so that in the prod environment
the print statement will print settings.prod.MY_VAR.

>>> print app_settings.APP_ROOT

Since app_settings is combined with environment settings,
this will print settings.shared.APP_ROOT in all environments.

"""

from importlib import import_module
from mass_dal.settings import curr_env


app_settings = import_module('DRFExample.settings.' + curr_env)
