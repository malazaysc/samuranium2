import unittest
import os
from pathlib import Path

from Samuranium import Samuranium

index_file_path = Path.joinpath(Path(__file__).parent, 'test_utilities', 'mock_web', 'index.html')
page_url = f'file://{index_file_path}'


class BrowserConfigurationsTest(unittest.TestCase):
    """Test different browser configrations"""

    def tearDown(self) -> None:
        self.samu.driver.quit()

    def test_browser_chrome_headless_config_file(self):
        """
        Tests that chrome browser is started with headless mode.
        Configured via .samuranium file
        """
        self.samu = Samuranium()
        self.assertTrue(self.samu.driver_manager.headless)
        self.assertTrue('-headless' in self.samu.driver_manager.chrome_options)
        self.assertEqual(self.samu.driver.capabilities.get('browserName'), 'chrome')

    def test_browser_chrome_headless_args(self):
        """
        Tests that chrome browser is started with headless mode.
        Configured via args
        """
        self.samu = Samuranium(headless=True)
        self.assertTrue(self.samu.driver_manager.headless)
        self.assertTrue('-headless' in self.samu.driver_manager.chrome_options)
        self.assertEqual(self.samu.driver.capabilities.get('browserName'), 'chrome')

    @unittest.skipIf(os.getenv('CI', False), 'Running on CI')
    def test_browser_chrome_not_headless_args(self):
        """
        Tests that chrome browser is started.
        Configured via args
        """
        self.samu = Samuranium(headless=False)
        self.assertFalse(self.samu.driver_manager.headless)
        self.assertFalse('-headless' in self.samu.driver_manager.chrome_options)
        self.assertEqual(self.samu.driver.capabilities.get('browserName'), 'chrome')


if __name__ == '__main__':
    unittest.main()
