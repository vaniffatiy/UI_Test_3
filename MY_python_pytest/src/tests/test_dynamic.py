from UI_test.UI_Test_3.MY_python_pytest.src.pages.dynamic_home import DynamicHome


class TestDynamic(DynamicHome):
    def test_dynamic_id(self):
        self.open_site()
        id_before = id(self.get_element())
        self.refresh()
        id_after = id(self.get_element())
        assert id_before != id_after, f"{id_after} is not {id_before}"







