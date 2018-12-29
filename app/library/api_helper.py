from flask import Response, jsonify, request
import json
import datetime

STATUS_TRANSACTION = {
    1 : 'Transaksi baru',
    2 : 'Transaksi siap kirim',
    3 : 'Terkirim',
    4 : 'Gagal'
}

MESSAGE_ERROR = {
    200: 'OK',
    400: 'Bad Request.',
    403: 'Forbidden.',
    404: 'Page not found.',
    405: 'Method not allowed.',
    410: 'Unauthorized.',
    500: 'Internal Server Error.',
    1001: 'Error DB Connection.',
    1002: 'Invalid Query.',
    1003: 'Under Maintenance.',
    1004: 'Token Mismatch.',
    1005: 'Not Authorized.',
    1006: 'Invalid Parameter.',
    1007: 'Failed CRUD to Database.',
    1008: 'Bad Syntax.',
    1009: 'Unknown Error.',
    1010: 'Perhatian Data tidak ditemukan.',
    1011: 'Login failed.',
    1012: 'Upload data failed.',
    1013: 'Failed Sync Data.',
    1014: 'Terdapat step yang belum di konfirmasi.'
}

def my_converter(value):
    """
    my_converter : Convert datetime
    """

    if isinstance(value, datetime.datetime):
        return value.__str__()

def json_load(data):
    try:
        return json.loads(data)
    except ValueError as error:
        return None

def check_request():
    try:
        return True if bool(request.data) else False
    except Exception as error:
        return False

def request_values():
    try:
        return request.values
    except Exception as error:
        return None

def request_get(key, defaultValue=None):
    try:
        return request.args.get(key, defaultValue)
    except Exception as error:
        return None

def request_files(field):
    try:
        return request.files.getlist(field)
    except Exception as error:
        return None

def request_header(field):
    try:
        return request.headers.get(field)
    except Exception as error:
        return None

def json_dump(data):
    try:
        return json.dumps(data)
    except ValueError as error:
        return None

def response(status, data=''):
    """
    Function to get response API
    """

    result = {'code': status}
    result['status'] = MESSAGE_ERROR[status]
    result['message'] = data

    result = dict_to_json(result)
    res = Response(result, status=200, mimetype='application/json')
    res.headers['X-Robots-Tag'] = 'noindex, nofollow, noarchive, noodp, noydir, noarchive, nosnippet'
    return res

def responseEditable(status, data=''):
    """
    Function to get response API
    """

    result = {'code': status}
    result['status'] = MESSAGE_ERROR[status]
    if isinstance(data, str):
        result['message'] = data
    else:
        result['message'] = data['message']
        result['kupid'] = data['kupid']
        result['gtin'] = data['gtin']
        
    result = dict_to_json(result)
    res = Response(result, status=200, mimetype='application/json')
    res.headers['X-Robots-Tag'] = 'noindex, nofollow, noarchive, noodp, noydir, noarchive, nosnippet'
    return res

def dict_to_json(detail_log):
    """ my_converter """
    return json.dumps(detail_log, sort_keys=True, default=my_converter)
