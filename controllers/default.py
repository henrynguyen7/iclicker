# -*- coding: utf-8 -*-

from pyminer import BitcoinRPC, Miner
from gluon import *

def index():
    ip = current.request.client
    return dict(ip=ip)

def info():
    return dict()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

def getblockcount():
    client = BitcoinRPC("127.0.0.1", "8332", "bitcoinrpc", "asdfasdf")
    blockcount = client.getblockcount()
    return dict(blockcount=blockcount)

def submitattempt():
    uniqueId, timestamp = request.vars.uniqueId, request.vars.timestamp
    print uniqueId
    print timestamp
    miner = Miner("miner")
    return dict(nonce="",
                isSuccessfulHash=False)
