"""
Part 2: the best movie.

    uv run python human_part2.py

Write your rule on the `**My rule:**` line of WRITEUP.md. Print the top 10 movies (id, title,
ratings count, mean rating) under it.
"""

from load_data import load_all


def top10_my_rule(ratings, ratings_df, movies, movies_df):
    print("== My rule ==")
    movies_ratings = ratings_df.merge(movies_df, on="movie_id")
    movie_ratings = movies_ratings.groupby("title")["rating"].mean()
    movie_counts = movies_ratings.groupby("title").size()
    
    movie_ratings = movie_ratings[movie_counts >= 40]
    
    top_10 = movie_ratings.sort_values(ascending=False).head(10)
    
    print(top_10)
    print(movie_counts[top_10.index])

def human_part2(ratings, ratings_df, movies, movies_df):
    top10_my_rule(ratings, ratings_df, movies, movies_df)


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part2(ratings, ratings_df, movies, movies_df)
