from django.http import JsonResponse


class Response(object):
    """ 通用code码 10000 ~ 10999 """
    code_10000 = "SUCCESS"
    code_10001 = 'REQUEST DATA INVALID'
    code_10002 = 'REQUEST DATA MISSED'
    code_10003 = 'TYPE_NOT_MATCH'
    code_10004 = 'EQUALS'
    code_10005 = 'NOT_BETWEEN'
    code_10006 = 'STR_NOT_CONTAINS'
    code_10007 = 'STR_TOO_LONG'

    def __init__(self, code=None, msg=None, data=None):
        self.code = code
        self.msg = msg
        self.data = data

        if self.msg is None:

            attr = 'code_{code}'.format(code=self.code)

            if hasattr(self, attr):
                self.msg = self.__getattribute__(attr)

    @property
    def json(self):
        response = {"code": self.code, "message": self.msg, "data": self.data}
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
