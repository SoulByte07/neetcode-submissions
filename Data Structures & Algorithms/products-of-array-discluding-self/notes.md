you cant use this trick:
product( arr )
product_except_curr = product( arr ) / current
because of 0

sol 1: 
if 0 in arr:
	cal product except 0
	place that val in the 0 th places



try and except wasnt working because if arr have multiple 0's , we are cooked
