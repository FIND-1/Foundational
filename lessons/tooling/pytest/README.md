# pytest 教程（面向写过 Jest / Vitest 的前端开发者）

> 本教程是工具补充，不属于 source 主线。配套示例：[cart.py](cart.py)（被测代码）和 [test_cart.py](test_cart.py)（测试），建议边读边运行。

## 1. pytest 是什么

pytest 是 Python 事实上的标准测试框架，地位相当于前端的 Jest 或 Vitest。Python 自带的 `unittest` 也能写测试，但需要继承类、调用 `self.assertEqual`，写法繁琐；pytest 只需要写普通函数和普通 `assert`。

## 2. 安装（推荐在仓库根目录 `.venv` 中安装）

```powershell
# 若尚未创建虚拟环境，先执行：
python -m venv .venv

# 使用 .venv 中的 pip 安装开发依赖（不污染全局 Python）：
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest --version
```

- 用 `.\.venv\Scripts\python.exe -m pytest` 而不是全局 `pytest`，可以确保使用项目隔离的虚拟环境（类似前端每个项目独立的 `node_modules`）。
- 第 1 章只需掌握**安装、运行**以及输出中的 **`PASSED` / `FAILED` / `SKIPPED`** 三种状态；下文第 6～11 节的 `fixture`、装饰器、hook 等属于进阶内容，暂不需要提前掌握。

## 3. 第一个测试

pytest 会按命名约定自动发现测试，不需要额外注册：

| 对象 | 规则 |
| --- | --- |
| 文件 | `test_*.py` 或 `*_test.py` |
| 函数 | 以 `test` 开头 |
| 类（可选） | 以 `Test` 开头，且没有 `__init__` |

```python
# test_cart.py
from cart import add_item

def test_add_item_to_empty_cart():
    cart = add_item({}, "apple", 3.5)
    assert cart == {"apple": {"price": 3.5, "quantity": 1}}
```

和 Jest 对比：没有 `describe` / `it` / `expect`，一个函数就是一个测试，`assert 表达式` 就是断言。

运行：

```powershell
.\.venv\Scripts\python.exe -m pytest lessons/tooling/pytest          # 运行一个目录
.\.venv\Scripts\python.exe -m pytest                                 # 运行全部（本项目的 pytest.ini 已限定在 lessons 下）
```

## 4. 读懂输出

```text
lessons/tooling/pytest/test_cart.py ..........s.x                     [100%]
```

| 符号 | 含义 |
| --- | --- |
| `.` | 通过 |
| `F` | 失败（断言不成立，或测试中抛出了异常） |
| `E` | 错误（测试之外出错，例如 fixture 出错） |
| `s` | 跳过（skip） |
| `x` | 预期失败（xfail），并且确实失败了 |
| `X` | 预期失败，却通过了（XPASS） |

断言失败时，pytest 会重写 `assert`，把两边的值都展示出来，不需要 `expect(...).toEqual(...)` 也能看到差异：

```text
>       assert cart == {"apple": {"price": 3.5, "quantity": 2}}
E       AssertionError: assert {'apple': {'price': 3.5, 'quantity': 1}} == {'apple': {'price': 3.5, 'quantity': 2}}
E         Differing items:
E         {'apple': {'price': 3.5, 'quantity': 1}} != {'apple': {'price': 3.5, 'quantity': 2}}
```

动手试一下：把 `test_cart.py` 里任意一个期望值改错，运行一次，再改回来。

## 5. 常用命令行参数

| 参数 | 作用 | Jest 对应 |
| --- | --- | --- |
| `-v` | 每个测试单独显示一行 | `--verbose` |
| `-q` | 精简输出 | `--silent`（近似） |
| `-x` | 遇到第一个失败就停止 | `--bail` |
| `-k 表达式` | 按名称筛选，如 `-k "discount and not invalid"` | `-t` |
| `文件::函数` | 只运行某个测试，如 `test_cart.py::test_total_with_float` | `-t` + 文件路径 |
| `--lf` | 只重跑上次失败的测试 | `--onlyFailures` |
| `-s` | 不捕获输出，直接显示测试中的 `print` | `console.log` 默认就会显示 |
| `-ra` | 结尾汇总所有非通过项的原因（本项目 `pytest.ini` 已默认开启） | |
| `--pdb` | 失败时进入调试器 | `node --inspect` |

