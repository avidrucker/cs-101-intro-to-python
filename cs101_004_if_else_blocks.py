# this is an example code comment

movie_count = 3 # number of movies I saw last year
arbitrary_number = 10 # an arbitrary number

# We can use a simple "if else block" to see
# if a number if bigger than another
if movie_count > arbitrary_number:
	print("You watched a lot of movies!")
else:
	print("You watched few movies...")

# To get the mean average of 6 values
# we add them up & divide by 6
avg_movies_watched = (20 + 6 + 8 + 11 + 0 + movie_count) / 6


print("average movies watched:", avg_movies_watched)

# I add an "elif" (else-if) inbetween my "if" and "else"
# to catch the 3rd condition (if the number of movies I've
# watched is the same as the average)
if movie_count > avg_movies_watched:
	print("You watched more movies than the (mean) average.")
elif movie_count == avg_movies_watched:
  print("You watched the same # of movies as the average.")
else:
	print("You watched less movies than the (mean) average.")
