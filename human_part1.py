"""
Part 1: basic rating statistics.

    uv run python human_part1.py

Answer the four questions below with your own code, print each answer under its label, and
explain each in one sentence in WRITEUP.md.
"""

from load_data import load_all

def human_part1(ratings, ratings_df, movies, movies_df, users, users_df):

    print("== (a) ==")
    # (a) How many ratings, users, and movies are there, and how are ratings distributed across 1-5 stars?
    
    print(len(ratings_df))
    print(len(users_df))
    print(len(movies_df))

    print(ratings_df.groupby("rating").size())
    
    
    print("== (b) ==")
    # (b) What is the median number of ratings per user, and how many users have 100 or more ratings?
    print(ratings_df.groupby("user_id").size().median())

    print((ratings_df.groupby("user_id").size()>=100).sum())

    print("== (c) ==")
    # (c) Join ratings to titles. Which 10 movies have the most ratings?
    print(ratings_df.merge(movies_df, on ="movie_id").groupby("title").size().sort_values(ascending=False).head(10))

    print("== (d) ==")
    # (d) Among movies with at least 20 ratings, which 10 have the highest mean rating?
    #     Show title, mean, and count.

    movies_ratings = ratings_df.merge(movies_df, on="movie_id")

    movie_ratings = movies_ratings.groupby("title")["rating"].mean()
    movie_counts = movies_ratings.groupby("title").size()

    movie_ratings = movie_ratings[movie_counts >= 20]

    top_10 = movie_ratings.sort_values(ascending=False).head(10)

    print(top_10)
    print(movie_counts[top_10.index])

if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part1(ratings, ratings_df, movies, movies_df, users, users_df)