## 6. 断言异常：`pytest.raises`

```python
def test_negative_price_raises():
    with pytest.raises(ValueError, match="价格不能为负数"):
        add_item({}, "apple", -1)
```

- `with` 代码块中必须抛出指定类型的异常，否则测试失败。Jest 写法是 `expect(() => fn()).toThrow(...)`。
- `match` 是正则表达式，用于匹配异常信息。
- 需要检查异常对象时写 `with pytest.raises(ValueError) as exc_info:`，之后用 `exc_info.value` 取得异常。

## 7. 浮点数：`pytest.approx`

```python
assert total(cart) == pytest.approx(0.3)   # 相当于 Jest 的 toBeCloseTo
```

## 8. 参数化：`@pytest.mark.parametrize`

同一段逻辑需要验证多组数据时使用，相当于 Jest 的 `test.each`：

```python
@pytest.mark.parametrize(
    ("amount", "percent", "expected"),
    [(100, 0, 100), (100, 20, 80), (100, 100, 0)],
    ids=["不打折", "八折", "免费"],
)
def test_apply_discount(amount, percent, expected):
    assert apply_discount(amount, percent) == pytest.approx(expected)
```

- 第一个参数是参数名，第二个参数是数据列表；每组数据都会生成一个独立的测试。
- `@` 是装饰器语法，作用是给函数附加行为或标记（与 JS 装饰器提案的概念类似）。

## 9. fixture：准备和清理

fixture 用来准备测试需要的数据或环境，作用相当于 `beforeEach` / `afterEach`，但它是**按需注入**的：测试函数的参数名和哪个 fixture 同名，pytest 就把那个 fixture 的结果传进来。

```python
@pytest.fixture
def fruit_cart():
    cart = {}
    add_item(cart, "apple", 3.5, quantity=2)
    return cart

def test_total_with_fixture(fruit_cart):     # 参数名 = fixture 名
    assert total(fruit_cart) == 7.0
```

- **隔离**：默认每个测试都会重新执行 fixture，测试之间互不影响。
- **清理**：用 `yield` 代替 `return`，`yield` 之后的代码会在测试结束后执行：

  ```python
  @pytest.fixture
  def cart_file(tmp_path):
      path = tmp_path / "cart.json"
      yield path          # 准备阶段到此结束，把 path 交给测试
      path.unlink()       # 测试结束后执行清理
  ```

- **组合**：fixture 可以依赖其他 fixture（上例依赖了内置的 `tmp_path`）。
- 【了解】作用域：`@pytest.fixture(scope="module")` 表示整个文件只执行一次，相当于 `beforeAll`。
- **共享**：写在 `conftest.py` 里的 fixture，同目录及子目录的所有测试文件都能直接使用，不需要 import。

### 常用内置 fixture

| fixture | 作用 | 示例 |
| --- | --- | --- |
| `capsys` | 捕获 `print` 的输出 | `capsys.readouterr().out == "hello"` |
| `tmp_path` | 每个测试独享的临时目录（`pathlib.Path`），会自动清理 | `tmp_path / "a.json"` |
| `monkeypatch` | 临时替换函数、属性、环境变量，测试结束后自动恢复，相当于 `jest.spyOn` / `vi.stubEnv` | `monkeypatch.setattr("builtins.input", lambda prompt="": "42")` |

## 10. 标记：skip、skipif、xfail

```python
@pytest.mark.skip(reason="暂不运行")                                      # 无条件跳过，相当于 test.skip
@pytest.mark.skipif(sys.platform != "win32", reason="只在 Windows 上运行")  # 按条件跳过
@pytest.mark.xfail(reason="已知 bug", strict=True)                         # 预期失败；strict=True 时如果意外通过，反而算失败
```

