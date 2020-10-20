"""
This module helps in setting pre-defined methods/functions
that are necessary in running the test files.
"""
import time


# noinspection PyProtectedMember
def to_highlight(element, color, border_size, duration=0.5):
    """Highlights a web element"""
    driver = element._parent  # pylint: disable=W0212

    def apply_style(sty_):
        driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);", element, sty_
        )

    original_style = element.get_attribute("style")
    apply_style("border: {0}px solid {1};".format(border_size, color))
    time.sleep(duration)
    apply_style(original_style)
