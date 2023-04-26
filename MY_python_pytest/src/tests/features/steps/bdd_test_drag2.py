from behave import *
from UI_test.UI_Test_3.MY_python_pytest.src.pages.drag_page import DragPage


@given(u'we have the website opened')
def step_impl(context, webdriver_handler):
    drag = DragPage(webdriver_handler)
    drag.open_site()


@then(u'we activate "drag and drop" function both source_to_target and by offset')
def step_impl(context, webdriver_handler):
    drag = DragPage(webdriver_handler)
    drag.drag_drop()
    drag.drag_drop_offset()



