# -*- coding: utf-8 -*-
from unittest import TestCase
from pyidwm.Config import Config
from pyidwm.helper.Store import Store
from osgeo import ogr


class StoreTest(TestCase):

    def test_constructor(self):
        store = Store()
        self.assertIsInstance(store, Store)

    def test_get_driver(self):
        store = Store()
        driver = store.get_driver()
        self.assertIsInstance(driver, ogr.Driver)

    def test_get_data_source(self):
        store = Store()
        config = Config()
        config.geopackage = __file__ + "/../data/idwm.gpkg"
        data_source = store.get_data_source()
        self.assertIsInstance(data_source, ogr.DataSource)

    def test_get_layer(self):
        store = Store()
        config = Config()
        config.geopackage = __file__ + "/../data/idwm.gpkg"
        layer = store.get_layer("RRCountriesPoly")
        self.assertIsNotNone(layer)
