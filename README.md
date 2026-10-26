Markdown
# Spotify Mood DJ

**Spotify Mood DJ** is a data analysis and track recommendation engine that categorizes audio tracks into discrete emotional moods—*Happy / Party*, *Chill / Relaxed*, *Angry / Intense*, and *Sad / Melancholy*—based on Russell's circumplex model of affect using track valence and energy. The project analyzes feature correlations across popularity tiers and languages, allowing users to dynamically filter and generate custom playlist exports based on mood, language, and minimum popularity constraints.

## Key Insights

* **Weak Audio Correlations with Popularity:** Single audio features (such as danceability or energy) show only weak-to-moderate correlations with popularity, showing that audio characteristics alone do not dictate track success.
* **Hit Concentration:** Hits (tracks with high popularity scores) cluster primarily in high-energy and high-valence domains (*Happy / Party*) as well as lower-energy positive domains (*Chill / Relaxed*).
* **Language Mood Discrepancies:** Mood distribution varies significantly across languages, with certain regional tracks showing a higher proportion of low-valence, low-energy songs (*Sad / Melancholy*) relative to mainstream English pop.

## Mood Map

![Mood Map](output/mood_map.png)

## How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/spotify-mood-dj.git](https://github.com/your-username/spotify-mood-dj.git)
   cd spotify-mood-dj