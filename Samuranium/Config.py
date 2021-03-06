import configparser
import os

from Samuranium.utils.paths import PROJECT_ROOT_PATH


class Config:
    def __init__(self, context=None):
        self.config_file_location = os.path.join(PROJECT_ROOT_PATH, '.samuranium')
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_location)
        self.context = context

    @property
    def cli_params(self):
        if self.context:
            return self.context.config.userdata
        return []

    @property
    def is_mobile(self):
        return True

    @property
    def default_browser_options(self):
        return {
            'browser': 'CHROME',
            'headless': False
        }

    @property
    def browser(self):
        if self.cli_params:
            cli_browser = self.cli_params.get('browser', None)
            if cli_browser:
                return cli_browser
        return self.get_property('browser', 'browser')

    @property
    def browser_options(self):
        if self.config.has_section('browser'):
            return dict(self.config.items('browser'))
        return self.default_browser_options

    @property
    def default_wait_time(self):
        default_wait_time = 30
        return float(self.get_property('browser', 'max_wait_time') or default_wait_time)

    def get_property(self, category, key):
        try:
            return self.config.get(category, key).replace('"', '').replace("'", '')
        except:
            return None