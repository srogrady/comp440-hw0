"""
Claude's answers to the three questions in questions.md.

    uv run python claude_answers_1_2_3.py

Filled in by a Claude that has never seen the student's work. Kept as it was written.
"""

from load_data import load_all

MIN_RATINGS = 20  # threshold for "statistically meaningful" mean ratings, used in 1(d), 2, and 3


def question_1(ratings_df, movies_df):
    print("=" * 70)
    print("1(a) Basic counts and rating distribution")
    print("=" * 70)
    n_ratings = len(ratings_df)
    n_users = ratings_df["user_id"].nunique()
    n_movies = ratings_df["movie_id"].nunique()
    print(f"Ratings: {n_ratings:,}")
    print(f"Users:   {n_users:,}")
    print(f"Movies:  {n_movies:,}")
    print()
    print("Rating distribution:")
    counts = ratings_df["rating"].value_counts().sort_index()
    for stars, n in counts.items():
        pct = 100 * n / n_ratings
        print(f"  {stars} stars: {n:>6,}  ({pct:5.1f}%)")

    print()
    print("=" * 70)
    print("1(b) Ratings per user")
    print("=" * 70)
    per_user = ratings_df.groupby("user_id").size()
    print(f"Median ratings per user: {per_user.median():.1f}")
    print(f"Users with >= 100 ratings: {(per_user >= 100).sum():,} "
          f"(out of {n_users:,})")

    print()
    print("=" * 70)
    print("1(c) Top 10 most-rated movies")
    print("=" * 70)
    per_movie = ratings_df.groupby("movie_id").size().rename("count")
    joined = movies_df.set_index("movie_id")[["title"]].join(per_movie)
    top_10_count = joined.sort_values("count", ascending=False).head(10)
    print(top_10_count.reset_index(drop=True).to_string(index=False))

    print()
    print("=" * 70)
    print(f"1(d) Top 10 highest mean rating (movies with >= {MIN_RATINGS} ratings)")
    print("=" * 70)
    stats = ratings_df.groupby("movie_id")["rating"].agg(mean="mean", count="count")
    stats = movies_df.set_index("movie_id")[["title"]].join(stats)
    qualified = stats[stats["count"] >= MIN_RATINGS]
    top_10_mean = qualified.sort_values("mean", ascending=False).head(10)
    print(top_10_mean.reset_index(drop=True).to_string(index=False,
                                                         formatters={"mean": "{:.3f}".format}))
    return stats, qualified


def question_2(qualified):
    print()
    print("=" * 70)
    print("2. What is the best movie in this dataset?")
    print("=" * 70)
    print(f"""A raw top-mean-rating list is dominated by movies with just {MIN_RATINGS} or so
ratings, where a handful of enthusiastic raters can push the average close to 5.0.
To find a "best" movie that isn't an artifact of a small sample, use a Bayesian
("IMDB-style") weighted rating that shrinks each movie's mean toward the overall
mean, by an amount that shrinks as the movie collects more ratings:

    weighted = (v / (v + m)) * R  +  (m / (v + m)) * C

    R = the movie's own mean rating
    v = the movie's number of ratings
    m = a prior strength, set here to the median rating count among qualified movies
    C = the mean rating across all qualified movies
""")
    C = qualified["mean"].mean()
    m = qualified["count"].median()
    qualified = qualified.copy()
    qualified["weighted"] = (qualified["count"] / (qualified["count"] + m)) * qualified["mean"] \
        + (m / (qualified["count"] + m)) * C
    best = qualified.sort_values("weighted", ascending=False).head(10)
    print(f"(prior strength m = {m:.0f} ratings, overall mean C = {C:.3f})\n")
    print(best.reset_index(drop=True).to_string(
        index=False, formatters={"mean": "{:.3f}".format, "weighted": "{:.3f}".format}))
    top = best.iloc[0]
    print(f"\nBest movie: \"{top['title']}\" "
          f"(raw mean {top['mean']:.3f} over {top['count']:.0f} ratings, "
          f"Bayesian-weighted score {top['weighted']:.3f})")


def question_3(qualified):
    print()
    print("=" * 70)
    print("3. Which movie is the most Niche?")
    print("=" * 70)
    print(f"""A niche movie is one that a small audience loves, rather than one that
everybody has seen. That means: high mean rating, but low popularity (few
ratings), relative to other movies. Restricting to movies with >= {MIN_RATINGS}
ratings (so the mean isn't just noise), score each movie by

    niche_score = zscore(mean_rating) - zscore(num_ratings)

i.e. movies that stand out for being *better liked than they are watched*.
""")
    qualified = qualified.copy()
    mean_z = (qualified["mean"] - qualified["mean"].mean()) / qualified["mean"].std()
    count_z = (qualified["count"] - qualified["count"].mean()) / qualified["count"].std()
    qualified["niche_score"] = mean_z - count_z
    niche = qualified.sort_values("niche_score", ascending=False).head(10)
    print(niche.reset_index(drop=True).to_string(
        index=False, formatters={"mean": "{:.3f}".format, "niche_score": "{:.3f}".format}))
    top = niche.iloc[0]
    print(f"\nMost niche movie: \"{top['title']}\" "
          f"(mean {top['mean']:.3f} over only {top['count']:.0f} ratings)")


def claude_answers():
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    stats, qualified = question_1(ratings_df, movies_df)
    question_2(qualified)
    question_3(qualified)


if __name__ == "__main__":
    claude_answers()
