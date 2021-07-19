import unittest
from pathlib import Path

from ddt import ddt, data
from selenium.webdriver.common.by import By

from Samuranium import Samuranium

index_file_path = Path.joinpath(Path(__file__).parent, 'test_utilities', 'mock_web', 'index.html')
page_url = f'file://{index_file_path}'


@ddt
class BrowserActionsTest(unittest.TestCase):
    def setUp(self):
        self.samu = Samuranium()
        self.samu.navigate(page_url)

    def tearDown(self) -> None:
        self.samu.driver.quit()

    def test_navigate(self):
        self.assertEqual(self.samu.driver.current_url, page_url)

    def test_find_element_valid_with_strategy(self):
        """This test checks that passing a valid strategy and selector works"""
        selector_options = [
            (By.CSS_SELECTOR, '.class-title'),
            (By.XPATH, '//div[@class="class-title"]'),
            (By.CLASS_NAME, 'class-title'),
            (By.ID, 'id-title'),
            (By.LINK_TEXT, 'This is the index link'),
            (By.PARTIAL_LINK_TEXT, 'partial link text'),
            (By.NAME, 'name-title'),
            (By.TAG_NAME, 'h2'),
        ]

        for strategy, selector in selector_options:
            title = self.samu.find_element(selector=selector)
            self.assertTrue(title)
            self.assertTrue(title.is_displayed())

    def test_find_element_invalid_selector(self):
        """This test checks that passing an invalid selector returns None"""
        self.assertFalse(self.samu.find_element(selector='//$/').exists())

    def test_find_element_without_strategy_valid(self):
        selectors = [
            '.class-title',
            '//div[@class="class-title"]',
            'class-title',
            'id-title',
            'This is the index link',
            'partial link text',
            'name-title',
            'h2',
        ]
        for selector in selectors:
            title = self.samu.find_element(selector=selector)
            self.assertTrue(title)
            self.assertTrue(title.is_displayed())

    def test_find_element_non_existent_element(self):
        """Tests passing a selector for a non existent element to find_element"""
        self.assertFalse(self.samu.find_element(selector='invalid_non_existent').exists())

    @data('wait-for-class', '.wait-for-class', '//div[@class="wait-for-class"]',
          'This element shows after 1 second', 'after 1 second')
    def test_wait_for_element_valid_different_combinations(self, selector):
        """Test waiting for an element until is displayed"""
        new_element = self.samu.find_element(selector=selector)
        self.assertTrue(new_element)
        self.assertTrue(new_element.is_displayed(), f'not found with selector "{selector}"')

    def test_element_text(self):
        title = self.samu.find_element(selector='.class-title')
        self.assertEqual(title.text, 'Class Title')

    def test_element_is_present(self):
        title = self.samu.find_element(selector='.class-title')
        self.assertTrue(title.is_present)

        non_existent = self.samu.find_element(selector='.class-title123')
        self.assertFalse(non_existent.is_present)

    def test_element_click(self):
        counter = self.samu.find_element(selector='.counter')
        self.assertEqual(counter.text, '0')
        counter_btn = self.samu.find_element(selector='.counterBtn')
        counter_btn.click()
        counter = self.samu.find_element(selector='.counter')
        self.assertEqual(counter.text, '1')

    def test_wait_for_element_long(self):
        self.samu.navigate(f'{page_url}?wait=1.5')
        new_element = self.samu.find_element(selector='wait-for-class')
        self.assertTrue(new_element)
        self.assertTrue(new_element.is_displayed(), f'not found with selector wait-for-class')

    def test_find_elements(self):
        divs = self.samu.find_elements('//div')
        self.assertTrue(len(divs) > 0)


if __name__ == '__main__':
    unittest.main()
