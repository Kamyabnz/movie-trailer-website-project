import media 
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                        "a story of a boy that plays with his toys",
                        "https://gfx.videobuster.de/archive/v/c-MvmFJ6r-BNo00ZPIHKOTwcz0lMkawrSUyRjAyJTJGaW1hmSUyRmpwZWclMkZiZjVhNGJjv7bDZN7psTFjYzBj7jBm9jUuanBnJnI9d-84/toy-story.jpg",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

avatar = media.Movie("Avatar", 
                    "a marine on a different planet",
                    "https://i.pinimg.com/originals/24/e1/8a/24e18a4a2f82ba68b6e835c7178285a5.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

shutter_island = media.Movie("Shutter Island", 
                    "a police officer is investingating a murder on an isnland",
                    "https://s1.thcdn.com/productimg/0/600/600/63/10080563-1280330043-579000.jpg",
                    "https://www.youtube.com/watch?v=5iaYLCiq5RM")

wind_river = media.Movie("Wind River", 
                    "a murder has accured in Canada",
                    "https://www.wildbunch-germany.de/api/wildbunch/poster_image%2Fwindriver%2Fstage/WindRiver-A4-RGB.jpg",
                    "https://www.youtube.com/watch?v=qnXzC7Kh-N0")

lord_of_the_rings = media.Movie("Lord of the Rings", 
                    "a marine on a different planet",
                    "https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781608873821/the-lord-of-the-rings-9781608873821_hr.jpg",
                    "https://www.youtube.com/watch?v=V75dMMIW2B4")

split = media.Movie("Split", 
                    "a man with 43 different personalities",
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrUkpZ_VrCZkcSWpNL73eRCRFoGfKw0byUfSdJFI9pS1ZZtUgi",
                    "https://www.youtube.com/watch?v=1VqWDr2ldPI")

movies = [toy_story, avatar, shutter_island, wind_river, lord_of_the_rings, split]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)