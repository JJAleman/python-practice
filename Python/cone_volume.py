import math

# Finding the volume of a cone
def cone_volume(h, r):
		volume = round(((1/3) * math.pi * (r**2) * h),2)
		
		if(volume == 0):
				return 0
		else: 
				return volume
print(cone_volume(3, 2))
