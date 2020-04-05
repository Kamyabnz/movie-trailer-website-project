import media
import fresh_tomatoes


# The instances of Movie class with each specific attributes
# as parameters, we have the following Instances.
toy_story = media.Movie(
                    "Toy Story",
                    "A story of a boy that plays with his toys",
                    "https://tinyurl.com/rcsb5lm",
                    "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

avatar = media.Movie(
                    "Avatar",
                    "A marine on a different planet",
                    "https://tinyurl.com/wlk9kz6",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

shutter_island = media.Movie(
                    "Shutter Island",
                    "A police officer is investingating a murder",
                    "https://tinyurl.com/scmfe9q",
                    "https://www.youtube.com/watch?v=5iaYLCiq5RM")

wind_river = media.Movie(
                    "Wind River",
                    "A murder has accured in Canada",
                    "https://tinyurl.com/t756lec",
                    "https://www.youtube.com/watch?v=qnXzC7Kh-N0")

lord_of_the_rings = media.Movie(
                    "Lord of the Rings",
                    "The fantasy world of J. R. R. Tolkien",
                    "https://tinyurl.com/w6ed66h",
                    "https://www.youtube.com/watch?v=V75dMMIW2B4")

split = media.Movie(
                    "Split",
                    "A man with 23 different personalities",
                    "https://tinyurl.com/yx53gqxb",
                    "https://www.youtube.com/watch?v=1VqWDr2ldPI")

# List of instances of the Movie Class created and given to the Function
# open_movies_page inside of the fresh_tomatoes.py that creates the webpage
print(media.Movie.__doc__)
movies = [
    toy_story,
    avatar,
    shutter_island,
    wind_river,
    lord_of_the_rings,
    split]
fresh_tomatoes.open_movies_page(movies)
print("THE fresh_tomatoes.html HAS BEEN CREATED")
