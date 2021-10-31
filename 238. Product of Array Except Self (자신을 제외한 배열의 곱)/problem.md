## 238. Product of Array Except Self
## 238. 자신을 제외한 배열의 곱

<br>

### 문제 : 

**Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.**

**배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라. 나눗셈을 하지 않고 O(n)에 풀이하라.**

--------------------------------------

예제 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

예제 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]