import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # проверяем добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2
        
    # проверяем, что после добавления у книги нет жанра
    def test_add_new_book_book_without_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')

        assert collector.get_book_genre('Гарри Поттер') == ''

    # проверяем установку жанра книги
    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    # проверяем получение книг с определенным жанром
    @pytest.mark.parametrize(
        'genre, expected',
        [
            ('Фантастика', ['Гарри Поттер', 'Дюна']),
            ('Комедии', ['Маска']),
        ]
    )
    def test_get_books_with_specific_genre(self, genre, expected):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Дюна')
        collector.add_new_book('Маска')

        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Маска', 'Комедии')

        assert collector.get_books_with_specific_genre(genre) == expected

    # проверяем получение словаря книг
    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')

        assert collector.get_books_genre() == {'Гарри Поттер': ''}

    # проверяем, что книги с возрастным рейтингом
    # не попадают в список книг для детей
    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Очень страшный фильм')
        collector.add_new_book('Шрек')

        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Очень страшный фильм', 'Ужасы')
        collector.set_book_genre('Шрек', 'Мультфильмы')

        assert collector.get_books_for_children() == [
            'Гарри Поттер',
            'Шрек'
        ]

    # проверяем добавление книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    # проверяем, что книгу нельзя добавить в избранное дважды
    def test_add_book_in_favorites_add_book_twice(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    # проверяем удаление книги из избранного
    @pytest.mark.parametrize(
        'book',
        ['Гарри Поттер', 'Дюна']
    )
    def test_delete_book_from_favorites(self, book):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Дюна')

        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Дюна')

        collector.delete_book_from_favorites(book)

        assert book not in collector.get_list_of_favorites_books()

    # проверяем получение списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Дюна')

        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == [
            'Гарри Поттер',
            'Дюна'
        ]