from pathlib import Path


def test_plugin(pytester):
    pytester.syspathinsert(Path(__file__).parent.parent)
    pytester.copy_example("conftest.py")
    pytester.copy_example("helpers.py")
    pytester.copy_example("test_basic.py")
    pytester.runpytest()
