import pytest


class TestBooksCollector:

    # Проверяем добавление книги с граничными валидными значениями
    @pytest.mark.parametrize('book_name', ['А', 'А' * 40])
    def test_add_new_book_valid_boundary(self, collector, book_name):
        collector.add_new_book(book_name)

        assert book_name in collector.get_books_genre()

    # Проверяем, что книги с невалидной длиной названия не добавляются
    @pytest.mark.parametrize('book_name', ['', 'А' * 41])
    def test_add_new_book_invalid_boundary(self, collector, book_name):
        collector.add_new_book(book_name)

        assert book_name not in collector.get_books_genre()

    # Проверяем установку жанра книги
    def test_set_book_genre(self, collector):
        collector.add_new_book('Гарри Поттер')

        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    # Отдельно проверяем получение жанра книги
    def test_get_book_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    # Проверяем получение книг с определённым жанром
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == [
            'Гарри Поттер'
        ]

    # Проверяем получение словаря книг
    def test_get_books_genre(self, collector):
        collector.add_new_book('Гарри Поттер')

        assert collector.get_books_genre() == {
            'Гарри Поттер': ''
        }

    # Проверяем, что книги с возрастным рейтингом
    # не попадают в список книг для детей
    def test_get_books_for_children(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        collector.add_new_book('Очень страшный фильм')
        collector.set_book_genre('Очень страшный фильм', 'Ужасы')

        assert collector.get_books_for_children() == [
            'Гарри Поттер'
        ]

    # Проверяем добавление книги в избранное
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Гарри Поттер')

        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == [
            'Гарри Поттер'
        ]

    # Проверяем удаление книги из избранного
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        collector.delete_book_from_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == []

    # Проверяем получение списка избранных книг
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Дюна')

        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == [
            'Гарри Поттер',
            'Дюна'
        ]
        