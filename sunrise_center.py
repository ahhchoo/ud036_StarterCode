import fresh_tomatoes
import sunrise
manhattan_sunrise = sunrise.Sunrise("New York Sunrise",
                        "https://media-cdn.tripadvisor.com/media/photo-s/03/9b/2d/f2/new-york-city.jpg",
                        "https://www.youtube.com/watch?v=L6Wo4MZtnGI")

tokyoBay_sunrise = sunrise.Sunrise("Tokyo Bay Sunrise",
                                    "http://www.destination360.com/asia/japan/tokyo/images/s/tokyo-bay.jpg",
                                    "https://www.youtube.com/watch?v=0PoopxIuWCU")

mountFuji_sunrise = sunrise.Sunrise("Mount Fuji Sunrise",
                                    "https://mytokyoguide.files.wordpress.com/2011/06/sept-121.jpg",
                                    "https://www.youtube.com/watch?v=4oYsizhUr0g")

phuket_sunrise = sunrise.Sunrise("Phuket Sunrise",
                                    "http://phuket9.com/wp-content/uploads/2013/10/rawai-private-027-1024x682.jpg",
                                    "https://www.youtube.com/watch?v=u371cb_WlQs")

athens_sunrise = sunrise.Sunrise("Athens Sunrise",
                                    "http://www.travelpage.gr/UserFiles/Image/regions/Athens/500x500_d9918b7b42e805bf3e16957e7eef5ca9.jpg",
                                    "https://www.youtube.com/watch?v=aLt88oh6jps")

southCarolina_sunrise = sunrise.Sunrise("South Carolina Sunrise",
                                            "http://www.isleofpalmsexplorer.com/Flipkey/IsleofPalms.jpg",
                                            "https://www.youtube.com/watch?v=C9HR2yh_kvA")

sunrises = [manhattan_sunrise, tokyoBay_sunrise, mountFuji_sunrise, phuket_sunrise, athens_sunrise, southCarolina_sunrise]

fresh_tomatoes.open_movies_page(sunrises)
