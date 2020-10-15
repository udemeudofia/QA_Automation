import time


# noinspection PyProtectedMember
def to_highlight(element, color, border_size, duration=0.5):
    """Highlights a web element"""
    driver = element._parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border_size, color))
    time.sleep(duration)
    apply_style(original_style)
