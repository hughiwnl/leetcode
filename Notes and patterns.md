Interview type shi

The various possible approaches are:

Breadth-first preparation - Revise every topic and then start practicing a variety of questions across all topics. This strategy is recommended if you have around a month to spare.

Depth-first preparation - Tackle one topic at a time - revise materials for a topic, practice lots of questions for that topic. After ensuring mastery of a topic, move on to the next topic. Repeat for all or selected topics. If you don't have much time, this might be the best way to prepare. You can focus on the High priority topics in our recommended study plan.

Depth-first-then-breadth preparation - Tackle one topic at a time - revise materials for a topic, practice a few questions for that topic. After ensuring mastery, move on to the next topic. Repeat for all topics. At the end, practice a variety of questions across all topics. This strategy takes more time than others, so it's recommended if you have more than a month.

My personal recommendation would be the Breadth-first preparation or Depth-first-then-breadth preparation. It's important to have some form of breadth-level studying / practicing in your schedule so that you don't forget about the earlier topics as you move on to later topics.

//////

These are the data structures to keep in mind and try, in order of frequency they appear in coding interview questions:

Hash Maps: Useful for making lookup efficient. This is the most common data structure used in interviews and you are guaranteed to have to use it.
Graphs: If the data is presented to you as associations between entities, you might be able to model the question as a graph and use some common graph algorithm to solve the problem.
Stack and Queue: If you need to parse a string with nested properties (such as a mathematical equation), you will almost definitely need to use stacks.
Heap: Question involves scheduling/ordering based on some priority. Also useful for finding the max K/min K/median elements in a set.
Tree/Trie: Do you need to store strings in a space-efficient manner and look for the existence of strings (or at least part of them) very quickly?


Routines
Sorting
Binary search: Useful if the input array is sorted and you need to do faster than O(n) searches
Sliding window
Two pointers
Union find
BFS/DFS
Traverse from the back
Topological Sorting
/////

Identify the Best Theoretical Time Complexity of the solution
The Best Theoretical Time Complexity (BTTC) of a solution is a time complexity you know that you cannot beat.

Some simplified examples:

The BTTC of finding the sum of numbers in array is O(n) because you have to look at every value in the array at least once
The BTTC of finding the number of groups of anagrams is O(nk) where n is the number of words and k is the maximum number of letters in a word because you have to look at each word at least once and look at each character in each word at least once
The BTTC of finding the number of islands in a matrix is O(nm) where n is the number of rows and m is the number of columns because you have to look at each cell in the matrix at least once
Why is it important to know the BTTC? So that you don't go down the rabbit hole of trying to find a solution that is faster than the BTTC. The fastest practical solution can only ever be as fast as the BTTC, not faster than the BTTC. The BTTC is not necessarily achievable in practice (hence theoretical), it just means you can never find a real solution that is faster than it. If your initial solution is slower than the BTTC, there could be opportunities to improve such that you can attain the BTTC (but not always the case). It wouldn't hurt to mention the BTTC to your interviewer, which will be taken as a positive signal and also to remind yourself that you should not try to come up with something faster than the BTTC.

Some people might think that the BTTC is simply the total number of elements in a data structure, because you need to go through each element once. This is not always true. The most famous example would be finding a number in a sorted array of numbers. The sorted property changes things a whole lot:

Finding a number would be O(log(n)) because you can use a binary search.
Finding the largest number would be O(1) because it is the last value in the array.
This is why it is important to pay attention to every detail given about the question. Be careful not to determine the incorrect BTTC due to lack of attention to the question details!

With the correct BTTC determined, you now know the time complexity of the optimal solution lies between your initial solution and the BTTC and can work your way towards it. If your solution already has the BTTC and the interviewer is asking you to optimize further, there are usually two things they are looking out for:

Do even less work. Your solution could be O(n) but making two passes of the array and the interviewer is looking for the solution that uses a single pass.
Use less space. Refer to the section below on optimizing space complexity.

/////

As software engineers, the most common type of system design you will encounter is the back end / distributed system design type. Some common back end system design interview questions include:

Design a URL shortener (e.g. Bitly)
Design a social media website (e.g. Twitter)
Design a video watching website (e.g. YouTube)
Design a chatting service (e.g. Telegram, Slack, Discord)
Design a file sharing service (e.g. Google Drive, Dropbox)
Design a ride sharing service (e.g. Uber, Lyft)
Design a photo sharing service (e.g. Flickr, Pinterest)
Design an e-commerce website (e.g. Amazon, eBay)
Design a jobs portal (e.g. LinkedIn, Indeed)
Design a web crawler (e.g. Google)
