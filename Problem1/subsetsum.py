# README
# Using Dynamic Pro­gram­ming and mem­o­iza­tion,
# in this case is Dynamic Programming Top-Down approach.
# Time Com­plex­ity: O(n) , Space Com­plex­ity : O(n)

def subsetsum(array,targetSum):

    if targetSum == 0 or targetSum < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == targetSum:
            return [array[0]]
        else:
            # Break the prob­lem into sub-problems and solve them as needed and store the solu­tion for future
            currentSubArray = subsetsum(array[1:],(targetSum - array[0])) 
            if currentSubArray:
                return [array[0]] + currentSubArray  # expand subarray
            else:
                return subsetsum(array[1:],targetSum)
                

array = [18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833, 3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411]

result = subsetsum(array, 100000000)

print('Subset found: ' + str(result))
print('Test sum = ' + str(sum(result)))