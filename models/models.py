from flask import request
import json


class Model(object):
    ''' A class for modeling data from a Flask application. '''
    def __init__(self, **kwargs):
        self._data = {}
        if kwargs:
            self.setData(kwargs=kwargs)

    def setData(self, from_request=False, **kwargs):
        ''':param from_request: specifies whether keys in kwargs are retrieved directly from an HTML form. Default is False.
           :param kwargs: if from_request is True, then keys are mapped directly to values from HTML form inputs; given the input element's name.'''
        if from_request:
            self._data = { k: request.form.get(v) for k, v in kwargs.items() }
        else:
            self._data = { k: v for k, v in kwargs.items() if not isinstance(v, dict) }

    def keys(self):
        for k in self._data.items(): yield k

    def values(self):
        for v in self._data.values(): yield v

    def __call__(self):
        ''':returns key value pair of data in this model.  '''
        for k, v in self._data.items(): yield k, v

    def __str__(self):
        ''' :returns a json representation of the data in this model. '''
        return json.dumps(self._data, indent=3)
