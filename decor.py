from datetime import datetime

def decor(path):
    def _decor(old_function):
        def new_function(*args, **kwargs):
            current_date = datetime.now().date()
            current_time = datetime.now().time()
            result = old_function(*args, **kwargs)

            with open(f'{path}', 'a', encoding='utf-8') as f:
                f.writelines(f'{current_date}, {current_time}, {old_function.__name__}, {args}, {kwargs}, {result} \n')
            return result
        return new_function
    return _decor



