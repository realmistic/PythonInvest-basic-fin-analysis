# retry func() call for n times (default is 5)
def retry(func, times=5):
    for _ in range(times):
        try:
            return func()
        except Exception as e:
            print(e)
            continue
