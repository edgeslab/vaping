# Cannabis Legalization and Vaping
Supplementary materials for S. Adhikari, A. Uppal, R. Mermelstein, T. Berger-Wolf, E. Zheleva. Understanding the Dynamics between Vaping and Cannabis Legalization Using Twitter Opinions. AAAI Conference on Web and Social Media (ICWSM) 2021.

## Description
The following is the description of the folders and subfolders.
- `instructions`
  - `labelbox`: Instructions for annotating 500 JUUL and 500 cannabis-related tweets for three questions (Q1, Q2, Q3) using LabelBox platform.
  - `mturk`: Instructions for annotating 1000 JUUL and 1000 cannabis-related tweets for two questions (Q1, Q2) using Amazon Mechanical Turk platform.

- `dataset`
  - `mapping`: `allJuulIds.zip` and `allCannabisIds.zip` contain the mapping between internal ID and actual Tweet ID. These are large files containing Tweet IDs for all tweets extracted by keyword/hashtag filtering as described in the paper.
  - `labelbox`: Annotations for Tweets in LabelBox with two annotators, `A1` and `A2`, per tweet.
  - `mturk`: Annotations for Tweets in Amazon Mechanical Turk performed with three annotators per tweet.

## Questions
Here `<target>` can be either `e-cigarettes` or `cannabis`.

Q1. To the best of your judgment, is this tweet referring to `<target>`?

The answer should be one of the following:
- Yes: The tweet is referring to `<target>`.
- No: The tweet is not referring to `<target>`.

Q2. To the best of your judgment, is the person who wrote this tweet in favor of or against `<target>` use?

The answer should be one of the following:
- In favor: The tweet suggests that the tweet author is in favor of `<target>` use. This can be expressed by tweeting about personal `<target>` use, the experience of `<target>` use, intention to use, positive opinion on `<target>`, or advantages of `<target>`. 
- Against: The tweet suggests that the tweet author is against `<target>` use. This opposition can be expressed with negative experiences, negative opinions, intention to quit, information about harmful effects or disadvantages. 
- Neither: The tweet is neutral, or the author’s position can not be determined from the tweet, or the tweet is not about `<target>`.

Q3. To the best of your judgment, is this tweet about a personal experience, opinion, or observation?

The answer should be one of the following:
- Yes: The tweet shares personal experience, opinion, or observation.
- No: The tweet is not personal. Typically promotional tweets (advertisements) and news-related tweets as well as quotes from others are not considered personal tweets.
- Not sure: The answer “Yes” or “No” cannot be decided based on the tweet.
