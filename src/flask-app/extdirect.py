# -*- coding: utf-8 -*-
"""
    flaskext.extdirect
    ~~~~~~~~~~~~~~~~~~

    Adds Ext.Direct support to Flask. Under development.

    :copyright: (c) 2010 by PA Parent.
    :license: MIT, see LICENSE for more details.
"""

import logging
import inspect
import functools
import traceback
from sys import stderr

from flask import request, url_for, Blueprint
import utils

try:
    import json
except ImportError:
    import simplejson as json


class ExtDirectBlueprint(Blueprint):

    """ExtDirectBlueprint

    A blue print for ext direct.  Based on https://github.com/paparent/Flask-ExtDirect
    """

    logger = logging.getLogger("extdirect")

    def __init__(self, name, import_name, direct_name="Ext.app.REMOTING_API", namespace="Ext.app", **kw):
        """ExtDirectBlueprint

        :param name:
        :param import_name:
        :param direct_name:  name of the remoting API JS variable
        :param namespace:    JS namespace to define
        """
        self.logger.debug("ExtDirectBlueprint: name=%s import_name=%s direct_name=%s namespace=%s",
                name, import_name, direct_name, namespace)

        self.direct_name = direct_name
        self.namespace = namespace
        self.defs = {}
        self.registry = {}

        Blueprint.__init__(self, name, import_name, **kw)

    def register(self, app, options, first_registration=False):
        """Called by Flask.register_blueprint() to register a blueprint on the
        application. This can be overridden to customize the register behavior.
        Keyword arguments from register_blueprint() are directly forwarded to
        this method in the options dictionary."""
        self.logger.debug("register: app=%r, options=%r, first_registration=%r", app, options, first_registration)
        urlprefix = options["url_prefix"]
        app.add_url_rule('%s/api.js' % urlprefix, 'directapi', self.api)
        app.add_url_rule('%s/router' % urlprefix, 'directrouter', self.router, methods=['POST'])
        return Blueprint.register(self, app, options, first_registration=first_registration)

    def extdirect(self, klass=None, **kw):
        self.logger.debug("extdirect: klass=%s kw=%r", klass, kw)
        def decorate(func):
            flags = kw
            module = klass

            if module is None:
                module = func.__module__.split('.')[-1]

            funcname = func.__name__

            if module not in self.registry:
                self.registry[module] = {}
            if module not in self.defs:
                self.defs[module] = []

            args = inspect.getargspec(func)[0]
            infos = {'name': funcname, 'len': len(args)}
            infos.update(flags)
            self.defs[module].append(infos)
            self.registry[module][funcname] = func

            self.logger.debug("extdirect deco: defs=%r, regsistry=%r", self.defs, self.registry)
            return func
        return decorate

    def route(self, rule, **options):
        self.logger.debug("route: rule=%s options=%r", rule, options)
        return Blueprint.route(self, rule, **options)


    @utils.returns_js
    def api(self):
        lines = ["Ext.ns('%s');" % self.namespace,
                "%s = %s;" % (self.direct_name,
            json.dumps({'url': url_for('.directrouter'),
                      'type': 'remoting',
                      'actions': self.defs}, indent=4))]
        #lines.append("Ext.direct.Manager.addProvider(%s);" % self.direct_name)
        return "\n".join(lines)

    @utils.returns_json
    def router(self):
        self.logger.debug("router")
        try:
            data = request.form.to_dict()
            data.pop('extAction')
            data.pop('extMethod')
            data.pop('extType')
            data.pop('extUpload')
            data.pop('extTID')
            req = {
                'action': request.form['extAction'],
                'method': request.form['extMethod'],
                'type': request.form['extType'],
                'upload': request.form['extUpload'],
                'tid': request.form['extTID'],
                'data': data,
            }
            self.logger.debug("router: form req=%r" % req)
            return self._request(req)
        except KeyError:
            requests = json.loads(request.data)

            if isinstance(requests, dict):
                requests = [requests]

            responses = []
            for req in requests:
                responses.append(self._request(req))

            if len(responses) == 1:
                responses = responses[0]

            return responses

    def _request(self, req):
        action, method, data, tid = (req['action'], req['method'],
                                     req['data'], req['tid'])
        self.logger.debug("_request: %s.%s [%d] %r", action, method, tid, data)

        func = self.registry[action][method]


        try:
            if isinstance(data, dict):
                result = func(**data)
            elif data:
                result = func(*data)
            else:
                result = func()
        except Exception, ex:
            self.logger.error("_request: exception: %r" % ex)
            traceback.print_exc(file=stderr)
            out = {'type': 'exception',
                    'tid': tid,
                    'message': unicode(ex),
                    'where': traceback.format_exc()}
        out = {'type': 'rpc',
                'tid': tid,
                'action': action,
                'method': method,
                'result': result}

        self.logger.debug("_request: => %r", out)
        return out

# vim: set ft=python ts=4 sw=4 expandtab :
