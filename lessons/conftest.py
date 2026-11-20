"""lessons 下所有测试共享的 pytest 配置。

练习函数里仍是 `raise NotImplementedError` 时，把对应测试标记为 SKIPPED（未完成），
而不是 FAILED，这样“还没做”和“做错了”可以一眼区分。其他异常照常报告为失败。
"""

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if call.when == "call" and call.excinfo is not None and call.excinfo.errisinstance(NotImplementedError):
        report.outcome = "skipped"
        line = (item.location[1] or 0) + 1
        report.longrepr = (str(item.path), line, "未完成：练习函数中仍是 raise NotImplementedError")