## 11. 本项目的配置

| 文件 | 作用 |
| --- | --- |
| `pytest.ini` | 限定只在 `lessons` 下查找测试，并默认开启 `-ra` |
| `lessons/conftest.py` | 配套练习文件仍抛出模板的 `NotImplementedError("练习待完成")` 时，把测试显示为 **SKIPPED（未完成）**，而不是 FAILED |
| `requirements-dev.txt` | 开发依赖（pytest） |

`conftest.py` 是 pytest 的特殊文件：会被自动加载，用来放共享的 fixture 和钩子（hook）。本项目的钩子在每个测试执行后检查异常类型、专用消息和实际抛出异常的文件，属于进阶用法，能看懂意图即可。

## 12. 做练习的流程

以第 1 章为例（只测基础题加 `-m basic`，全部运行则去掉 `-m basic`）：

```powershell
.\.venv\Scripts\python.exe -m pytest lessons/01-basic-syntax -m basic -v
.\.venv\Scripts\python.exe -m pytest lessons/01-basic-syntax -v
```

1. 第一次运行，未完成的练习都会显示 `SKIPPED ... 未完成`。
2. 在 `exercises_01.py` 中完成基础练习（写表达式并完成输入输出），再运行 `-m basic -v`。
3. 对应的测试变成 `PASSED`，说明完成；显示 `FAILED` 时，阅读断言差异并修改。
4. 进阶练习（写函数）为可选；若暂未学函数语法，它们会保持 `SKIPPED`，不影响基础验收。
5. 全部完成并理解后，把收获与错题复盘写进 `notes.md`。

## 13. VS Code 集成

1. 安装 Python 扩展（ms-python.python）。
2. 打开命令面板，执行 `Python: Configure Tests`，选择 **pytest**，根目录选 `.`。
3. 左侧的「测试」面板会列出所有测试，可以单独运行或调试；测试函数旁边也会出现运行按钮。

## 14. Jest 与 pytest 对照

| Jest / Vitest | pytest |
| --- | --- |
| `test("x", () => {...})` | `def test_x(): ...` |
| `describe` | 文件本身，或 `class TestXxx:` |
| `expect(a).toBe(b)` / `toEqual(b)` | `assert a == b` |
| `expect(a).toBeTruthy()` | `assert a` |
| `expect(fn).toThrow(Err)` | `with pytest.raises(Err):` |
| `toBeCloseTo` | `pytest.approx` |
| `test.each` | `@pytest.mark.parametrize` |
| `beforeEach` / `afterEach` | `@pytest.fixture` + `yield` |
| `beforeAll` | `@pytest.fixture(scope="module")` |
| `jest.spyOn` / `vi.mock` | `monkeypatch`（复杂场景用 `unittest.mock`） |
| `test.skip` / `test.todo` | `@pytest.mark.skip` / `@pytest.mark.xfail` |
| `jest.config.js` | `pytest.ini` / `pyproject.toml` |
| `setupFilesAfterEach` 中的共享逻辑 | `conftest.py` |

## 15. 常见问题

| 现象 | 原因与解决 |
| --- | --- |
| `No module named pytest` | 没有安装，或安装到了另一个 Python 中。从仓库根目录用 `.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt` 安装 |
| 测试没有被收集（`collected 0 items`） | 文件名或函数名不符合 `test_` 命名约定 |
| `import file mismatch` | 不同目录中有同名的测试文件或模块。本项目用章节号命名（如 `exercises_01.py`）来避免 |
| `ModuleNotFoundError: No module named 'exercises_01'` | 没有从项目根目录运行，或文件被改名了 |
| 测试里的 `print` 没有显示 | pytest 默认捕获输出，加 `-s` 参数即可显示 |
| 安装 pytest 时报 `Missing dependencies for SOCKS support` | 系统配置了 SOCKS 代理，pip 缺少相应支持。可以关闭代理后再安装，或先安装 `pysocks`（需要能联网） |
