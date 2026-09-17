# HW0 writeup

**Name:** Shaylee O'Grady
**Date:** 2026-09-10

Replace every placeholder below with your answer. Every number you give comes from a script in this repo; say which one.

## Part 1. Basic rating statistics

Code: `human_part1.py`. One or two sentences per answer, with the numbers.

**(a) How many ratings, users, and movies are there, and how are ratings distributed across 1–5 stars?**

There are 100000 ratings, 943 users, 1682 movies, and the ratings are distributed across the 1-5 stars as follows:
1     6110
2    11370
3    27145
4    34174
5    21201

**(b) What is the median number of ratings per user, and how many users have 100 or more ratings?**

The median number of ratings per user is 65.0 and
364 users have 100 or more ratings.

**(c) Which 10 movies have the most ratings?**

These 10 movies have the most ratings : title
Star Wars (1977)                 583
Contact (1997)                   509
Fargo (1996)                     508
Return of the Jedi (1983)        507
Liar Liar (1997)                 485
English Patient, The (1996)      481
Scream (1996)                    478
Toy Story (1995)                 452
Air Force One (1997)             431
Independence Day (ID4) (1996)    429

**(d) Among movies with at least 20 ratings, which 10 have the highest mean rating?**

This first list is the movies with the highest mean ratings 
title
Close Shave, A (1995)                                     4.491071
Schindler's List (1993)                                   4.466443
Wrong Trousers, The (1993)                                4.466102
Casablanca (1942)                                         4.456790
Wallace & Gromit: The Best of Aardman Animation (1996)    4.447761
Shawshank Redemption, The (1994)                          4.445230
Rear Window (1954)                                        4.387560
Usual Suspects, The (1995)                                4.385768
Star Wars (1977)                                          4.358491
12 Angry Men (1957)                                       4.344000

This list shows those movies with the rating counts
Name: rating, dtype: float64
title
Close Shave, A (1995)                                     112
Schindler's List (1993)                                   298
Wrong Trousers, The (1993)                                118
Casablanca (1942)                                         243
Wallace & Gromit: The Best of Aardman Animation (1996)     67
Shawshank Redemption, The (1994)                          283
Rear Window (1954)                                        209
Usual Suspects, The (1995)                                267
Star Wars (1977)                                          583
12 Angry Men (1957)                                       125

**Anything you got stuck on (what you tried, where it broke), or "none":**

Took me quite a while to refresh on python and figure out what I needed, but got past it all with lots of trial and error. 

## Part 2. The best movie

Code: `human_part2.py`.

**My rule:** The best movie will have the highest mean star rating, out of the movies with at least 40 ratings. 

**One rule I considered and rejected, and why:** I rejected just plain highest mean star rating because one person could've rated an unpopular movie a 5 stars because they loved it and that wouldn't be fair. 

**Top 10 under my rule:** 
Here's the list with their ratings
title
Close Shave, A (1995)                                     4.491071
Schindler's List (1993)                                   4.466443
Wrong Trousers, The (1993)                                4.466102
Casablanca (1942)                                         4.456790
Wallace & Gromit: The Best of Aardman Animation (1996)    4.447761
Shawshank Redemption, The (1994)                          4.445230
Rear Window (1954)                                        4.387560
Usual Suspects, The (1995)                                4.385768
Star Wars (1977)                                          4.358491
12 Angry Men (1957)                                       4.344000

**Why my rule, in at most 150 words. Name one thing it gains and one thing it loses:**

It gains credibility because 40 ratings is a pretty large number of ratings (assuming that's 40 different people) so, it must be a pretty credible average. It could definitely be thrown off by outliers though. 

## Part 3. The most ___ movie

Code: `human_part3.py`.

**My adjective:** Niche

**My definition** (one sentence, precise enough that a classmate could code it)**:** Has only 1 rating, meaning very few viewers have watched it or thought very much about it. 

**One definition I considered and rejected, and why:** saying only a couple ratings because I realized I needed to be specific

**Top 5 under my definition:**

title
Aiqing wansui (1994)           1
All Things Fair (1996)         1
Angel on My Shoulder (1946)    1
Angela (1995)                  1
August (1996)                  1

**What your definition captures, what it misses, and where "niche-ness" lives in this data — the
genre labels, what the crowd did, or the words in the titles. At most 150 words:**

My definition captures the overlooked/unknown movies, the sort of outliers of this dataset, making these movies niche. They live in the movies with only 1 rating. It misses the odd movies with more than 1 rating but very few ratings still. 

## Part 4. Claude's answers

Claude answers the same three questions in `claude_answers_1_2_3.py`, without seeing your code
or your answers.

**Did its numbers for Part 1 match yours? If not, which, and what did you find?**

Match there were a few visual improvements and specifics (like percent of the data) that were included in addition. 

## Part 5. Comparing the best movie

**Claude's rule:**

To find a "best" movie that isn't an artifact of a small sample, use a Bayesian
("IMDB-style") weighted rating that shrinks each movie's mean toward the overall
mean, by an amount that shrinks as the movie collects more ratings:

    weighted = (v / (v + m)) * R  +  (m / (v + m)) * C
R = the movie's own mean rating
    v = the movie's number of ratings
    m = a prior strength, set here to the median rating count among qualified movies
    C = the mean rating across all qualified movies

(prior strength m = 69 ratings, overall mean C = 3.370)

**Read what Claude wrote about its rule. Does it anywhere admit the rule was a choice, and that a different rule was possible? Or does it give its answer as simply the answer? Quote the sentence that decides it:**

"To find a "best" movie that isn't an artifact of a small sample"

best in quotes and clarification shows it thought of other choices. 

**Your Part 2 top 10 and Claude's Part 2 top 10 — not the Part 1(d) lists. Where do they differ, and why?**

6 of 10 of the movies are the same. They differ in the beggining, and on the order because the organization was by a weighted mean rating score using Baysian model. 

**Better for what purpose? Name a situation where your rule is the right one and a situation where Claude's is. At most 150 words. You may conclude yours, its, or neither:**

Claude's is better for movies with not that many ratings, or with scattered ratings where people all felt very differnetly because my mean is effected by outliers. 


## Part 6. Comparing the most ___ movie

**Claude's definition:**

Niche : movies that stand out for being *better liked than they are watched

**Is Claude's film in your top 5?**

No we don't have any of the same.

**What Claude's definition sees that yours does not, and the reverse. At most 150 words:**

It also pays attention to what the rating scores were so that the niche movies are also well liked niche movies. Mine really limits the number of ratings though, so I feel my list is full of more unqiue movies. 

## Working with Claude

**What you asked Claude for during Parts 1–3** (debugging and installing only — say what you
got stuck on)**:**

Not really anything with claude I just got stuck in coding moments, but when I asked claude for support it was actually very comforting to know it understood my assignment and could provide suggestions. I asked it what parts of Python I should review and it gave me a list of potentially helpful code to review, and that was awesome!

**Something Claude said that you could not verify, and why. Or "none," and how you checked:**

It gave me a list of suggested Python methods that would be good to refresh for this assignment, and I couldn't verify those so I did my own searching/reading on google to remind myself what I needed to do. 

**What you would do differently next time, in 3–5 sentences:**

Take time to read the assignment (skim/assess it) on the day it is released so that I can more accurately schedule my time. 

**Where did this assignment slow you down for a reason that was its fault, not yours? Point at
the step. Or "nowhere." One or two sentences:**

I wasn't slowed down by any instructions or assignment flaws. Nowhere. 

**Hours spent:** 7

**Anyone who helped you, or "no one":** My Comp Sci friend Reese Preston. 
