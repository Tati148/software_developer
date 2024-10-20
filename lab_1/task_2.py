# TODO Найдите количество книг, которое можно разместить на дискете

disc_vol_b = 1.44 * 1024 * 1024

pages = 100
lines = 50
simbols = 25
one_smbl_b = 4

book_vol_in_b = one_smbl_b * simbols * lines * pages

books_count = round(disc_vol_b // book_vol_in_b)

print("Количество книг, помещающихся на дискету:", books_count)
