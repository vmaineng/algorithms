def longest_subarray_sum(nums, target_sum):
  #receive a list of integers, and a target target_sum
  #return the length of longest subarry that returns the target
  #ex: 

  #iterate through nums, with left and right at 0
  #keep expanding window while total of window < = target_sum
  #if it == target_sum, capture the window size
  #update it for max variable


  max_window = 0
  left = 0
  right = 0
  total = 0
  
  for right in range(0, len(nums)):
    total += nums[right]

    while total  > target_sum:
      total -= nums[left]
      left += 1
    if total == target_sum:
      max_window = max(max_window, (right - left + 1) )

  return max_window if max_window != 0 else -1
      
    