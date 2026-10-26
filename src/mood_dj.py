import pandas as pd


def mood_dj(df, mood, language=None, min_popularity=50, n=10):
   
    valid_moods = [
        "Happy / Party",
        "Chill / Relaxed",
        "Angry / Intense",
        "Sad / Melancholy",
    ]
    if mood not in valid_moods:
        raise ValueError(
            f"Invalid mood: '{mood}'. Must be one of {valid_moods}"
        )

    filtered_df = df[(df["mood"] == mood) & (df["popularity"] >= min_popularity)]

    if language is not None:
        filtered_df = filtered_df[filtered_df["language"] == language]

    filtered_df = filtered_df.sort_values(by="popularity", ascending=False)
    filtered_df = filtered_df.drop_duplicates(
        subset=["track_name", "artist_name"]
    )
    filtered_df = filtered_df.head(n)

    cols = ["track_name", "artist_name", "popularity", "mood", "language"]
    return filtered_df[cols].reset_index(drop=True)