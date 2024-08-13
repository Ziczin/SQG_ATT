class Log:
    is_log = False
    def __call__(self, *args, **kwds) -> None:
        if self.is_log:
            print(*args, **kwds)