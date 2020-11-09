# IMDB Clone

## DataFormat Used For Movies:
- title
- language
- year
- genres
- writers
- directors
- runtime_minutes
- votes



## Endpoints:
- 'token': 
  - METHODS: `POST` with `username` and `password`
- 'actors': 
  - METHODS: `GET` and `POST` with `name`
- 'directors': 
  - METHODS: `GET` and `POST` with `name`
- 'writers': 
  - METHODS: `GET` and `POST` with `name`
- 'genres': 
  - METHODS: `GET` and `POST` with `name`
- 'create/user': 
  - METHODS: `GET` and `POST` with `name`
- 'create/staff': 
  - METHODS: `GET` and `POST` with `name`


### `movie/`
- GET: List all the movies.
- POST: Create a particular movie.
  - Parameters: Use `DataFormat Used For Movies`.
  - > NOTE: You need to provide the id of actor, writer, genre, writers to add multiple.

### `movie/<int:movie-id>`
- GET: Return particular movie.
- PUT: Update a particular movie.
- DELETE: Delete a particular movie.