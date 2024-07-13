"""
https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%D1%8B_%D0%B4%D0%B5_%D0%9C%D0%BE%D1%80%D0%B3%D0%B0%D0%BD%D0%B0

Отрицание конъюнкции равно дизъюнкции отрицания
not (A and B) == not A or not B

Отрицание дизъюнкции равно конъюнкции отрицания
not (A or B) == not A and not B

Ещё одна полезная ссылка для доказательства законов де Моргана - логика высказываний:
https://ru.wikipedia.org/wiki/%D0%9B%D0%BE%D0%B3%D0%B8%D0%BA%D0%B0_%D0%B2%D1%8B%D1%81%D0%BA%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%BD%D0%B8%D0%B9

в частности, законы дистрибутивности:
    p ∧ ( q ∨ r )  ↔  ( p ∧ q ) ∨ ( p ∧ r )
    p ∨ ( q ∧ r )  ↔  ( p ∨ q ) ∧ ( p ∨ r )

или
   A ∨ ( B ∧ C )  ↔  ( A ∨ B ) ∧ ( A ∨ C )
   A ∨ ( B ∧ C )  ↔  ( A ∨ B ) ∧ ( A ∨ C )
"""

A = False
B = True

first_1 = not (A and B)
second_1 = not A or not B
print(first_1 == second_1)

first_2 = not (A or B)
second_2 = not A and not B
print(first_2 == second_2)
