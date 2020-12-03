# IDENTIPAINT

Identipaint is an art history flashcard website that trains users to identify artists by their paintings, using the principles of spaced repetition and interleaving.

This project is inspired by experiments conducted by Nate Kornell and Robert A Bjork at UCLA in 2008. They found that showing students paintings by several artists in interleaved sets later increased their ability to identify different paintings by those artists. [Learning concepts and categories: Is spacing the "enemy of induction"?](https://sites.williams.edu/nk2/files/2011/08/Kornell.Bjork_.2008a.pdf)

## Feature list

-   ### Must haves

    -   [ ] Display random sets of paintings, their titles and artists, by making calls to WikiArt API
    -   [ ] Login and registration in order to track user familiarity with artists

-   ### Neccesary features

    -   [ ] Replicate Kornell and Bjork experiment: serve a series of paintings along with artist name, then test user by having them identify artists of new paintings
    -   [ ] Implement Django authentication system for logins
    -   [ ] Use Foundation CSS framework for front-end design

-   ### Nicer features

    -   [ ] Provide user statistics that show progress in ability to identify artists
    -   [ ] Spaced repetition: more familiar artists are shown less frequently

-   ### Future plans
    -   [ ] More test modes: Guess painting titles, order paintings by date, etc.
    -   [ ] Progressive training: users move from being shown paintings in distantly related movements to paintings by more closely related artists
