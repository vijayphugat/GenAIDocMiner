from time import time
from datetime import timedelta


def calc_exec_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        # ts = {time() - start}
        td = str(timedelta(seconds=time() - start))
        print(f"func : {func.__name__} || execution time : {td} sec")

        return result

    return wrapper


def function_logger_service(func):
    def wrapper(*args, **kwargs):
        print("{} func : {} : start {}".format("#" * 40, func.__name__, "#" * 40))
        start = time()

        result = func(*args, **kwargs)

        td = str(timedelta(seconds=time() - start))
        print(f"\nexecution time : {td} sec")
        print("{} func : {} : end {}".format("#" * 50, func.__name__, "#" * 50))

        return result

    return wrapper


def function_logger_prim(func):
    def wrapper(*args, **kwargs):
        print("{} func : {} : start {}".format("=" * 40, func.__name__, "=" * 40))
        start = time()

        result = func(*args, **kwargs)

        td = str(timedelta(seconds=time() - start))
        print(f"\nexecution time : {td} sec")
        print("{} func : {} : end {}".format("=" * 40, func.__name__, "=" * 40))

        return result

    return wrapper


def function_logger_sec(func):
    def wrapper(*args, **kwargs):
        print("{} func : {} : start {}".format("_" * 40, func.__name__, "_" * 40))
        start = time()

        result = func(*args, **kwargs)

        td = str(timedelta(seconds=time() - start))
        print(f"\nexecution time : {td} sec")
        print("{} func : {} : end {}".format("_" * 40, func.__name__, "_" * 40))

        return result

    return wrapper


def parse_db_record_to_json(list_records):
    list_records_fmt = [row._mapping for row in list_records]
    return list_records_fmt
