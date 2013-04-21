#!/usr/bin/env python

from twython import Twython

t = Twython(app_key='',
            app_secret='',
            oauth_token='',
            oauth_token_secret='')

t.updateStatusWithMedia("/home/root/stache/tmp/captured001.jpg")

