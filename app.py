# lib/app.py
print("Hello world!", end=" ")
print("Hello sun!", end="!! ")
print("Hello sky!", end="!!!\n")

def test_app_py_exists():
    assert(path.exists("lib/app.py"))