"""只把配套练习文件中的显式待完成占位符计为 SKIPPED。"""

from pathlib import Path

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    error = call.excinfo
    if call.when != "call" or error is None or error.type is not NotImplementedError:
        return

    # 同类异常也可能来自测试、库或学习者的实现；只识别模板的专用消息和来源。
    if error.value.args != ("练习待完成",) or not item.path.match("test_exercises_*.py"):
        return
    exercise = item.path.with_name(item.path.name.removeprefix("test_"))
    origin = error.traceback[-1]
    if Path(origin.path) != exercise:
        return

    report = outcome.get_result()
    report.outcome = "skipped"
    report.longrepr = (str(exercise), origin.lineno + 1, "未完成：练习占位符")
