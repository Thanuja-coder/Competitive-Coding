#Container with Most water
#[1,8,6,2,5,4,8,3,7]

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

left = 0
right = len(height) - 1

max_water = 0

while left < right:

    width = right - left

    h = min(height[left], height[right])

    water = width * h

    max_water = max(max_water, water)

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print("Maximum water:", max_water)