class Mute:
    """
    Класс заглушка, когда нужно отключить функциональность какой-либо зависимости.
    """
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return self

    def __getattr__(self, item):
        return self

    def __setattr__(self, key, value):
        return None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None

    def __await__(self, *args, **kwargs):
        yield
