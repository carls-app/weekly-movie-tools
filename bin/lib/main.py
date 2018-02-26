import json
from datetime import timedelta
from pathlib import Path
from .trailers import get_trailers, download_trailer
from .posters import download_posters
from .movies import search_for_movie


def get_movie(*, title, year, date, known_showings=[], autopick=False, movie_base):
    movie = search_for_movie(title, year, autopick=autopick)
    if not movie:
        return

    trailers = list(get_trailers(movie['imdbID']))

    movie_dest_dirname = movie["Title"].replace('/', ':')
    date_str = date.isoformat() if 'isoformat' in date else date
    movie_base = movie_base if movie_base else Path(__file__).parent.parent.parent / 'movies'
    movie_dir = movie_base / f'{date_str} {movie_dest_dirname}'
    movie_dir.mkdir(parents=True, exist_ok=True)

    movie_file = movie_dir / 'movie.json'
    with open(movie_file, 'w', encoding='utf-8') as outfile:
        json.dump(movie, outfile, ensure_ascii=False, indent=2)
        outfile.write('\n')

    download_posters(movie, movie_dir)

    trailers_file = movie_dir / 'trailers.json'
    with open(trailers_file, 'w', encoding='utf-8') as outfile:
        json.dump({'trailers': trailers}, outfile, ensure_ascii=False, indent=2)
        outfile.write('\n')

    for trailer in trailers:
        download_trailer(trailer, movie_dir / 'trailers')

    showings_file = movie_dir / 'showings.json'
    with open(showings_file, 'w', encoding='utf-8') as outfile:
        if known_showings:
            showings = known_showings
        else:
            showings = {
                'showings': [
                    {
                        'date': date.isoformat(),
                        'times': ['17:00', '19:30', '22:00'],
                        'location': 'Viking Theater',
                    },
                    {
                        'date': (date + timedelta(days=1)).isoformat(),
                        'times': ['17:00', '19:30', '22:00'],
                        'location': 'Viking Theater',
                    },
                ]
            }
        json.dump(showings, outfile, ensure_ascii=False, indent=2)
        outfile.write('\n')
