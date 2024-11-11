summary = """Здравствуйте, пакет \"calculate\" инициализирован!

Вы можете импортировать или использовать функцию \"evaluate\" с аргументами:

1) Первый операнд с необходимым типом int или float
2) Второй операнд с необходимым типом int или float
3) Знак для вычисления (необходимо написать число):
\t `+` - 1
\t `-` - 2
\t `*` - 3
\t `/` - 4"""

print(summary)

__all__ = ['evaluate']

from calculate.calc import evaluate