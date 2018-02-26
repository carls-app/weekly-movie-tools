#!/usr/bin/env python3

import argparse
import arrow
import feedparser
from pathlib import Path
from collections import defaultdict
from urllib.parse import parse_qs, urlparse
from lib import get_movie


def parse_feed_item_to_event(item):
    str_date, title = item['title'].split('-', maxsplit=1)
    location, str_time = item['summary'].split(', ', maxsplit=1)
    qs_date = parse_qs(urlparse(item['link']).query)['date'][0]

    title = title.replace('SUMO: ', '')
    str_when = f'{qs_date.strip()} {str_time.strip()} America/Winnipeg'
    when = arrow.get(str_when, 'YYYY-MM-DD H:mm a ZZZ')

    return {
        'title': title.strip(),
        'when': when,
        'location': location.strip(),
    }

def convert_to_events(entries):
    events = [parse_feed_item_to_event(item) for item in entries]

    grouped = defaultdict(list)

    for event in events:
        grouped[event['title']].append({
            'date': event['when'].format('YYYY-MM-DD'),
            'time': event['when'].format('HH:mm'),
            'location': event['location'],
        })

    return [{'title': name, 'showings': showings}
            for name, showings in grouped.items()]

    return grouped


def get_showings(movie):
    grouped = {}
    for event in movie['showings']:
        location = event['location']
        date = event['date']
        event['times'] = []

        if location not in grouped:
            grouped[location] = {}

        if date not in grouped[location]:
            grouped[location][date] = event

        grouped[location][date]['times'].append(event['time'])

        del event['time']

    showings = [by_date
                for by_location in grouped.values()
                for by_date in by_location.values()]

    return {'showings': showings}


def main():
    feed = feedparser.parse('https://apps.carleton.edu/student/orgs/sumo/feeds/events')

    known_movies = convert_to_events(feed['entries'])

    if not known_movies:
        print('no movies posted')
        return

    next_movie = known_movies[0]

    showings = get_showings(next_movie)
    date = showings['showings'][0]['date']

    movie_base = Path(__file__).absolute().parent.parent.parent / 'weekly-movie' / 'movies'

    get_movie(title=next_movie['title'], year=None, date=date,
              known_showings=showings, autopick=True,
              movie_base=movie_base)


if __name__ == '__main__':
    main()
