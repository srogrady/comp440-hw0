"""
Part 3: the most ___ movie.

    uv run python human_part3.py

Pick an adjective. Write it on the `**My adjective:**` line of WRITEUP.md and a one-sentence
definition a classmate could code on the `**My definition:**` line. Print the top 5 movies
under it.
"""

from load_data import load_all


def top5_my_definition(ratings, ratings_df, movies, movies_df):
    print("== Niche ==")

    movies_ratings = ratings_df.merge(movies_df, on="movie_id")

    movie_counts = movies_ratings.groupby("title").size()

    niche_movies = movie_counts[movie_counts == 1].head(5)

    print(niche_movies)

def human_part3(ratings, ratings_df, movies, movies_df):
    top5_my_definition(ratings, ratings_df, movies, movies_df)


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part3(ratings, ratings_df, movies, movies_df)
