# [LC 355. Design Twitter)](https://leetcode.com/problems/design-twitter/description/)

## General Notes

- PEDAC: Problem
  - class methods and inputs
    - `Twitter()`: constructor
      - input: none
      - output: a new `Twitter` instance / object
    - `postTweet(userId, tweetId)`
      - input: string `word`
      - output: none
    - `getNewsFeed(userId)`
      - input: int
      - output: int array of `tweetId`'s in DSC order of tweet post timestamp of size in range \[0, 10]
    - `follow(followerId, followeeId)`
      - input: both ints
      - output: none
      - user with id `folloerId` starts following user with id `followeeId`
    - `unfollow(followerId, followeeId)`
      - input: both ints
      - output: none
      - user with id `folloerId` stops following user with id `followeeId`
  - constraints
    - `userId`, `followerId`, `followeeId`:
      - ints of values in the range \[1, 500]
    - `tweetId`: int in the range \[0, 10^4]
      - guaranteed to be unique

## Solution 1: array and hashmap solution

- method-dependent T & S complexity solution
  - `postTweet()`: O(1) T and O(1)? S
  - `getNewsFeed()`: O(N) T and O(1) S
  - `follow()`: O(1) T and O(1)? S
  - `unfollow()`: O(1) T and O(1)? S
- summary
  - `Twitter()` constructor initiates these instance variables:
    - `tweets`: array of `[userId, tweetId]` elements
    - `followers`: hashmap that maps each `userId` to a set of `followerId`'s
  - `follow()` and `unfollow()` methods add and remove `followerIds` from the sets of `followeeId`'s or `userId`'s of the `followers` hashmap instance variable
  - `postTweet()` pushes an element `[userId, tweetId]` to the `tweets` instance variable
  - `getNewsFeed()` loops thru its `tweets` array instance variable backwards and pushes tweets to a new array `res` that are either followed by the user with id `userId` or by the user itself until the loop finishes or `res` reaches size 10
