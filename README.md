# sumo-weekly-movies
An archive of the SUMO weekly movies

## What?
This repository maintains a list of the movies shown by the Student Union Movie Organization at Carleton College, who choose a new movie to show on campus each week.

We began tracking these movies in the fall of the 2017-18 school year.

## Usage
If you want to do things with the raw data, you're free to use `master`.

However, we process the data to do things like extract the dominant color of the movie poster; those processed files are stored on the `gh-pages` branch.

If you're wanting to use the processed data files, here's what you need to know:

- There are two top-level files, `archive.json` and `next.json`. They are more-or-less just pointers to the actual data files.
- Each movie has an `index.json` file that actually contains the data

These `index.json` files look like this:

```json
{
  "root": "https://carls-app.github.io/weekly-movie/movies/2018-03-02%20Coco",
  "info": {
    "Title": "Coco",
    "Year": "2017",
    "Rated": "PG",
    "Released": "21 Nov 2017",
    "Runtime": "105 min",
    "Genre": "Animation, Adventure, Comedy",
    "Director": "Lee Unkrich, Adrian Molina(co-director)",
    "Writer":
      "Lee Unkrich (original story by), Jason Katz (original story by), Matthew Aldrich (original story by), Adrian Molina (original story by), Adrian Molina (screenplay by), Matthew Aldrich (screenplay by)",
    "Actors":
      "Anthony Gonzalez, Gael García Bernal, Benjamin Bratt, Alanna Ubach",
    "Plot":
      "Aspiring musician Miguel, confronted with his family's ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.",
    "Language": "English, Spanish",
    "Country": "USA",
    "Awards": "Nominated for 2 Oscars. Another 55 wins & 39 nominations.",
    "Ratings": [
      { "Source": "Internet Movie Database", "Value": "8.7/10" },
      { "Source": "Rotten Tomatoes", "Value": "97%" },
      { "Source": "Metacritic", "Value": "81/100" }
    ],
    "imdbID": "tt2380307",
    "Type": "movie",
    "DVD": "13 Feb 2018",
    "BoxOffice": "$191,925,612",
    "Production": "Disney/Pixar",
    "Website": "N/A",
    "ReleaseDate": "2017-11-21",
    "Genres": ["Animation", "Adventure", "Comedy"]
  },
  "showings": [
    { "time": "2018-03-02T20:00:00-06:00", "location": "Weitz Cinema" },
    { "time": "2018-03-02T23:00:00-06:00", "location": "Weitz Cinema" },
    { "time": "2018-03-03T20:00:00-06:00", "location": "Weitz Cinema" },
    { "time": "2018-03-03T23:00:00-06:00", "location": "Weitz Cinema" }
  ],
  "poster": {
    "sizes": [
      {
        "url":
          "https://carls-app.github.io/weekly-movie/movies/2018-03-02%20Coco/poster/96.jpg",
        "filename": "poster/96.jpg",
        "width": 96,
        "height": 137
      },
      {
        "url":
          "https://carls-app.github.io/weekly-movie/movies/2018-03-02%20Coco/poster/192.jpg",
        "filename": "poster/192.jpg",
        "width": 192,
        "height": 274
      },
      {
        "url":
          "https://carls-app.github.io/weekly-movie/movies/2018-03-02%20Coco/poster/300.jpg",
        "filename": "poster/300.jpg",
        "width": 300,
        "height": 429
      },
      {
        "url":
          "https://carls-app.github.io/weekly-movie/movies/2018-03-02%20Coco/poster/512.jpg",
        "filename": "poster/512.jpg",
        "width": 512,
        "height": 732
      },
      {
        "url":
          "https://carls-app.github.io/weekly-movie/movies/2018-03-02%20Coco/poster/768.jpg",
        "filename": "poster/768.jpg",
        "width": 768,
        "height": 1097
      },
      {
        "url":
          "https://carls-app.github.io/weekly-movie/movies/2018-03-02%20Coco/poster/1024.jpg",
        "filename": "poster/1024.jpg",
        "width": 1024,
        "height": 1463
      }
    ],
    "colors": {
      "dominant": [218, 113, 51],
      "palette": [
        [44, 34, 106],
        [225, 118, 49],
        [144, 117, 178],
        [113, 77, 107],
        [225, 202, 151],
        [125, 28, 54]
      ]
    }
  },
  "trailers": [
    {
      "name": "Official US Teaser Trailer",
      "type": "Teaser",
      "url": "https://www.youtube.com/watch?v=zNCz4mQzfEI",
      "lang": "en-US",
      "thumbnails": [
        {
          "url":
            "https://carls-app.github.io/weekly-movie/movies/2018-03-02%20Coco/trailers/zNCz4mQzfEI/small.jpg",
          "filename": "trailers/zNCz4mQzfEI/small.jpg",
          "width": 120,
          "height": 67
        },
        // ...
      ]
    },
    // ...
  ]
}
```

A few things to note:

- Inside the `posters` object, you get a selection of poster sizes, as well as a mapping of the poster colors
- Similarly, each trailer comes with a selection of thumbnails and the dominant colors of that trailer

## Contibuting
To add a new movie:

1. Get an OMDB API key: http://www.omdbapi.com/apikey.aspx
2. Take the key they email you, and export it: `export OMDB_API_KEY="my-key"`
    - I recommend putting this in your shell's config file (`~/.bashrc`, `~/.config/fish/config.fish`, etc)
3. Install Pipenv, if you don't have it already: https://docs.pipenv.org
4. Install our dependencies: `pipenv install`
5. Download the movie info: `./bin/add-movie YYYY-MM-DD MovieName`
    - `YYYY-MM-DD` is the date that the movie will be shown
    - `MovieName` is the name of the movie
    - The script will ask you to pick the correct movie
6. Make sure the "showings" are correct (in `showings.json`) – sometimes SUMO shows movies on odd days/times
7. Commit and PR!

---

If you need to check that your files are workable, you can run

```bash
pipenv run bin/build.py
```
