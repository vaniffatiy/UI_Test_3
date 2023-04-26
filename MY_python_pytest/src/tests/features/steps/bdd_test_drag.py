from behave import *
from UI_test.UI_Test_3.MY_python_pytest.src.pages.drag_page import DragPage


@given(u'we have the website opened')
def step_impl(context, webdriver_handler):
    drag = DragPage(webdriver_handler)
    drag.open_site()


@when(u'we activate "drag and drop" function both end_to_end and by offset')
def step_impl(context, webdriver_handler):
    drag = DragPage(webdriver_handler)
    drag.drag_drop()
    drag.drag_drop_offset()


@then(u'we confirm that the functions work well')
def step_impl(context, webdriver_handler):
    drag = DragPage(webdriver_handler)
    assert drag.drag_drop() is True
    assert drag.drag_drop_offset() is True
    assert context.failed is False
