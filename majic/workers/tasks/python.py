
from majic.templates import task

@task('PythonTask')
def PythonTask(func, *args, **kwargs):
    return func(*args, **kwargs)
