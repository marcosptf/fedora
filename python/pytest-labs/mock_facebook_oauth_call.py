#!/usr/bin/env python2
#encoding: UTF-8
#import mock
#import facebook
#
#class SimpleFacebook(object):
#    
#    def __init__(self, oauth_token):
#        self.graph = facebook.GraphAPI(oauth_token)
#
#    def post_message(self, message):
#        """Posts a message to the Facebook wall."""
#        self.graph.put_object("me", "feed", message=message)
#        
#
#@mock.patch.object(facebook.GraphAPI, 'put_object', autospec=True)
#def test_post_message(mock_put_object):
#    sf = simple_facebook.SimpleFacebook("fake oauth token")
#    sf.post_message("Hello World!")
#
#    # verify
#    mock_put_object.assert_called_with(message="Hello World!")
#
