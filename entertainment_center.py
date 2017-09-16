import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Story of a boy and his toys that come to life.",
                        "http://vignette4.wikia.nocookie.net" +
                        "/pixar/images/4/4c/Toy-story-movie" +
                        "-posters-4.jpg/revision/latest" +
                        "?cb=20160329080002",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
avatar = media.Movie("Avatar",
                     "A story about Aliens trying to survive in the" +
                     "poisonous environment by interacting with humans",
                     "http://intlportal2.s3.foxfilm.com" +
                     "/intlportal2/56ba791b20287.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

annabelle_creations = media.Movie("Annabelle Creations",
                                  "A horror story of a doll getting " +
                                  "possessed " +
                                  "by evil and killing the people",
                                  "https://i1.wp.com/bloody-disgusting.com" +
                                  "/wp-content/uploads/2017/03/" +
                                  "ANNABELLE-CREATION-POSTER." +
                                  "jpg?resize=691%2C1024",
                                  "https://www.youtube.com/watch" +
                                  "?v=KisPhy7T__Q")
it = media.Movie("It",
                 "A group of children battle the murderous, " +
                 "bloodthirsty clown known as Pennywise.",
                 "https://i.pinimg.com/736x" +
                 "/3e/33/92/3e3392d339c2b8028" +
                 "007d0f9af979be4---movies" +
                 "-it-movie-.jpg",
                 "https://www.youtube.com/watch?v=FnCdOQsX5kc")

simran = media.Movie("Simran",
                     "A Gujarati housekeeping lady in the US allows " +
                     "ambition to get the better of her & gets " +
                     "involved in a world of crime.",
                     "https://cdn.pinkvilla.com/files/SimranPoster.jpg",
                     "https://www.youtube.com/watch?v=_LUe4r6eeQA")

logan = media.Movie("Logan",
                    "In the near future, a weary Logan " +
                    "(Hugh Jackman) cares for an " +
                    "ailing Professor X.",
                    "https://encrypted-tbn0.gstatic.com/images" +
                    "?q=tbn:ANd9GcQ5CYQBjtbAMg5wyQirPA_" +
                    "vIC_41-KwjaogMdFg3YL9ADz9T2DUpg",
                    "https://www.youtube.com/watch?v=gbug3zTm3Ws")

movies = [toy_story, avatar, annabelle_creations, it, logan, simran]
fresh_tomatoes.open_movies_page(movies)
