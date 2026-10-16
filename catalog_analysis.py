import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies: list) -> float:
    if not movies:
        return
    total_rating = 0
    for movie in movies:
        total_rating += movie['rating']
    return round(total_rating / len(movies),1)

def catalog_age_stats(movies: list, current_year: int = 2026) -> tuple:
    if not movies:
        return
    ages = []
    for movie in movies:
        ages.append(current_year - movie['year'])
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))

def duration_in_hours(minutes: int) -> str:
    return str(minutes // 60) + 'ч ' + str(minutes % 60) + 'м'

def rating_tier(rating: float) -> str:
    if rating >= 9:
        category = 'шедевр'
    elif rating >= 7:
        category = 'хорошо'
    else:
        category = 'средне' if rating >= 5 else 'слабо'
    return category

def decade_label(year: int) -> str:
    match year:
        case _ if 2020 < year:
            label = 'новые'
        case _ if 2015 <= year <= 2020:
            label = 'недавние'
        case _ if year < 2015:
            label = 'старые'
    return label

# В условии не сказано, что следующие блоки нужно оформлять в функции.
# Закоментировать их, что бы не оставлять открытый код, так как по условию
# дожна быть одна точка входа build_report(movies).
# Далее есть еще 2 таких блока

# for movie in movies:
#     if 'comedy' in movie['genres']:
#         continue
#     print(movie['title'])

# i = 0
# while i < len(movies):
#     if movies[i]['rating'] > 9:
#         print(movies[i]['title'])
#         break
#     i += 1
# else:
#     print('Шедевров не найдено')

def count_long_movies(movies: list, threshold: int = 120) -> int:
    if not movies:
        return
    count = 0
    for movie in movies:
        count += int(movie['duration_min']) > threshold
    return count

def normalize_title(title: str) ->str:
    new_title = ''
    words = title.split()
    for word in words:
        new_title += word[0].upper() + word[1:] + ' '
    return new_title.strip()

def make_slug(title: str) ->str:
    return title.lower().replace(' ','-')

def format_report_line(movie: dict) -> str:
    if not movie:
        return
    return (f'"{normalize_title(movie['title'])}" ({movie['year']}) - ' +
            f'{movie['rating']}/10, {duration_in_hours(movie['duration_min'])}, ' + 
            f'жанры: {', '.join(sorted(movie['genres']))}'
    )

def titles_sorted_by_rating(movies: list) -> list:
    if not movies:
            return
    return (sorted([(normalize_title(movie['title']), movie['rating'])
            for movie in movies], key=lambda x: x[1], reverse=True)
    )

def top_n_by_rating(movies: list, n: int = 3) -> list:
    return titles_sorted_by_rating(movies)[:n]

def count_by_genre(movies: list) -> dict:
    if not movies:
        return
    count_by_genres = {}
    for movie in movies:
        for genre in movie['genres']:
            count_by_genres[genre] = count_by_genres.get(genre, 0) + 1
    return count_by_genres

def actor_filmography(movies: list) -> dict:
    if not movies:
        return
    actor_movies = {}
    for movie in movies:
        for actor in movie['actors']:
            actor_movies.setdefault(actor, []).append(normalize_title(movie['title']))
    return actor_movies

# movie_top_half = {movie['title']: movie['rating']
#                   for movie in movies if movie['rating'] > average_rating(movies)}
# print(movie_top_half
    
def all_genres(movies: list) -> set:
    if not movies:
        return
    genres = set()
    for movie in movies:
        genres = genres | set(movie['genres'])
    return genres

def common_actors(movie1: dict, movie2: dict) -> set:
    if not movie1 or not movie2:
        return
    return set(movie1['actors']) & set(movie2['actors'])

def genres_only_in_one(movies_a: dict, movies_b: dict) -> set:
    if not movies_a or not movies_b:
        return
    return all_genres(movies_a) - all_genres(movies_b)

def iter_high_rated(movies: list, min_rating: float = 8.0):
    for movie in movies:
        if movie['rating'] > min_rating:
            yield movie

# for movie in iter_high_rated(movies):
#    print(format_report_line(movie))

# print(sum(movie["duration_min"] for movie in movies if movie["rating"] > 7))

def build_report(movies: list) -> None:
    if not movies:
        return
    print('ОТЧЕТ ПО КАТАЛОГУ')
    print(f'Средний рейтинг: {average_rating(movies)}')
    print(f'Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет')
    
    print('\nТоп-3 фильма:')
    # Функция top_n_by_rating() не подходит, поскольку возвразает список из 
    # tuple('title', 'rating') а нам для вывода нужна полная информация о фильме.
    # Сортируем здесь.
    sorted_by_rating = sorted(movies,
                              key=lambda movie: movie["rating"],
                              reverse=True)[:3]
    for movie in sorted_by_rating:
        print(format_report_line(movie))

    print('\nФильмов по жанрам:')
    sorted_count_by_gendre = sorted(count_by_genre(movies).items(),
                                    key=lambda item: item[1],
                                    reverse=True)
    for genre in sorted_count_by_gendre:
        print(f'{genre[0]} - {genre[1]}')
    
    print(f'\nВсе жанры каталога: {', '.join(all_genres(movies))}')

if __name__ == "__main__":
     build_report(movies)
