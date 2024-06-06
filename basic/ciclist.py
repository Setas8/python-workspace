departureHour = int(input("Departure Hour: "))
departureMin = int(input("Departure Min: "))
departureSecs = int(input("Departure Secs: "))
tripSecs =  int(input("trip seconds: "))

initialSecs = departureHour*3600 + departureMin*60 + departureSecs
finalSecs = initialSecs + tripSecs
arrivalhour = finalSecs // 3600
arrivalMin = (finalSecs % 3600) // 60
arrivalSecs = (finalSecs % 3600) % 60

print("Time of arrival")
print(arrivalhour,":",arrivalMin,":",arrivalSecs)
