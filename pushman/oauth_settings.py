# -*- coding: utf-8 -*-


def DJANGO_WE_CFG_FUNC(request, state=None):
    """ WeChat CFG Callback Func """


def DJANGO_WE_BASE_FUNC(code, state, access_info=None):
    """ WeChat Base Redirect Callback Func """


def DJANGO_WE_USERINFO_FUNC(code, state, access_info=None, userinfo=None):
    """ WeChat Userinfo Redirect Callback Func """
    from account.models import UserInfo
    from django.conf import settings
    from utils.redis.connect import r

    # Save profile or something else
    unique_identifier = userinfo.get(settings.WECHAT_UNIQUE_IDENTIFICATION, '')

    user, created = UserInfo.objects.select_for_update().get_or_create(**{settings.WECHAT_UNIQUE_IDENTIFICATION: unique_identifier})
    user.unionid = userinfo.get('unionid', '')
    user.openid = userinfo.get('openid', '')
    user.nickname = userinfo.get('nickname', '')
    user.avatar = userinfo.get('headimgurl', '')
    user.save()

    token_check_key = user.user_id

    return {
        settings.TOKEN_CHECK_KEY: token_check_key,
        'vtoken': r.token(token_check_key, ex=False, buf=False),
    }
