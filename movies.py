import fresh_tomatoes
import media


good_will_hunting = media.Movie("Good Will Hunting", 
                                "Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist to find direction in his life.", 
                                "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png", 
                                "https://www.youtube.com/watch?v=PaZVjZEFkRs")



ocean_11 = media.Movie("Ocean's Eleven", 
                        "Danny Ocean and his ten accomplices plan to rob three Las Vegas casinos simultaneously.", 
                        "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTx9V4e8vu1PtIcA_yBHGl8j0-4kytr25IyOEe4tHVNSAo_6sje", 
                        "https://www.youtube.com/watch?v=imm6OR605UI")



hunger_games = media.Movie("Hunger Games", 
                            "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games: a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.", 
                            "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNJ0NIhwRUUX2f-8oIrWSWuKf7WT38JvNTlThf1BxdRltYEtOb", 
                            "https://www.youtube.com/watch?v=mfmrPu43DF8")



jojo = media.Movie("Jojo Rabbit", 
                    "A young boy in Hitler\'s army finds out his mother is hiding a Jewish girl in their home.", 
                    "https://lumiere-a.akamaihd.net/v1/images/image_a094a4bd.jpeg?region=0,0,800,1200", 
                    "https://www.youtube.com/watch?v=tL4McUzXfFI")


nineteen_seventeen = media.Movie("1917", 
                                "April 6th, 1917. As a regiment assembles to wage war deep in enemy territory, two soldiers are assigned to race against time and deliver a message that will stop 1,600 men from walking straight into a deadly trap.", 
                                "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6397/6397919_so.jpg", 
                                "https://www.youtube.com/watch?v=gZjQROMAh_s")


dark_knight = media.Movie("Dark Knight", 
                            "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.", 
                            "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", 
                            "https://www.youtube.com/watch?v=EXeTwQWrcwY")

#print(dark_knight.tralier_youtube_url)
movies = [good_will_hunting, ocean_11, hunger_games, jojo, nineteen_seventeen, dark_knight]
fresh_tomatoes.open_movies_page(movies)