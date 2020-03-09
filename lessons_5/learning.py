

################# Part 2 list comper

# import time
#
# result_lsit = []
# start_lopp = time.time()
# for i in range(100):
#     result_lsit.append(i)
#
# print(time.time() - start_lopp)
#
# start_lopp_2 = time.time()
# result_lsit_2 = [i for i in range(100) if not i % 2]
# print(time.time() - start_lopp_2)
#
# set_compr = {i if not i % 2 else i ** 2 for i in range(1000000)}
#
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
#
# set_dict_compr = {k: v for k, v in zip(a, b)}
# print(set_dict_compr)
#
# set_dict_compr_2 = {k: v for k, v in enumerate(a)}
# print(set_dict_compr_2)

################# Part 1
# class FacebookAuth:
#     api_url = 'facebook.com/'
#
#     def __init__(self, login, password):
#         self._login = login
#         self._password = password
#
#     def __call__(self, *args, **kwargs):
#         print('Object has been called')
#
#     @staticmethod
#     def validate(login, password):
#         print(login, password)
#
#
# fb = FacebookAuth('asd', 'asdsd')
# fb()
#
# FacebookAuth.validate('igor', 'asldkasldksd')
#
#
# class Dec:
#     def __init__(self, funk):
#         self._f = funk
#
#     def __call__(self, *args, **kwargs):
#         print(f'Wrapping function {self._f.__name__}')
#         self._f()
#
#
# @Dec
# def test():
#     print('hello')
#
#
# test()
