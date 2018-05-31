'''Stores details of movies and displays them on a website.'''
import media
import fresh_tomatoes
'''Creates six Movie objects, initialising these objects with'''
'''title,poster image,video trailer link.'''
maze_runner = media.Movie("Maze runner:3",
                          "https://cdn.traileraddict.com/content"
                          "/20th-century-fox/maze-runner-death-cure-3.jpg",
                          "https://www.youtube.com/watch?v=4-BTxXm8KSg",
                          "Thomas leads some escaped Gladers on their final"
                          "and most dangerous mission yet."
                          )
rampage = media.Movie("Rampage",
                      "https://images-na.ssl-images-amazon.com/images"
                      "/M/MV5BOTkzNTg5NjI5MV5BMl5BanBnXkFtZTgwMzM"
                      "4NjkxNDM@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=coOKvrsmQiI",
                      "Okoye teams up with a discredited genetic engineer"
                      "and the military to secure an antidote and prevent a"
                      "global catastrophe."
                      )
infinity_wars = media.Movie("Avengers:Infinity Wars",
                            "https://encrypted-tbn0.gstatic.com/"
                            "images?q=tbn:ANd9GcQycbVjn3F8BG8D7YiSni"
                            "8p2DupwF3TblHqgaYrwzFLjPz8sLBE1A",
                            "https://www.youtube.com/watch?v=6ZfuNTqbHE8",
                            "Iron Man, Thor, Hulk and the rest of the Avengers"
                            "unite to battle their most powerful enemy"
                            "yet -- the evil Thanos."
                            )
creed = media.Movie("Creed",
                    "https://mir-s3-cdn-cf.behance.net/project"
                    "_modules/max_3840/f9f21429460029.55f403996fac2.jpg",
                    "https://www.youtube.com/watch?v=Uv554B7YHk4",
                    "Adonis Johnson, the son of heavyweight"
                    "champion Apollo Creed embraces his legacy"
                    "as a boxer and seeks mentorship from"
                    "Rocky Balboa, his father's old friend and rival."
                    )
dunkirk = media.Movie("Dunkirk",
                      "http://entertainment.ie/images_content/H7tbgZh.jpg",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU",
                      "In May 1940, Germany advanced into France, trapping"
                      "Allied troops on the beaches of Dunkirk. Under air and"
                      "ground cover from British and French forces, troops"
                      "were slowly and methodically evacuated from the beach."
                      )
prisoners = media.Movie("Prisoners",
                        "https://www.warnerbros.com/sites/default"
                        "/files/styles/key_art_270x400/public/"
                        "prisoners_keyart.jpg?itok=oH3lmhFq",
                        "https://www.youtube.com/watch?v=2SupordEUpw&t=1s",
                        "When the police take time to find Keller Dover's "
                        "daughter and her friend, he decides"
                        "to go on a search himself."
                        "His desperation leads him closer"
                        "to finding the truth"
                        "but also jeopardises his own life."
                        )
''' Store the Movie objects in a list.'''
movies = [maze_runner, rampage, infinity_wars, creed, dunkirk, prisoners]
''' Open the website in the user's browser, featuring the movies.'''
fresh_tomatoes.open_movies_page(movies)
