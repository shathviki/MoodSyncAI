# MoodSyncAI

MoodSyncAI is a smart music recommendation app that detects your emotional state using computer vision and curates a personalized Spotify playlist to match your mood. By analyzing facial expressions, MoodSyncAI enhances the music-listening experience, offering tracks that align with your current emotions.

#  Features

##  🎭 Mood Detection via Camera

*  Uses facial recognition and emotion detection to analyze your mood in real time.

*  Leverages computer vision using OpenCV, and ML through the use of TensorFlow and Deepface library for facial analysis with pre-trained models.

*  Classifies moods into predefined categories: Happy, Sad, Neutral, Surprised, Angry

##  🎵 Mood-Based Music Recommendations

*  Integrates with Spotify to curate mood-based playlists.

*  Dynamically selects tracks that best fit your emotional state:

   *  Happy: Upbeat pop, energetic EDM, or feel-good anthems.

   *  Sad: Soft indie, emotional ballads, or soothing instrumentals.

   * Stressed: Lo-fi beats, classical music, or calming acoustic tracks.

   * Excited: High-energy rock, hip-hop, or dance music.

   * Relaxed: Jazz, ambient, or nature sounds.

##  🔄 User Feedback & Personalization

*  Users can rate how well the recommended playlist matches their mood.

*  Manual mood adjustment option to refine recommendations.

*  Feedback loop to improve future suggestions through machine learning.

#  Tech Stack

*  Frontend: React Native (for mobile) or React (for web)

*  Backend: Node.js with Express.js

*  Database: MongoDB or Firebase (for user preferences & history)

*  Machine Learning: TensorFlow.js / OpenCV for emotion detection

*  API Integrations:

    * Spotify API for fetching and playing music

    * Emotion Detection API (Affectiva, Azure, or Google Cloud Vision) for mood analysis



Start syncing your emotions with music today! 🎶

